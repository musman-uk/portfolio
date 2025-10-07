
from independent_projects.quality_assurance_checkpoint.examples.example_2_mutable_default_argument import fixed_script


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
