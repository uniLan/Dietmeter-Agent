import dotenv
import json
import dietmeter
import user



def main():
    # create a while loop that will receive suer input and display the output
    while True:
        user_input = input("Enter your message: ")
        if user_input == 'exit':
            break

        # create a dietmeter object
        diet_meter = dietmeter.dietmeter()
        # chat to openai
        chat_response = diet_meter.chat_to_openai(user_input)
        # print the response
        print('Dietmeter: ', chat_response.content)


if __name__ == '__main__':
    main()
