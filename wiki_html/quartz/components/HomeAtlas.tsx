import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { resolveRelative } from "../util/path"
import style from "./styles/homeAtlas.scss"
import { byDateAndAlphabetical } from "./PageList"
import PaperGraph from "./PaperGraph"
import { concatenateResources } from "../util/resources"

const HomeMainGraph = PaperGraph({
  title: "Paper Network",
  eyebrow: "Research Graph",
  helpText: "Each node is a paper, colored by topic. Drag, scroll-zoom, click to open the paper.",
  linkOnly: true,
})

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

const browseSections = [
  {
    title: "Topics",
    href: "topics",
    description: "Curated topic collections that organize papers, concepts, and analyses around a question.",
  },
  {
    title: "Papers",
    href: "sources",
    description: "Paper-level notes with metadata, summaries, filters, and the paper connectivity graph.",
  },
  {
    title: "Concepts",
    href: "concepts",
    description: "Reusable concept pages that stay stable even as the corpus grows across topics.",
  },
  {
    title: "Analyses",
    href: "analyses",
    description: "Cross-paper syntheses that compare methods, evidence chains, and open tensions.",
  },
]

const currentTracks = [
  "Start from a topic collection when you are learning a new area.",
  "Drop into paper pages when you need study-level evidence and metadata.",
  "Use concepts and analyses to move from isolated papers to a reusable knowledge model.",
]

const anchorSlugs = [
  "analyses/b-cell-neoantigen-proposal-anchor",
  "analyses/cancer-resistance-manuscript-anchor",
  "analyses/ptmanchor-manuscript-anchor",
]

const topicSlugToId: Record<string, string> = {
  "topics/b-cell-neoantigen-human-cancer": "bcell-neoantigen",
  "topics/immunotherapy-resistance-and-immune-evasion": "resistance",
  "topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics": "ptmanchor",
}

