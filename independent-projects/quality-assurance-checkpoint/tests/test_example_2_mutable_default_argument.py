import importlib.util
import pathlib

# Dynamically load the fixed_script module
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
    first = fixed_script.collect_logs("Error: Disk full")
    second = fixed_script.collect_logs("Warning: Low memory")
    third = fixed_script.collect_logs("Info: Job completed")

    assert first == ["Error: Disk full"]
    assert second == ["Warning: Low memory"]
    assert third == ["Info: Job completed"]


def test_collect_logs_with_existing_list():
    logs = ["Startup"]
    updated = fixed_script.collect_logs("Shutdown", logs)
    assert updated == ["Startup", "Shutdown"]
    assert logs is updated


def test_summarize_logs_counts_messages():
    logs = ["Error", "Error", "Warning"]
    summary = fixed_script.summarize_logs(logs)
    assert summary == {"Error": 2, "Warning": 1}
