#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

import openai

openai.api_key = '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'

def get_chat_response(user_input):
    # Call the OpenAI API to get the response
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=user_input,
        max_tokens=150
    )

    return response.choices[0].text.strip()

def main():
    print("ChatBox - Type 'exit' to end the conversation")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Exiting the chat.")
            break

        
        response = get_chat_response(user_input)

        # Print the response
        print(f"ChatBox: {response}")

if __name__ == "__main__":
    main()
