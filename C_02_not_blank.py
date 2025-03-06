def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't b blank. Please try again.\n")


# Main routine starts here
who = not_blank("Please enter your name: ")
print(f"Hello {who}")
