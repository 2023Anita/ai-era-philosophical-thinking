#!/usr/bin/env python3
"""Validate the static course catalog and its direct entry pages."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "courses" / "catalog.json"


def main() -> int:
    errors: list[str] = []
    try:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"FAIL: missing {CATALOG}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"FAIL: invalid catalog JSON: {exc}")
        return 1

    courses = data.get("courses", [])
    if len(courses) != 3:
        errors.append(f"expected 3 initial course entries, found {len(courses)}")

    for course in courses:
        course_id = course.get("id", "<missing id>")
        for field in ("title", "description", "path", "cover"):
            if not course.get(field):
                errors.append(f"{course_id}: missing {field}")

        relative_path = str(course.get("path", "")).removeprefix("./")
        course_dir = ROOT / relative_path
        if not course_dir.is_dir():
            errors.append(f"{course_id}: missing directory {relative_path}")
        elif not (course_dir / "index.html").is_file():
            errors.append(f"{course_id}: missing index.html")

        cover_path = str(course.get("cover", "")).removeprefix("./")
        if cover_path and not (ROOT / cover_path).is_file():
            errors.append(f"{course_id}: missing cover {cover_path}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {len(courses)} course entries and direct pages are present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
