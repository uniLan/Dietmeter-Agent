import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv('.env')
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)










def main():

    pass





if __name__ == '__main__':
    main()