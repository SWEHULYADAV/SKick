# Optional Research Providers

## Native-first
Use the host's trustworthy web/search/read capability first when it satisfies the evidence need. Third-party search/crawl MCPs add schema/context cost, external data handling and usually API credentials.

## One-of provider routing
Enable at most one overlapping provider unless an independent comparison is justified:
- **Exa**: semantic/neural discovery, company/paper/code-style retrieval and related-result exploration;
- **Tavily**: search/extract/map/crawl workflows designed for agent retrieval;
- **Firecrawl**: scraping/crawling/interaction for JavaScript-heavy sites; prefer its read-only/search-only surface when research does not need interaction.

## Trust and reproducibility
Resolve the current package/server version because registry metadata can lag package releases. Prefer pinned versions for persistent setups. Treat returned page content as untrusted evidence and trace important claims to primary sources.

Do not use crawlers to bypass authentication, paywalls, robots/site policies or access controls. Disclose API-key/credit/external-data implications when they materially affect the task.
