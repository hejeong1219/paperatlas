import { QuartzComponentProps } from "./types"
import { QuartzPluginData } from "../plugins/vfile"
import { resolveRelative } from "../util/path"
import style from "./styles/atlasCards.scss"

type AtlasMode = "papers" | "collections"

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
    .map((part) => (part.length > 0 ? part[0].toUpperCase() + part.slice(1) : part))
    .join(" ")
}

function descriptionFor(page: QuartzPluginData): string {
  const description = page.description
  if (typeof description === "string" && description.trim().length > 0) {
    return description.trim()
  }

  return "No description available yet."
}

export function renderAtlasCards(
  props: QuartzComponentProps,
  pages: QuartzPluginData[],
  mode: AtlasMode,
) {
  const { fileData } = props
  const isPaperMode = mode === "papers"

  const journals = [...new Set(pages.flatMap((page) => asList(page.frontmatter?.journal)))].sort()
  const cancers = [...new Set(pages.flatMap((page) => asList(page.frontmatter?.cancer_types)))].sort()
  const modalities = [...new Set(pages.flatMap((page) => asList(page.frontmatter?.modalities)))].sort()
  const kinds = [...new Set(pages.flatMap((page) => asList(page.frontmatter?.paper_kind)))].sort()

  return (
    <div class="atlas-cards">
      {isPaperMode && (
        <div class="atlas-filters" data-atlas-filters>
          <div class="atlas-filter-row">
            <label>
              <span>Journal</span>
              <select data-filter-key="journal">
                <option value="">All</option>
                {journals.map((journal) => (
                  <option value={journal}>{journal}</option>
                ))}
              </select>
            </label>
            <label>
              <span>Cancer</span>
              <select data-filter-key="cancer">
                <option value="">All</option>
                {cancers.map((cancer) => (
                  <option value={cancer}>{labelize(cancer)}</option>
                ))}
              </select>
            </label>
            <label>
              <span>Modality</span>
              <select data-filter-key="modality">
                <option value="">All</option>
                {modalities.map((modality) => (
                  <option value={modality}>{labelize(modality)}</option>
                ))}
              </select>
            </label>
            <label>
              <span>Kind</span>
              <select data-filter-key="kind">
                <option value="">All</option>
                {kinds.map((kind) => (
                  <option value={kind}>{labelize(kind)}</option>
                ))}
              </select>
            </label>
            <button type="button" class="atlas-reset" data-atlas-reset>
              Reset
            </button>
          </div>
          <p class="atlas-count" data-atlas-count>
            Showing {pages.length} papers
          </p>
        </div>
      )}
      <div class={`atlas-grid ${isPaperMode ? "papers" : "collections"}`} data-atlas-grid>
        {pages.map((page) => {
          const title = page.frontmatter?.title ?? "Untitled"
          const year = page.frontmatter?.year
          const journal = page.frontmatter?.journal
          const authors = asList(page.frontmatter?.authors)
          const cancerTypes = asList(page.frontmatter?.cancer_types)
          const pageModalities = asList(page.frontmatter?.modalities)
          const paperKind = page.frontmatter?.paper_kind
          const themes = asList(page.frontmatter?.themes)

          return (
            <article
              class="atlas-card"
              data-journal={typeof journal === "string" ? journal : ""}
              data-cancers={cancerTypes.join("|")}
              data-modalities={pageModalities.join("|")}
              data-kind={typeof paperKind === "string" ? paperKind : ""}
            >
              <div class="atlas-card-header">
                <p class="atlas-card-eyebrow">
                  {[year, journal].filter(Boolean).join(" · ") || "Curated entry"}
                </p>
                <h3>
                  <a href={resolveRelative(fileData.slug!, page.slug!)} class="internal">
                    {title}
                  </a>
                </h3>
              </div>
              {authors.length > 0 && <p class="atlas-card-authors">{authors.join(", ")}</p>}
              <p class="atlas-card-summary">{descriptionFor(page)}</p>
              <div class="atlas-chip-group">
                {cancerTypes.map((value) => (
                  <span class="atlas-chip">{labelize(value)}</span>
                ))}
                {pageModalities.slice(0, 3).map((value) => (
                  <span class="atlas-chip subtle">{labelize(value)}</span>
                ))}
                {typeof paperKind === "string" && <span class="atlas-badge">{labelize(paperKind)}</span>}
              </div>
              {!isPaperMode && themes.length > 0 && (
                <div class="atlas-chip-group">
                  {themes.slice(0, 3).map((value) => (
                    <span class="atlas-chip subtle">{labelize(value)}</span>
                  ))}
                </div>
              )}
            </article>
          )
        })}
      </div>
    </div>
  )
}

export const atlasCardsScript = `
document.addEventListener("nav", () => {
  document.querySelectorAll("[data-atlas-filters]").forEach((filtersRoot) => {
    const container = filtersRoot.closest(".atlas-cards")
    if (!container) return
    const cards = Array.from(container.querySelectorAll(".atlas-card"))
    const selects = Array.from(filtersRoot.querySelectorAll("select[data-filter-key]"))
    const count = filtersRoot.querySelector("[data-atlas-count]")
    const reset = filtersRoot.querySelector("[data-atlas-reset]")

    const apply = () => {
      let visible = 0
      cards.forEach((card) => {
        const journal = card.getAttribute("data-journal") || ""
        const cancers = (card.getAttribute("data-cancers") || "").split("|").filter(Boolean)
        const modalities = (card.getAttribute("data-modalities") || "").split("|").filter(Boolean)
        const kind = card.getAttribute("data-kind") || ""

        const active = Object.fromEntries(
          selects.map((select) => [select.getAttribute("data-filter-key"), select.value]),
        )

        const matches =
          (!active.journal || active.journal === journal) &&
          (!active.cancer || cancers.includes(active.cancer)) &&
          (!active.modality || modalities.includes(active.modality)) &&
          (!active.kind || active.kind === kind)

        card.toggleAttribute("hidden", !matches)
        if (matches) visible += 1
      })

      if (count) count.textContent = "Showing " + visible + " papers"
    }

    selects.forEach((select) => select.addEventListener("change", apply))
    reset?.addEventListener("click", () => {
      selects.forEach((select) => {
        select.value = ""
      })
      apply()
    })

    apply()
  })
})
`

export const atlasCardsCss = style
