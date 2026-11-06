# Proposed API contracts

Not implemented. JSON naming, status codes, and payload schemas will become executable contracts during backend development.

| Method | Path | Purpose | Success |
| --- | --- | --- | --- |
| GET | /health | Process liveness only | 200 |
| POST | /screenshots | Multipart upload, field: file | 201 |
| GET | /screenshots | Paginated list; processing-status filter | 200 |
| GET | /screenshots/{id} | Metadata and extraction details | 200 |
| GET | /screenshots/{id}/image | Serve original validated image | 200 |
| POST | /screenshots/{id}/extract | Extract a new item or retry a failed attempt | 200 |
| GET | /items | Search titles/summaries; filter category/review status | 200 |
| PATCH | /items/{id} | Save validated user corrections | 200 |
| POST | /items/{id}/approve | Mark reviewed information approved | 200 |
| POST | /items/{id}/tasks | Explicitly create a task from user-approved fields | 201 |
| GET | /tasks | Paginated tasks; status and deadline filters | 200 |
| PATCH | /tasks/{id} | Update title, deadline, or status | 200 |
| DELETE | /screenshots/{id} | Delete source image and related records | 204 |

## Rules
- Synchronous extraction first, with a bounded timeout; no background-job infrastructure yet.
- Reject concurrent extraction and extraction over an existing item with 409.
- Task creation requires an approved item.
- Repeated item approval is idempotent; repeated task creation is not. UI disables duplicate submissions; request idempotency can be added later.
- PATCH validates provided fields and applies changes atomically.
- Editing reviewed information resets review status.
- Search starts with SQLite-backed text matching.
- Pagination uses limit/offset with bounded limits.

## Errors
- 404: record missing.
- 413: upload too large.
- 415: unsupported image type.
- 422: invalid fields, corrupt image, or unresolved deadline supplied as a confirmed task date.
- 409: incompatible lifecycle state.
- 502: provider failure or invalid provider output.
- 504: provider timeout.
- 500: unexpected application failure, with a safe message.

Proposed application error shape:

```json
{
  "error": {
    "code": "extraction_failed",
    "message": "Could not extract this screenshot. Please retry.",
    "request_id": "generated-request-id"
  }
}
```

Use exception handlers to normalize request-validation and application errors. Never return provider secrets, raw provider responses, or internal file paths.
