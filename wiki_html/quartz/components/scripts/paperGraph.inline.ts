import {
  forceCenter,
  forceLink,
  forceManyBody,
  forceCollide,
  forceSimulation,
  forceX,
  forceY,
  drag,
  select,
  zoom,
} from "d3"

type NodeDatum = {
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
  href: string
  x?: number
  y?: number
  vx?: number
  vy?: number
  fx?: number | null
  fy?: number | null
}

const TOPIC_COLORS: Record<string, string> = {
  ptmanchor: "#7b5cff",       // purple
  resistance: "#ff6b6b",      // coral
  "bcell-neoantigen": "#4ecdc4", // teal
  other: "#9aa5b1",
}

type LinkDatum = {
  source: string | NodeDatum
  target: string | NodeDatum
  weight: number
  reasons: string[]
}

function labelize(value: string) {
  return value
    .split("-")
    .map((part) => (part ? part[0].toUpperCase() + part.slice(1) : part))
    .join(" ")
}

function shorten(text: string, limit: number) {
  return text.length > limit ? `${text.slice(0, limit).trim()}…` : text
}

function renderPanel(panel: HTMLElement, node: NodeDatum, related: LinkDatum[], compact: boolean) {
  const chips = [
    ...node.cancers.map((item) => `<span class="chip">${labelize(item)}</span>`),
    ...node.modalities.map((item) => `<span class="chip subtle">${labelize(item)}</span>`),
  ].join("")

  const connections = related
    .slice(0, compact ? 3 : 6)
    .map((link) => {
      const other = (link.source as NodeDatum).id === node.id ? (link.target as NodeDatum) : (link.source as NodeDatum)
      return `
        <li>
          <strong>${shorten(other.title, compact ? 58 : 120)}</strong>
          <span>${shorten(link.reasons.join(" · "), compact ? 88 : 180)}</span>
        </li>
      `
    })
    .join("")

  panel.innerHTML = `
    <p class="panel-eyebrow">${[node.year, node.journal].filter(Boolean).join(" · ") || "Paper"}</p>
    <h3 class="panel-title">${shorten(node.title, compact ? 88 : 220)}</h3>
    <p class="panel-summary">${shorten(node.summary, compact ? 180 : 420)}</p>
    <div class="panel-chip-row">${chips}</div>
    <p><a class="panel-link" href="${node.href}">Open paper page</a></p>
    <div class="panel-section">
      <h4>Connections</h4>
      <ul class="connection-list">${connections || "<li><span>No linked neighbors yet.</span></li>"}</ul>
    </div>
  `
}

