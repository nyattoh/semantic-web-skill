# Page metadata and structured data

Use this reference when creating or reviewing a page description, page icons, Open Graph, X cards or JSON-LD. These are draft requirements for agent work, not implemented audit rules.

## Device-dependent page icons

Before choosing or generating icon assets, research the requested display contexts and OS/browser versions using current primary sources: the HTML and Web Application Manifest standards and the relevant platform/browser vendor documentation. Record each source URL, retrieval date, applicable version/context, required or recommended formats/sizes, selection and cropping rules, and unresolved differences. Distinguish current documentation from archived guidance. If a target version is unspecified, record the assumed targets and unverified coverage; do not silently claim all devices. If current sources are unavailable, preserve the dated evidence and identify the dependent choice as `needs_review`.

The sizes and filenames below are a starting example, not a fixed universal icon bundle. Select the delivered set from that research and the requested scope, then verify the actual generated assets and target behaviour. Cached icons, browser candidate selection and OS cropping can produce different results despite identical HTML; investigate those causes on the named target before changing files or claiming coverage.

Treat browser-tab/bookmark favicons, iOS/iPadOS Home Screen (Web Clip) icons, web-manifest application icons and Safari pinned-tab icons as distinct contexts. Include only the contexts in the requested scope; a web manifest or PWA setup is not a universal favicon requirement.

For a cross-browser favicon set, provide a scalable SVG favicon (`rel="icon"`, `type="image/svg+xml"`, `sizes="any"`) and an ICO fallback named `favicon.ico` containing 16x16, 32x32 and 48x48 raster entries. The HTML standard lets user agents choose among icon candidates using `type`, `media` and `sizes`; format support and selection still vary. Check the SVG at small sizes and ensure it has visible contrast in both light and dark browser chrome. Either use one SVG with an opaque, contrasting tile that remains distinct against both light and dark surroundings, or provide light/dark SVG candidates using `media="(prefers-color-scheme: light)"` and `media="(prefers-color-scheme: dark)"`. Do not assume every browser will honour an embedded SVG colour-scheme rule. Keep the ICO fallback available when SVG favicons are unsupported.

When iOS/iPadOS Home Screen appearance is in scope, provide a separate 180x180 PNG referenced with `rel="apple-touch-icon"`. Do not assume this link is used by Android, desktop browsers or every user agent; check target devices if exact Home Screen rendering matters.

When app-launcher identity is in scope, a web manifest may provide 192x192 and 512x512 PNG icons. Give these full-colour icons explicit `purpose: "any"`. Current Chromium installability guidance includes both sizes, but icon sizes alone do not make a site installable and are not a universal web-page favicon requirement. Keep manifest `id`, `start_url` and `scope` aligned with the deployment base path when that path is the intended app identity. For a site deployed under `/semantic/`, use a manifest URL under that path and verify the final URLs of its app identity, start URL, scope and icon paths. Both root-relative and relative references can be correct, depending on the base used. In particular, manifest `id` is resolved against the origin of `start_url`, while `start_url`, `scope` and icon paths use manifest URL resolution. Thus `id: "./"` can resolve to the origin root even when the manifest and start URL are under `/semantic/`; use an explicitly correct identity such as `/semantic/` and inspect the resolved value. The manifest standard does not require `id` to be within `scope`; choose an identity path intentionally rather than treating this relationship as a universal rule. Confirm resolved values from the served manifest, not only from a source template. The `/semantic/` example below is specific to this deployment; do not require that path for other sites.

For the `/semantic/` deployment, the expected relationship is:

```html
<link rel="manifest" href="/semantic/site.webmanifest">
```

```json
{
  "id": "/semantic/",
  "start_url": "/semantic/",
  "scope": "/semantic/",
  "icons": [
    { "src": "/semantic/assets/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any" },
    { "src": "/semantic/assets/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any" }
  ]
}
```

Treat filenames above as an example mapping: verify that referenced assets exist and that the delivered manifest resolves to the intended base path.

