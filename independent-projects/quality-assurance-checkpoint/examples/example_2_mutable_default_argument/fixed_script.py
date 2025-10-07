"""
Example 2: Mutable Default Argument Fixed

Fix:
- Use None as the default argument.
- Initialize a new list inside the function when no list is provided.
"""

from typing import List, Dict, Optional


def collect_logs(message: str, logs: Optional[List[str]] = None) -> List[str]:
    """
    Append a message to a new or provided logs list.

    Parameters
    ----------
    message : str
        The log message to add.
    logs : List[str] or None, optional
        The list of logs to append to. If None, a new list is created.

    Returns
    -------
    List[str]
        The updated list of logs.
    """
    if logs is None:
        logs = []
    logs.append(message)
    return logs


def summarize_logs(logs: List[str]) -> Dict[str, int]:
    """
    Summarize logs by counting occurrences of each message.
    """
    summary: Dict[str, int] = {}
    for msg in logs:
        summary[msg] = summary.get(msg, 0) + 1
    return summary


def main():
    print("=== Fixed Logging Demo ===")
    first = collect_logs("Error: Disk full")
    second = collect_logs("Warning: Low memory")
    third = collect_logs("Info: Job completed")

    print("First call:", first)
    print("Second call:", second)
    print("Third call:", third)
    print("Summary:", summarize_logs(third))


if __name__ == "__main__":
    main()

