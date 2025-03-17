import datetime
from project import Project

FILENAME = "projects.txt"

def main():
    """Main function to manage projects."""
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = ""
    while choice != "q":  # Loop until user chooses to quit
        print_menu()
        choice = input(">>> ").strip().lower()

        if choice == "l":
            projects = load_projects(input("Enter filename: "))
        elif choice == "s":
            save_projects(input("Enter filename: "), projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            projects.append(add_new_project())
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save_if_needed(projects)
            print("Thank you for using the project management software.")
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    """Display menu options."""
    print("- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n"
          "- (F)ilter projects by date  \n- (A)dd new project  \n- (U)pdate project  \n- (Q)uit")

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, "r") as file:
            file.readline()  # Skip header
            for line in file:
                parts = line.strip().split("\t")
                if len(parts) == 5:
                    name, date, priority, cost, completion = parts
                    projects.append(Project(name, date, int(priority), float(cost), int(completion)))
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with an empty list.")
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate:.2f}\t{project.completion}\n")
    print(f"Projects saved to {filename}.")

def display_projects(projects):
    """Display projects, grouped by completion status and sorted by priority."""
    incomplete_projects = sorted([p for p in projects if not p.is_complete()])
    completed_projects = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = sorted([p for p in projects if p.start_date > filter_date], key=lambda p: p.start_date)
        for project in filtered_projects:
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")

def add_new_project():
    """Prompt user for a new project and return a Project object."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: "))
    completion = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost, completion)

def update_project(projects):
    """Allow the user to update a project's completion or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project)

        new_completion = input("New Percentage: ").strip()
        if new_completion:
            project.completion = int(new_completion)

        new_priority = input("New Priority: ").strip()
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid selection.")

def save_if_needed(projects):
    """Ask user if they want to save before quitting."""
    save_choice = input(f"Would you like to save to {FILENAME}? (y/n): ").strip().lower()
    if save_choice == "y":
        save_projects(FILENAME, projects)

if __name__ == "__main__":
    main()

