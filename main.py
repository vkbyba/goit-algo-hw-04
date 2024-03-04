def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower() if parts else ''
    args = parts[1:]  # Get the rest of the parts as arguments
    return cmd, args

def add_contact(args, contacts):
    if len(args) < 2:  # Check if there are enough arguments
        return "Not enough arguments to add a contact."
    name, phone = args[0], args[1]  # Unpack the first two arguments
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
