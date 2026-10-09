# Semantic first-pass smoke case

Status: draft case. A description is not a test result. Record the host, model, exact prompt, generated artifacts, checks, and failures for every run.

## Prompt

Create a one-page landing page for a fictional ceramics studio. Its audience is people shopping for handmade homeware; its main task is viewing the collection. The desktop hero heading is vertical and becomes horizontal on mobile, with clear spacing from adjacent text. A supplied image depicts a cobalt-blue hand-thrown bowl on a pale table. Use a useful image alternative; add a visible caption only if it contributes information. Include an ordered three-step making process, a real `#collection` link, and footer navigation.

The collection link has a decorative arrow that must stay still. Its underline must reveal left-to-right on hover and keyboard focus, take 300ms, sit below the text, and stop before the arrow with visible clearance. Honour `prefers-reduced-motion`. Do not add academic links, unsupported product claims, visible `unknown` placeholders, or a network form. Keep the page concise.

Implement the page. Verify it at 375px and 1440px widths. Report what was actually checked and mark checks that did not run.

## Acceptance checks

- The response identifies the audience, main task, content facts, and requested prohibitions before layout decisions.
- The implementation includes one heading hierarchy, semantic navigation, an ordered process list, the requested collection destination, and an image alternative appropriate to the supplied image. There is no redundant caption.
- The vertical-to-horizontal heading change and adjacent spacing are implemented at the named viewports; the document does not overflow or overlap at either width.
- The underline uses a base-state `::after` transform from `scale(0, 1)` to `scale(1, 1)`, `transform-origin: left top`, and a 300ms transform transition. Hover and focus states reveal it; the line does not touch or move the arrow.
- Reduced-motion behavior preserves the collapsed base state and shows the requested underline without the full-duration transition.
- Browser rendering and hover/focus behavior are marked `untested` unless they actually ran. A code snippet or screenshot alone is not reported as runtime proof.
- The output contains no irrelevant external links, invented claims, or visitor-facing uncertainty placeholders.
