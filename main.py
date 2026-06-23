from ai import ask_gemini

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = ask_gemini(question)

    print("Astra:", answer)