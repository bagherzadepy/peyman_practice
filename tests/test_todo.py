from src.todo import add_task, remove_task, mark_done


def test_add_task():
    tasks = []
    add_task(tasks, "Learn Python")
    assert "Learn Python" in tasks


def test_remove_task():
    tasks = ["Task1", "Task2"]
    remove_task(tasks, 1)
    assert tasks == ["Task2"]


def test_mark_done():
    tasks = ["Task1"]
    mark_done(tasks, 1)
    assert tasks[0].endswith("✅")