If a maskable app icon is requested, make it a separate 512x512 PNG with an opaque background and `purpose: "maskable"`; do not mark a conventional `any` icon as maskable unless its artwork is designed for cropping. Keep essential artwork inside the central safe circle whose diameter is 80% of the icon's minimum dimension. Check the image in a mask preview and retain the regular `any` icon for contexts that do not apply a mask.

Safari pinned-tab `mask-icon` is an optional Safari-specific asset. It is monochrome artwork with a single selected colour, so it is not a substitute for a full-colour favicon or a universal cross-browser feature. Include it only when Safari pinned tabs are in scope.

An icon or manifest alone does not establish an installable PWA, offline behaviour, or successful installation. Do not claim any of these without separately checking the current platform criteria and the actual behaviour. Separate local asset validation (existence, decode, dimensions and ICO entries), manifest parsing/path resolution, desktop browser preview, emulation, and real-device testing. Local decode or dimensions checks do not establish browser selection or Home Screen rendering. Report device/browser combinations not exercised as `not run`, naming the missing environment; do not imply device coverage from a screenshot or local browser.

## Establish content and URL evidence

Record the page purpose, visible content, language/locale, existing metadata, image asset, intended public page URL, whether that identity is owner-confirmed or verified live, and authorised scope. A public repository URL does not establish the deployment URL of a separate site.

Give each page a distinct, truthful `title` and `meta name="description"` that reflect its visible content and current product status. Identify duplicate titles or descriptions across the supplied page set; if only one page is supplied, mark site-wide uniqueness unverified. Do not add outcomes, reviews, credentials or availability claims absent from the page.

Emit `link rel="canonical"`, `og:url` and `og:image` only when the intended public deployment identity and relevant asset path are confirmed, including by the owner before publication. This allows pre-deployment metadata without requiring publication. Require absolute HTTP(S) URLs; do not resolve a relative value against localhost and call it a public URL. Confirm the page identity before aligning canonical and `og:url`; never substitute the project repository for the page itself. Label owner-confirmed future URLs as planned; live HTTPS, crawler accessibility and platform previews are separate checks and remain not run until actually verified.

If the deployment URL is unknown, omit these URL-dependent fields from the local output and report `needs_review`, naming the missing URL and the fields withheld. Do not ship fabricated domains, template variables, example URLs or blank URL tags. This leaves Open Graph incomplete for public sharing; do not describe it as fully validated. Apply the same evidence boundary to X images and JSON-LD page/asset identities.

## Head metadata

- Open Graph: supply truthful `og:title`, `og:description`, an appropriate `og:type` and `og:locale`. Use `website` for an ordinary promotional landing page; do not label it an article merely to improve discovery. Open Graph locales use language and territory, such as `ja_JP` or `en_GB`; choose from the actual page, not the operator's location. Add the confirmed URL/image fields under the gate above. Describe the real image in `og:image:alt`; add MIME type and dimensions only when checked against the actual file.
- X cards: emit explicit `twitter:card`, `twitter:title` and `twitter:description`. The API/tag identifiers retain their official spelling. Select the card type for the actual content; a checked image and owner-confirmed planned absolute URL permit pre-deployment image metadata. Do not claim live large-image readiness without checking current provider requirements and public image access. Add `twitter:image` and `twitter:image:alt` only for the confirmed image/target. Omit unverified `twitter:site` or `twitter:creator` accounts. A local head check does not establish a platform preview.
- Inspect source and browser-parsed `head` for duplicate or conflicting tags, escaping errors and unintended empty values. Compare title and descriptions with rendered headings, body and visible limitations. Metadata cannot remedy misleading page copy.

## JSON-LD

Use `script type="application/ld+json"` with valid JSON and `@context: "https://schema.org"`. Choose a type supported by the actual page content; a promotional demo can use `WebPage`, with a truthful `name`, `description` and `inLanguage`. Omit unknown `url`, `@id` and image URLs until confirmed. The schema context URL identifies the vocabulary and is not a fabricated deployment URL.

Do not invent reviews, ratings, star counts, FAQs, publisher credentials or organisation identity. Add `FAQPage`, `Organization` (official schema identifier), other entities or rich-result-specific properties only when the visible content and evidence warrant them. A generic `WebPage` is not proof of a supported Google rich-result feature. Structured data supplements semantic HTML; retain meaningful headings, landmarks, links and controls.

