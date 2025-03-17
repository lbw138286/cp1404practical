import datetime

class Project:
    """Represents a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Initialize a Project object."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Sort projects by priority (lower value = higher priority)."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion == 100

