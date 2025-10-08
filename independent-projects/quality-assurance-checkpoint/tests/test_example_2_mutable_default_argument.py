import importlib.util
import pathlib

# Dynamically load the fixed_script module for Example 2 - Mutable Default Argument
SCRIPT_PATH = (
    pathlib.Path(__file__).parent.parent
    / "examples"
    / "example_2_mutable_default_argument"
    / "fixed_script.py"
)

spec = importlib.util.spec_from_file_location("fixed_script", SCRIPT_PATH)
fixed_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixed_script)


def test_collect_logs_starts_fresh_each_time():
    """
    Verify that each call to collect_logs starts with a new list
    when no existing list is provided.
    """
    first = fixed_script.collect_logs("Error: Disk full")
    second = fixed_script.collect_logs("Warning: Low memory")
    third = fixed_script.collect_logs("Info: Job completed")

    # Each call should return a single-element list, not accumulate across calls
    assert first == ["Error: Disk full"]
    assert second == ["Warning: Low memory"]
    assert third == ["Info: Job completed"]


def test_collect_logs_with_existing_list():
    """
    Verify that collect_logs appends to an explicitly provided list
    and does not create a new one.
    """
    logs = ["Startup"]
    updated = fixed_script.collect_logs("Shutdown", logs)

    # The provided list should be updated in place
    assert updated == ["Startup", "Shutdown"]
    assert logs is updated


def test_summarize_logs_counts_messages():
    """Verify that summarize_logs correctly counts repeated messages."""
    logs = ["Error", "Error", "Warning"]
    summary = fixed_script.summarize_logs(logs)

    # Expect two "Error" entries and one "Warning"
    assert summary == {"Error": 2, "Warning": 1}
