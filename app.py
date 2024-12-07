print("Welcome to the Word Count Program")

try:
    # Prompt the user to input a string
    user_input = str(input("Enter a string: "))

    word_count = len(user_input)
    # Print the number of words
    print("Number of characters in the string are:", word_count)

except Exception as e:
    print("An error occurred:", e)
