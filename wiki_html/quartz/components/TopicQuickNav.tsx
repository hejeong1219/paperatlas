import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { resolveRelative } from "../util/path"
// @ts-ignore
import style from "./styles/topicQuickNav.scss"

const TOPICS = [
  {
    id: "bcell-neoantigen",
    label: "B-Cell Neoantigen",
    color: "#4ecdc4",
    path: "topics/b-cell-neoantigen-human-cancer",
    description: "B-cell, TLS, and neoantigen biology",
  },
  {
    id: "cancer-multiomics-literature",
    label: "Cancer Multiomics Atlas",
    color: "#176087",
    path: "topics/cancer-multiomics-literature",
    description: "Proteogenomic and phosphoproteomic integration",
  },
  {
    id: "resistance",
    label: "Cancer Resistance",
    color: "#ff6b6b",
    path: "topics/immunotherapy-resistance-and-immune-evasion",
    description: "Immune evasion and therapeutic resistance",
  },
  {
    id: "multiomics-proteomics-ptm-identification",
    label: "PTM Identification",
    color: "#6c8f6b",
    path: "topics/multiomics-proteomics-ptm-identification",
    description: "Proteome, phosphoproteome, and acetylome depth",
  },
  {
    id: "ptmanchor",
    label: "PTM Signaling",
    color: "#b76e79",
    path: "topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics",
    description: "PTM-aware kinase-state interpretation",
  },
]

export default (() => {
  const TopicQuickNav: QuartzComponent = ({ fileData, allFiles }: QuartzComponentProps) => {
    const counts: Record<string, number> = {}
    for (const page of allFiles) {
      const slug = page.slug ?? ""
      if (!slug.startsWith("sources/") || slug === "sources/index") continue
      const fm = page.frontmatter as Record<string, unknown> | undefined
      const primary = fm?.topic as string | undefined
      const extras = Array.isArray(fm?.extra_topics) ? (fm.extra_topics as string[]) : []
      const ids = [primary, ...extras].filter((x): x is string => Boolean(x))
      for (const id of ids) {
        counts[id] = (counts[id] || 0) + 1
      }
    }
    return (
      <div class="topic-quick-nav">
        <h3>Topics</h3>
        <ul class="quick-nav-list">
          {TOPICS.map((t) => (
            <li class="quick-nav-item">
              <a
                href={resolveRelative(fileData.slug!, t.path as any)}
                class="quick-nav-card"
                style={{ borderLeftColor: t.color } as any}
              >
                <span class="quick-nav-dot" style={{ backgroundColor: t.color } as any}></span>
                <div class="quick-nav-text">
                  <strong class="quick-nav-label">{t.label}</strong>
                  <span class="quick-nav-desc">{t.description}</span>
                </div>
                <span class="quick-nav-count">{counts[t.id] ?? 0}</span>
              </a>
            </li>
          ))}
        </ul>
      </div>
    )
  }
  TopicQuickNav.css = style
  return TopicQuickNav
}) satisfies QuartzComponentConstructor