Parse each emitted JSON-LD block with a JSON parser. Check its schema types/properties and match every factual value to visible content or an identified source. Parseability alone does not establish semantic correctness or eligibility.

## Verification and output

Report each item as checked, failed, not run or `needs_review`, with the evidence and remaining condition:

1. Source map: connect title, description, OG/X values and JSON-LD facts to the page content or supplied source.
2. Delivered head: inspect the emitted HTML and browser-parsed DOM on the actual local/runtime route, not only a template. Record extracted values and duplicate/conflict findings. If runtime access is unavailable, report it as not run.
3. Images: check file existence, decode success, actual size/type and descriptive alternatives. A confirmed deployment target and asset path can establish a planned absolute image URL before publication. Check live HTTPS and public crawler access separately when within authorised scope; a local image loading does not prove either.
4. URLs: record owner-confirmed planned or verified-live canonical, `og:url` and asset URLs, or the unresolved public URL and withheld fields. Check absolute URLs and page identity. Do not call a planned URL live or publish merely to complete these checks.
5. JSON-LD: record JSON parsing, vocabulary/type review and visible-content consistency separately. Use current provider validation for an applicable rich-result feature only when within scope; never report unsupported WebPage-only markup as a failed rich-result implementation.
6. Preview: record any actual provider preview separately from local parsing. Do not upload private/local material or publish a site solely to obtain a preview without authorisation.

No metadata, schema validation or preview guarantees ranking, search inclusion, rich-result display, AI citation or platform presentation.

## Primary references

Checked on 2026-10-09 (JST):

- [Open Graph protocol](https://ogp.me/): field definitions, object types, locales and image properties. It specifies title, type, image and URL as the basic four properties; an unresolved public URL therefore prevents a complete public OG object.
- [Schema.org WebPage](https://schema.org/WebPage): vocabulary for a page and its properties; not a Google feature eligibility contract.
- [Google general structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies): truthful visible-content alignment, JSON-LD support and the absence of guaranteed rich-result display.
- [X card markup documentation entry](https://developer.x.com/en/docs/x-for-websites/cards/overview/markup): during this check it redirected to the generic [X documentation overview](https://docs.x.com/overview), which did not verify current card-specific limits. Recheck primary card documentation when platform behaviour or dimensions matter; record unresolved requirements instead of inventing precise limits.

For device icons, checked on 2026-10-09 (JST):

- [WHATWG HTML icon link type](https://html.spec.whatwg.org/multipage/links.html#link-type-icon): selection among icon candidates may use `type`, `media` and `sizes`.
- [MDN `<link>` reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link): `sizes="any"` for scalable icons and ICO multi-size support notes. Use as practical reference alongside the standard.
- [Apple Safari Web Content Guide — Web Clips](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html): documents `apple-touch-icon` and gives a 180x180 example. This is archived guidance; confirm actual current iOS/iPadOS Home Screen rendering on target versions when required.
- [Apple Safari Web Content Guide — pinned tab icons](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/pinnedTabs/pinnedTabs.html): describes `mask-icon` artwork as single-colour. Treat this as an optional Safari-specific context.
- [MDN manifest `icons`](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/icons), [`id`](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/id), [`start_url`](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/start_url) and [`scope`](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/scope): path resolution, icon purpose and manifest member semantics.
- [W3C Web Application Manifest](https://www.w3.org/TR/appmanifest/): current 2026-10-08 document is a Working Draft. Its URL-processing algorithms define manifest-relative `start_url` and `scope` resolution and resolve `id` against the origin of `start_url`; check the current text and browser behaviour when identity handling matters.
- [MDN making PWAs installable](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable): lists the 192px and 512px icons in Chromium-based browser installability criteria. This is not a universal favicon or web-manifest requirement.
- [MDN defining app icons](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Define_app_icons): explains maskable icons and the 80%-diameter safe zone.

The absolute-public-URL gate and explicit X fields above are this project's implementation requirements. Do not present them as a newly verified universal provider rule.
