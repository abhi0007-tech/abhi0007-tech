# Proposed data model

These are design contracts, not implemented migrations.

## Screenshots
| Field | Purpose |
| --- | --- |
| id | Generated unique identifier |
| original_filename | Display name only |
| storage_key | Backend-generated file reference |
| media_type, byte_size, width, height | Validated image metadata |
| created_at | Upload timestamp |
| processing_status | uploaded, extracting, extracted, failed |
| error_code | Safe failure classification, nullable |

## Items
| Field | Purpose |
| --- | --- |
| id, screenshot_id | Identity and unique link to screenshot |
| category | notice_event, bill, job_opening, other |
| title, summary | Editable description |
| details_json | Validated category-specific fields |
| suggested_actions_json | Proposed actions, never automatically tasks |
| review_notes_json | Missing or ambiguous information |
| original_extraction_json | Original structured proposal for comparison |
| review_status | needs_review or approved |
| created_at, updated_at, reviewed_at | Lifecycle timestamps |

The original proposal is retained when fields are corrected. Limit JSON size and validate its contents through category-specific Pydantic schemas. This keeps the initial SQLite schema small without making arbitrary JSON trusted.

### Category fields
- Notice/event: organizer, location, event date/time, action deadline.
- Bill: provider, amount, currency, due date.
- Job opening: company, role, location, application URL, deadline.
- Other: editable summary and notes, without invented category fields.

Amounts should use decimal-safe representation, not floating-point arithmetic. Dates retain source text and distinguish date-only values from timezone-aware date/time values.

## Tasks
| Field | Purpose |
| --- | --- |
| id, item_id | Identity and source link |
| title | User-approved action |
| due_date | Confirmed date-only deadline, nullable |
| due_at | Confirmed timezone-aware instant, nullable |
| timezone | User-confirmed timezone when applicable |
| status | pending, completed, cancelled |
| created_at, updated_at, completed_at | Lifecycle timestamps |

At most one of due_date and due_at may be populated. A task may have no deadline. Updating item details does not silently update previously approved tasks.

## Relationships
- Screenshot -> zero or one item.
- Item -> zero or many tasks.
- Enable SQLite foreign key enforcement and explicit cascading deletion.
- Original files remain outside the database; their references live in screenshots.
