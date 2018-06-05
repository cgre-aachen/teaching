
c = get_config()

c.Exchange.course_id = "course1"
c.CourseDirectory.db_assignments = [
    dict(name = "assignment1")
]
c.ClearSolutions.code_stub = "# YOUR CODE HERE"
c.LateSubmissionPlugin.penalty_method = "none"
c.ExecutePreprocessor.kernel_name = "python3"
c.CourseDirectory.db_students = [
    dict(id = "jd223344", first_name="Jane",
        last_name="Doe"),
    dict(id = "mm234567", first_name="Max",
        last_name="Mustermann")
]
