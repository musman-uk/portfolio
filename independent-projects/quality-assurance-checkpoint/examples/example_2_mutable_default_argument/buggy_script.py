"""
Example 2: Mutable Default Argument Bug

Scenario:
- A logging utility that collects messages into lists.
- Intended to allow either starting fresh or appending to an existing list.
- BUG: uses a mutable default argument, so logs persist across calls.
"""

from typing import List, Dict


def collect_logs(message: str, logs: List[str] = []) -> List[str]:
    """
    Append a message to the logs list.

    Parameters
    ----------
    message : str
        The log message to add.
    logs : List[str], optional
        The list of logs to append to. Defaults to a shared list (BUG).

    Returns
    -------
    List[str]
        The updated list of logs.

    Notes
    -----
    - This function contains an intentional bug: the default list is shared
      across calls, so messages accumulate unexpectedly.
    """
    logs.append(message)
    return logs


def summarize_logs(logs: List[str]) -> Dict[str, int]:
    """
    Summarize logs by counting occurrences of each message.

    Parameters
    ----------
    logs : List[str]
        A list of log messages.

    Returns
    -------
    Dict[str, int]
        A dictionary mapping each unique message to its count.
    """
    summary: Dict[str, int] = {}
    for msg in logs:
        summary[msg] = summary.get(msg, 0) + 1
    return summary


def main():
    """Demonstration of the buggy logging behaviour."""
    print("=== Buggy Logging Demo ===")
    first = collect_logs("Error: Disk full")
    second = collect_logs("Warning: Low memory")
    third = collect_logs("Info: Job completed")

    # Because of the mutable default bug, each call shares the same list
    print("First call:", first)
    print("Second call:", second)
    print("Third call:", third)
    print("Summary:", summarize_logs(third))


if __name__ == "__main__":
    main()
