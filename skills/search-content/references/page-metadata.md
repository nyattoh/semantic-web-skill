# Page metadata and structured data

Use this reference when creating or reviewing a page description, Open Graph, X cards or JSON-LD. These are draft requirements for agent work, not implemented audit rules.

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

The absolute-public-URL gate and explicit X fields above are this project's implementation requirements. Do not present them as a newly verified universal provider rule.
