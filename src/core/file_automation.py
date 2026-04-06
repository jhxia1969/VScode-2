from pathlib import Path


def batch_rename(
    directory: Path,
    prefix: str,
    start_index: int = 1,
    extension_filter: str = "",
    dry_run: bool = False,
) -> list[tuple[str, str]]:
    if not directory.exists() or not directory.is_dir():
        raise NotADirectoryError(f"Invalid directory: {directory}")

    files = [p for p in directory.iterdir() if p.is_file()]
    if extension_filter:
        files = [p for p in files if p.suffix.lower() == extension_filter.lower()]

    files.sort(key=lambda p: p.name)
    results: list[tuple[str, str]] = []

    current = start_index
    for old_path in files:
        new_name = f"{prefix}_{current:03d}{old_path.suffix}"
        results.append((old_path.name, new_name))
        if not dry_run:
            old_path.rename(old_path.with_name(new_name))
        current += 1

    return results
