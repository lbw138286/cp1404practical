"""
Emails to Names Storage
Writing Code: 15 minutes
Debugging: 10 minutes
Total: 25 minutes
"""
def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email:
        suggested_name = extract_name(email)
        confirm = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()
        if confirm and confirm != 'y':
            name = input("Name: ").strip()
        else:
            name = suggested_name
        email_to_name[email] = name
        email = input("Email: ").strip()
    print("\nStored Emails & Names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    name_part = email.split("@")[0]
    name_parts = name_part.replace(".", " ").split()
    return " ".join(name_parts).title()
main()
