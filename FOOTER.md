## Contributing

Corrections matter more than additions. If a link has moved, a portal has started charging, or a description is wrong, please open an issue or a pull request.

To add a source, add an object to `research/entries.json` with these fields and run `python3 build_readme.py`:

```json
{
  "category": "Courts, tribunals and law",
  "name": "Name of the source",
  "url": "https://...",
  "what": "One sentence on what a journalist can find there.",
  "access": "open | free login | captcha | paid | partly paid",
  "run_by": "Who runs it",
  "status": "ok | unreachable | changed",
  "checked": "YYYY-MM-DD",
  "note": "Optional caveat"
}
```

Please open the link yourself on the day you add it, and keep to the scope above: no people-search services and nothing built on breached personal data.

## Related

- [india-osint](https://github.com/Ghongha007/india-osint): public records and open data for investigating India
- [china-osint](https://github.com/Ghongha007/china-osint): public records and open data for investigating China
- [russia-osint](https://github.com/Ghongha007/russia-osint): public records and open data for investigating Russia
- [usa-osint](https://github.com/Ghongha007/usa-osint): public records and open data for investigating the United States
- [ukraine-osint](https://github.com/Ghongha007/ukraine-osint): public records and open data for investigating Ukraine
- [ai-for-osint](https://github.com/Ghongha007/ai-for-osint): AI tools for investigators, with where each runs and its known limits
- [groundline](https://github.com/Ghongha007/groundline): check every sentence of a draft or AI summary against its source documents
- [chat2net](https://github.com/Ghongha007/chat2net): turn a chat or social-media export into a Gephi network
- [osint-skills](https://github.com/Ghongha007/osint-skills): agent skills for verification, geolocation, chronolocation and fact-checking
- [verify-mcp](https://github.com/Ghongha007/verify-mcp): an MCP server with keyless, read-only verification lookups

## Licence

The list is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The script is MIT. Compiled by [OSINT JOURNO](https://github.com/OSINT-JOURNO).
