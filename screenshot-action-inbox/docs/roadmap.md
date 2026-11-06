# Implementation roadmap

No runtime features have been completed yet. This commit provides the Phase 1 design and scaffold.

| Phase | Deliverable | Completion check |
| --- | --- | --- |
| 1 | Scope, architecture, data model, API contracts, folders | Trace upload -> extraction -> review -> approved task |
| 2 | FastAPI foundation, configuration, logs, health endpoint | Server starts; health and configuration tests pass |
| 3 | Image upload/storage and SQLite records | Valid image survives restart; invalid input rejected; deletion works |
| 4 | Vision extraction and validated output | Synthetic examples extract; missing fields remain missing; timeout/malformed-output tests pass |
| 5 | Corrections, approval, task lifecycle | Corrections persist; unapproved items cannot create tasks; completion works |
| 6 | React interface | Upload, review, save, search, and complete through browser |
| 7 | Reliability, exact-file duplicate detection, Docker, CI | Relevant tests pass locally and in CI; documented container setup works |
| 8 | Portfolio documentation and demo | Another person can follow setup and assess actual implemented behavior |

## Next milestone: backend foundation
Create backend dependency configuration and app/main.py. Add configuration loading, safe logging, GET /health, and tests. Expected response:

```json
{"status": "ok", "service": "screenshot-action-inbox"}
```

Document install, run, and test commands only after validating them. No vision API key is needed for the health endpoint.

## Evaluation approach
Use a small synthetic or redacted set across all three categories. Record expected fields, missing-field behavior, date ambiguities, incorrect extractions, and API failures. Report measured outcomes only after running evaluation. Include blurry screenshots and conflicting dates.

## Later releases
Reminders, calendar integration with explicit approval, semantic search/RAG, OCR fallback if useful, and user accounts before public multi-user use.
