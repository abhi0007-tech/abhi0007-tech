# Screenshot Action Inbox

Turn saved screenshots into organized information and user-approved tasks.

> Status: Phase 1 design and project scaffold only. No application, AI integration, or tests have been implemented or validated yet.

## The problem
Screenshots of college notices, bills, events, and job openings often get buried in a gallery. Important details and deadlines become hard to find.

## Planned first release
1. Upload a PNG or JPEG screenshot.
2. Extract structured information using a vision-capable AI model.
3. Review the proposed information beside the original image.
4. Correct and save it.
5. Approve suggested tasks, then track their completion.
6. Search, filter, and delete saved items.

Initial categories: notices/events, bills, and job openings. Unknown details remain empty; ambiguous dates require review.

## Planned technology
| Component | Choice | Purpose |
| --- | --- | --- |
| Frontend | React and Vite | Inbox, upload, review, tasks |
| Backend | Python and FastAPI | APIs and application rules |
| Validation | Pydantic | Request and extraction schemas |
| Extraction | Vision model API, provider undecided | Interpret image content |
| Persistence | SQLite | Records, corrections, tasks |
| Images | Local storage initially | Original screenshots |
| Tests | pytest | Backend behavior and failure handling |
| Packaging | Docker, later | Reproducible setup |
| CI | GitHub Actions, later | Automated checks |

Versions and provider capabilities will be checked against official documentation during implementation.

## Design documents
- [Architecture and workflow](docs/design.md)
- [Proposed data model](docs/data-model.md)
- [Proposed API contracts](docs/api-contracts.md)
- [Phases and completion criteria](docs/roadmap.md)

## Layout
- `backend/app/`: future API, configuration, schemas, services, provider adapter, persistence
- `backend/tests/`: future backend tests
- `frontend/`: future React application
- `docs/`: Phase 1 decisions

## Setup
There is no runnable application yet. Phase 2 will add a tested FastAPI health endpoint, dependency configuration, and exact setup commands. The optional `.env.example` contains no credentials; no API key is needed for Phase 1.

## Boundaries
The first release is a local, single-user application. Reminders, calendar writes, authentication, OCR fallback, RAG, and semantic search are future work. Public multi-user deployment requires access control and further operational work.

Never commit private screenshots, real bills, credentials, local databases, or proprietary work material. Use synthetic or redacted examples for demonstrations.
