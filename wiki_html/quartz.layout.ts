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
    Component.TopicQuickNav(),
    Component.Backlinks(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.RecentNotes({
      title: "Recently Updated",
      limit: 6,
      showTags: false,
      linkToMore: false,
      filter: (page) => page.slug !== "index" && !page.slug?.startsWith("tags/"),
    }),
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
    Component.TopicQuickNav(),
    Component.RecentNotes({
      title: "Recent Additions",
      limit: 6,
      showTags: false,
      linkToMore: false,
      filter: (page) => page.slug !== "index" && !page.slug?.startsWith("tags/"),
    }),
  ],
}
