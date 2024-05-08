import dotenv
import json
from langchain_openai import ChatOpenAI

dotenv.load_dotenv('.env')
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

def load_profile():
    '''load the user profile JSON format'''
    pass


def chatBegin():
    pass







def main():

    pass





if __name__ == '__main__':
    main()