export default (() => {
  const HomeAtlas: QuartzComponent = ({ fileData, allFiles, cfg }: QuartzComponentProps) => {
    const sourcePages = allFiles.filter((page) => page.slug?.startsWith("sources/") && page.slug !== "sources/index")

    const featuredPapers = sourcePages
      .filter((page) => page.slug?.startsWith("sources/") && page.slug !== "sources/index")
      .sort(byDateAndAlphabetical(cfg))
      .slice(0, 6)

    const featuredTopics = allFiles
      .filter((page) => page.slug?.startsWith("topics/") && page.slug !== "topics/index")
      .sort(byDateAndAlphabetical(cfg))
      .slice(0, 4)

    const anchorPages = anchorSlugs
      .map((slug) => allFiles.find((page) => page.slug === slug))
      .filter((page): page is NonNullable<(typeof allFiles)[number]> => Boolean(page))

    const topicCount = allFiles.filter((page) => page.slug?.startsWith("topics/") && page.slug !== "topics/index").length
    const conceptCount = allFiles.filter((page) => page.slug?.startsWith("concepts/") && page.slug !== "concepts/index").length
    const analysisCount = allFiles.filter((page) => page.slug?.startsWith("analyses/") && page.slug !== "analyses/index").length

    const featuredThemes = [...new Set(featuredPapers.flatMap((page) => asList(page.frontmatter?.themes)))]
      .slice(0, 8)

    const topicCounts: Record<string, number> = {}
    for (const page of sourcePages) {
      const primary = page.frontmatter?.topic as string | undefined
      const extras = asList(page.frontmatter?.extra_topics)
      const ids = [primary, ...extras].filter((x): x is string => Boolean(x))
      for (const id of ids) {
        topicCounts[id] = (topicCounts[id] || 0) + 1
      }
    }

    return (
      <section class="home-atlas">
        <div class="hero">
          <p class="eyebrow">Paper Atlas</p>
          <h1>Paper Atlas</h1>
          <p class="lede">
            A paper-first knowledge system for building reusable topic maps from literature,
            instead of keeping notes as isolated PDFs, summaries, or journal lists.
          </p>
          <div class="hero-actions">
            <a class="primary" href={resolveRelative(fileData.slug!, "topics")}>
              Browse Topics
            </a>
            <a class="secondary" href={resolveRelative(fileData.slug!, "sources")}>
              Explore Papers
            </a>
          </div>
          <div class="hero-stats">
            <div class="stat-pill">
              <strong>{sourcePages.length}</strong>
              <span>Papers</span>
            </div>
            <div class="stat-pill">
              <strong>{topicCount}</strong>
              <span>Topics</span>
            </div>
            <div class="stat-pill">
              <strong>{conceptCount}</strong>
              <span>Concepts</span>
            </div>
            <div class="stat-pill">
              <strong>{analysisCount}</strong>
              <span>Analyses</span>
            </div>
          </div>
        </div>

        <div class="browse-grid">
          {browseSections.map((section) => (
            <article class="browse-card">
              <h3>
                <a href={resolveRelative(fileData.slug!, section.href)}>{section.title}</a>
              </h3>
              <p>{section.description}</p>
            </article>
          ))}
        </div>

        <section class="panel graph-main-panel">
          <HomeMainGraph fileData={fileData} allFiles={allFiles} cfg={cfg} />
        </section>

        <div class="dashboard-grid">
          <section class="panel wide">
            <div class="panel-header">
              <h2>Current Topic Collections</h2>
              <a href={resolveRelative(fileData.slug!, "topics")}>View all topics</a>
            </div>
            <div class="featured-grid">
              {featuredTopics.map((page) => {
                const topicId = page.slug ? topicSlugToId[page.slug] : undefined
                const paperCount = topicId ? topicCounts[topicId] || 0 : 0
                return (
                <article class="featured-card">
                  <p class="meta">
                    {(asList(page.frontmatter?.tags)
                      .slice(0, 2)
                      .map((tag) => labelize(tag))
                      .join(" · ") || "Topic Collection") + (paperCount > 0 ? ` · ${paperCount} papers` : "")}
                  </p>
                  <h3>
                    <a href={resolveRelative(fileData.slug!, page.slug!)} class="internal">
                      {page.frontmatter?.title}
                    </a>
                  </h3>
                  <p class="summary">{page.description}</p>
                  <div class="chip-row">
                    {asList(page.frontmatter?.themes)
                      .slice(0, 3)
                      .map((value) => (
                        <span class="chip">{labelize(value)}</span>
                      ))}
                    {asList(page.frontmatter?.tags)
                      .slice(0, 2)
                      .map((value) => (
                        <span class="chip subtle">{labelize(value)}</span>
                      ))}
                  </div>
                </article>
                )
              })}
            </div>
          </section>

          <section class="panel">
            <div class="panel-header">
              <h2>Active Project Anchors</h2>
              <a href={resolveRelative(fileData.slug!, "analyses")}>View all analyses</a>
            </div>
            <div class="anchor-grid">
              {anchorPages.map((page) => (
                <article class="anchor-card">
                  <p class="meta">
                    {asList(page.frontmatter?.tags)
                      .slice(0, 2)
                      .map((tag) => labelize(tag))
                      .join(" · ") || "Project Anchor"}
                  </p>
                  <h3>
                    <a href={resolveRelative(fileData.slug!, page.slug!)} class="internal">
                      {page.frontmatter?.title}
                    </a>
                  </h3>
                  <p class="summary">{page.description}</p>
                  <div class="chip-row">
                    {asList(page.frontmatter?.themes)
                      .slice(0, 3)
                      .map((value) => (
                        <span class="chip subtle">{labelize(value)}</span>
                      ))}
                  </div>
                </article>
              ))}
            </div>
          </section>

          <section class="panel">
            <div class="panel-header">
              <h2>How To Use The Atlas</h2>
            </div>
            <ul class="track-list">
              {currentTracks.map((track) => (
                <li>{track}</li>
              ))}
            </ul>
          </section>

          <section class="panel">
            <div class="panel-header">
              <h2>Research Themes</h2>
            </div>
            <div class="chip-cloud">
              {featuredThemes.slice(0, 5).map((theme) => (
                <a class="chip" href={resolveRelative(fileData.slug!, `tags/${theme}`)}>
                  {labelize(theme)}
                </a>
              ))}
            </div>
          </section>
        </div>
      </section>
    )
  }

  HomeAtlas.css = concatenateResources(style, HomeMainGraph.css)
  HomeAtlas.afterDOMLoaded = HomeMainGraph.afterDOMLoaded
  return HomeAtlas
}) satisfies QuartzComponentConstructor
