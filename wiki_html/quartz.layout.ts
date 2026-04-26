import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      Home: "/",
      Sources: "/sources",
      Concepts: "/concepts",
      Analyses: "/analyses",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs({ rootName: "Atlas" }),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ConditionalRender({
      component: Component.HomeAtlas(),
      condition: (page) => page.fileData.slug === "index",
    }),
    Component.ConditionalRender({
      component: Component.ArticleTitle(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ConditionalRender({
      component: Component.ContentMeta(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ConditionalRender({
      component: Component.TagList(),
      condition: (page) => page.fileData.slug !== "index",
    }),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({
      title: "Browse",
      folderDefaultState: "open",
      useSavedState: true,
    }),
  ],
  right: [
    Component.Graph({
      localGraph: {
        drag: true,
        zoom: true,
        depth: 1,
        scale: 1.2,
        repelForce: 0.5,
        centerForce: 0.5,
        linkDistance: 30,
        fontSize: 0.6,
        opacityScale: 1,
        showTags: false,
        focusOnHover: true,
        removeTags: ["pmid"],
      },
      globalGraph: {
        drag: true,
        zoom: true,
        depth: -1,
        scale: 1.0,
        repelForce: 1.0,
        centerForce: 0.2,
        linkDistance: 50,
        fontSize: 0.6,
        opacityScale: 1,
        showTags: false,
        focusOnHover: true,
        removeTags: [],
      },
    }),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.RecentNotes({
      title: "Recently Updated",
      limit: 6,
      showTags: false,
      linkToMore: false,
      filter: (page) => page.slug !== "index" && !page.slug?.startsWith("tags/"),
    }),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs({ rootName: "Atlas" }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({
      title: "Browse",
      folderDefaultState: "open",
      useSavedState: true,
    }),
  ],
  right: [
    Component.Graph({
      localGraph: {
        drag: true,
        zoom: true,
        depth: 1,
        scale: 1.2,
        repelForce: 0.5,
        centerForce: 0.5,
        linkDistance: 30,
        fontSize: 0.6,
        opacityScale: 1,
        showTags: false,
        focusOnHover: true,
        removeTags: ["pmid"],
      },
      globalGraph: {
        drag: true,
        zoom: true,
        depth: -1,
        scale: 1.0,
        repelForce: 1.0,
        centerForce: 0.2,
        linkDistance: 50,
        fontSize: 0.6,
        opacityScale: 1,
        showTags: false,
        focusOnHover: true,
        removeTags: [],
      },
    }),
    Component.RecentNotes({
      title: "Recent Additions",
      limit: 6,
      showTags: false,
      linkToMore: false,
      filter: (page) => page.slug !== "index" && !page.slug?.startsWith("tags/"),
    }),
  ],
}
