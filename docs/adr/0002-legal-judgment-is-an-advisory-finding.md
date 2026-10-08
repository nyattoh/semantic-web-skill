# Legal and provider-policy judgment is an advisory finding, never a pass

Status: accepted (2026-10-09)

The owner wants the agent to search current law and provider policy and judge whether content conforms, instead of maintaining static legal rules. We keep that: the agent searches primary sources on the day of the run and records citations, retrieval date and a reasoned reading. We do not let that reading produce `passed`. Its result is always `needs_review` with the Advisory finding attached, because a search-based reading can miss or misread a source and the project cannot certify compliance (product spec sections 10 and 12).

Considered: static region rules maintained by the project (slow, goes stale, cannot cover many regions) versus AI judgment reported as `passed` (overclaims). Coverage of many regions is therefore achieved by a research procedure plus a declared Regional pack per market, not by claiming certified rules; a market without a pack is reported as unsupported.