function initPaperGraphs() {
  document.querySelectorAll<HTMLElement>("[data-paper-graph]").forEach((root) => {
    const canvas = root.querySelector<HTMLElement>("[data-paper-graph-canvas]")
    const panel = root.querySelector<HTMLElement>("[data-paper-graph-panel]")
    if (!canvas) return

    const graph = JSON.parse(root.dataset.graph || '{"nodes":[],"links":[]}') as {
      nodes: NodeDatum[]
      links: LinkDatum[]
    }

    canvas.innerHTML = ""
    const compact = root.classList.contains("compact")
    const linkOnly = root.dataset.linkOnly === "true"
    const width = canvas.clientWidth || 640
    const height = compact ? 360 : 520

    const svg = select(canvas).append("svg").attr("viewBox", `0 0 ${width} ${height}`)
    const zoomLayer = svg.append("g").attr("class", "zoom-layer")
    const linkLayer = zoomLayer.append("g").attr("class", "links")
    const nodeLayer = zoomLayer.append("g").attr("class", "nodes")
    const labelLayer = zoomLayer.append("g").attr("class", "labels")

    const simulation = forceSimulation<NodeDatum>(graph.nodes)
      .force(
        "link",
        forceLink<NodeDatum, LinkDatum>(graph.links)
          .id((d) => d.id)
          .distance((d) => 50 + Math.max(0, 10 - d.weight) * 6),
      )
      .force("charge", forceManyBody().strength(compact ? -160 : -220))
      .force("collide", forceCollide<NodeDatum>().radius((d) => (compact ? 14 : 18)).iterations(2))
      .force("x", forceX<NodeDatum>((d) => {
        if (d.topic === "ptmanchor") return width * 0.22
        if (d.topic === "resistance") return width * 0.5
        if (d.topic === "bcell-neoantigen") return width * 0.78
        return width * 0.5
      }).strength(0.18))
      .force("y", forceY<NodeDatum>(height / 2).strength(0.06))
      .alphaDecay(0.05)
      .alphaMin(0.02)
      .velocityDecay(0.6)

    // wheel-zoom + pan-by-drag-on-empty
    const zoomBehavior = zoom<SVGSVGElement, unknown>()
      .scaleExtent([0.25, 4])
      .filter((event) => {
        // allow wheel for zoom; allow background drag (not on a node) for pan
        if (event.type === "wheel") return true
        if (event.type === "mousedown" || event.type === "touchstart") {
          return !(event.target as Element).closest("circle")
        }
        return !event.button
      })
      .on("zoom", (event) => {
        zoomLayer.attr("transform", event.transform.toString())
      })
    svg.call(zoomBehavior as any)

    const links = linkLayer
      .selectAll("line")
      .data(graph.links)
      .enter()
      .append("line")
      .attr("stroke", "var(--gray)")
      .attr("stroke-opacity", 0.45)
      .attr("stroke-width", (d) => Math.min(4, 1 + d.weight * 0.35))

    const nodes = nodeLayer
      .selectAll("circle")
      .data(graph.nodes)
      .enter()
      .append("circle")
      .attr("r", (d) => (compact ? 8 : 10) + Math.min(compact ? 5 : 8, d.modalities.length + d.cancers.length))
      .attr("fill", (d) => TOPIC_COLORS[d.topic] ?? TOPIC_COLORS.other)
      .attr("stroke", "var(--light)")
      .attr("stroke-width", 2)
      .style("cursor", "pointer")

    const labels = labelLayer
      .selectAll("text")
      .data(graph.nodes)
      .enter()
      .append("text")
      .attr("font-size", compact ? 10 : 11)
      .attr("fill", "var(--dark)")
      .attr("text-anchor", "middle")
      .text((d) => {
        const limit = compact ? 24 : 34
        return d.title.length > limit ? `${d.title.slice(0, limit)}…` : d.title
      })

    const dragBehavior = drag<SVGCircleElement, NodeDatum>()
      .on("start", (event, d) => {
        if (!event.active) simulation.alphaTarget(0.2).restart()
        d.fx = d.x
        d.fy = d.y
      })
      .on("drag", (event, d) => {
        d.fx = event.x
        d.fy = event.y
      })
      .on("end", (event, d) => {
        if (!event.active) simulation.alphaTarget(0)
        d.fx = null
        d.fy = null
      })

    nodes.call(dragBehavior as any)

    let selectedId = graph.nodes[0]?.id

    const updateSelection = (id?: string) => {
      if (linkOnly) return
      if (!id) return
      selectedId = id
      nodes.attr("fill", (d) => (d.id === selectedId ? "var(--tertiary)" : (TOPIC_COLORS[d.topic] ?? TOPIC_COLORS.other)))
      links.attr("stroke-opacity", (d) =>
        (d.source as NodeDatum).id === selectedId || (d.target as NodeDatum).id === selectedId ? 0.9 : 0.18,
      )

      const node = graph.nodes.find((item) => item.id === selectedId)
      if (!node || !panel) return
      const related = graph.links.filter(
        (link) => (link.source as NodeDatum).id === selectedId || (link.target as NodeDatum).id === selectedId,
      )
      renderPanel(panel, node, related, compact)
    }

    if (linkOnly) {
      nodes.on("click", (_, d) => {
        window.location.href = d.href
      })
      labels.on("click", (_, d) => {
        window.location.href = d.href
      }).style("cursor", "pointer")
      nodes.attr("fill", (d) => TOPIC_COLORS[d.topic] ?? TOPIC_COLORS.other)
      links.attr("stroke-opacity", 0.35)
    } else {
      nodes.on("click", (_, d) => updateSelection(d.id))
      labels.on("click", (_, d) => updateSelection(d.id)).style("cursor", "pointer")
    }

    simulation.on("tick", () => {
      links
        .attr("x1", (d) => (d.source as NodeDatum).x || 0)
        .attr("y1", (d) => (d.source as NodeDatum).y || 0)
        .attr("x2", (d) => (d.target as NodeDatum).x || 0)
        .attr("y2", (d) => (d.target as NodeDatum).y || 0)

      nodes.attr("cx", (d) => d.x || 0).attr("cy", (d) => d.y || 0)

      labels
        .attr("x", (d) => d.x || 0)
        .attr("y", (d) => (d.y || 0) - 16)
    })

    if (!linkOnly) {
      updateSelection(selectedId)
    }
  })
}

document.addEventListener("nav", initPaperGraphs)
document.addEventListener("DOMContentLoaded", initPaperGraphs)
