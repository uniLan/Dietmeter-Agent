import dotenv
import json
import dietmeter as dm
import user


def main():

    dietmeter = dm.dietmeter()
    # create a while loop that will receive suer input and display the output
    while True:
        user_input = input("Enter your message: ")
        if user_input == 'exit':
            break
        # chat to openai
        chat_response = dietmeter.chat_to_openai(user_input)
        # print the response
        print('Dietmeter: ', chat_response.content)


if __name__ == '__main__':
    main()
