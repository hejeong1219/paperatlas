import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/paperGraph.scss"
// @ts-ignore
import script from "./scripts/paperGraph.inline"
import { resolveRelative } from "../util/path"
import { QuartzPluginData } from "../plugins/vfile"

function asList(value: unknown): string[] {
  if (Array.isArray(value)) {
    return value.filter((item): item is string => typeof item === "string")
  }
  if (typeof value === "string" && value.length > 0) {
    return [value]
  }
  return []
}

function labelize(value: string): string {
  return value
    .split("-")
    .map((part) => (part ? part[0].toUpperCase() + part.slice(1) : part))
    .join(" ")
}

type GraphNode = {
  id: string
  slug: string
  title: string
  summary: string
  year?: number
  journal?: string
  cancers: string[]
  modalities: string[]
  themes: string[]
  topic: string
  cmAxis: string
  href: string
}

type GraphLink = {
  source: string
  target: string
  weight: number
  reasons: string[]
}

function shared(a: string[], b: string[]) {
  return a.filter((item) => b.includes(item))
}

function buildGraph(pages: QuartzPluginData[], currentSlug: string): { nodes: GraphNode[]; links: GraphLink[] } {
  const inferTopic = (page: QuartzPluginData): string => {
    const slug = page.slug ?? ""
    if (slug.startsWith("analyses/") &&
        (slug.includes("ptmanchor") || slug.includes("copheemap"))) return "ptmanchor"
    if (slug.startsWith("analyses/") && slug.includes("cancer-resistance")) return "resistance"
    if (slug.startsWith("analyses/") && slug.includes("b-cell-neoantigen")) return "bcell-neoantigen"
    if (slug.startsWith("analyses/") && slug.includes("cancer-multiomics")) return "cancer-multiomics"
    const fm = page.frontmatter as Record<string, unknown> | undefined
    let t = (fm?.topic as string) ?? "other"
    // Normalize topic variants into the canonical cluster keys
    if (t.startsWith("cancer-multiomics") || t.startsWith("multiomics-")) t = "cancer-multiomics"
    if (t.startsWith("b-cell-neoantigen")) t = "bcell-neoantigen"
    return t
  }

  const nodes: GraphNode[] = pages.map((page) => ({
    id: page.slug!,
    slug: page.slug!,
    title: page.frontmatter?.title ?? "Untitled",
    summary: page.description?.trim() ?? "No summary available yet.",
    year: page.frontmatter?.year as number | undefined,
    journal: page.frontmatter?.journal as string | undefined,
    cancers: asList(page.frontmatter?.cancer_types),
    modalities: asList(page.frontmatter?.modalities),
    themes: asList(page.frontmatter?.themes),
    topic: inferTopic(page),
    cmAxis: ((page.frontmatter as Record<string, unknown> | undefined)?.cm_axis as string) ?? "",
    href: resolveRelative(currentSlug as any, page.slug! as any),
  }))

  const pageMap = new Map(pages.map((page) => [page.slug!, page]))
  const links: GraphLink[] = []

  for (let i = 0; i < nodes.length; i++) {
    for (let j = i + 1; j < nodes.length; j++) {
      const left = nodes[i]
      const right = nodes[j]
      const sameTopic = left.topic === right.topic

      const leftPage = pageMap.get(left.slug)
      const rightPage = pageMap.get(right.slug)
      const leftLinks = asList(leftPage?.links)
      const rightLinks = asList(rightPage?.links)
      // Explicit co-citation wiki link injected into the note bodies
      const directLink =
        leftLinks.includes(right.slug) || rightLinks.includes(left.slug)

      // Same-topic papers auto-cluster by shared metadata; cross-topic pairs
      // only connect when an explicit co-citation link bridges them — this keeps
      // the topic clusters intact while showing real paper-to-paper connections.
      if (!sameTopic && !directLink) continue

      const reasons: string[] = sameTopic
        ? [`Topic: ${labelize(left.topic)}`]
        : ["Co-citation bridge"]
      let weight = sameTopic ? 1 : 2

      if (sameTopic) {
        const sharedCancer = shared(left.cancers, right.cancers)
        if (sharedCancer.length > 0) {
          reasons.push(`Shared cancer: ${sharedCancer.map(labelize).join(", ")}`)
          weight += sharedCancer.length * 2
        }
        const sharedModalities = shared(left.modalities, right.modalities)
        if (sharedModalities.length > 0) {
          reasons.push(`Shared modality: ${sharedModalities.map(labelize).join(", ")}`)
          weight += sharedModalities.length * 2
        }
        const sharedThemes = shared(left.themes, right.themes)
        if (sharedThemes.length > 0) {
          reasons.push(`Shared theme: ${sharedThemes.map(labelize).join(", ")}`)
          weight += sharedThemes.length
        }
        if (left.journal && right.journal && left.journal === right.journal) {
          reasons.push(`Same journal: ${left.journal}`)
          weight += 1
        }
        const descMention =
          leftPage?.description?.includes(right.title) ||
          rightPage?.description?.includes(left.title)
        if (descMention) {
          reasons.push("Mentioned in summary")
          weight += 1
        }
      }

      if (directLink) {
        reasons.push("Direct wiki connection")
        weight += 2
      }

      if (weight > 1) {
        links.push({
          source: left.id,
          target: right.id,
          weight,
          reasons,
        })
      }
    }
  }

  return { nodes, links }
}

interface PaperGraphOptions {
  title?: string
  eyebrow?: string
  helpText?: string
  compact?: boolean
  linkOnly?: boolean
}

export default ((opts?: Partial<PaperGraphOptions>) => {
  const PaperGraph: QuartzComponent = ({ fileData, allFiles }: QuartzComponentProps) => {
    const papers = allFiles.filter((page) => {
      const slug = page.slug
      if (!slug) return false
      // Papers
      if (slug.startsWith("sources/") && slug !== "sources/index") return true
      // User manuscripts/proposals (anchor pages and journal-club deep-dives)
      if (slug.startsWith("analyses/") &&
          (slug.endsWith("-manuscript-anchor") ||
           slug.endsWith("-proposal-anchor") ||
           slug.endsWith("-deep-dive"))) return true
      return false
    })
    const graph = buildGraph(papers, fileData.slug!)
    const compact = opts?.compact ?? false

    return (
      <section
        class={`paper-graph ${compact ? "compact" : ""}`}
        data-paper-graph
        data-link-only={opts?.linkOnly ? "true" : "false"}
        data-graph={JSON.stringify(graph)}
      >
        <div class="paper-graph-header">
          <div>
            <p class="eyebrow">{opts?.eyebrow ?? "Connectivity Map"}</p>
            <h2>{opts?.title ?? "Paper Graph"}</h2>
          </div>
          <p class="graph-help">
            {opts?.helpText ?? "Nodes are papers. Click a node to inspect the summary and related signals."}
          </p>
        </div>
        <div class="paper-graph-layout">
          <div class="paper-graph-canvas" data-paper-graph-canvas></div>
          {!opts?.linkOnly && (
            <aside class="paper-graph-panel" data-paper-graph-panel>
              <p class="panel-eyebrow">Select a paper</p>
              <h3>Paper summary panel</h3>
              <p>Click a circle in the graph to view the paper title, summary, metadata, and relationship signals.</p>
            </aside>
          )}
        </div>
      </section>
    )
  }

  PaperGraph.css = style
  PaperGraph.afterDOMLoaded = script
  return PaperGraph
}) satisfies QuartzComponentConstructor<Partial<PaperGraphOptions>>
