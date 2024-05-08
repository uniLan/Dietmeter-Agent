import langchain_openai
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

class dietmeter:

    def __init__(self):
        api_key = ''
        self.chat_history_data = ChatMessageHistory()

        self.openai_llm = langchain_openai.ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2, api_key=api_key)

        self.SYSTEM_TEMPLATE = \
            """
            Answer the user's questions based on the below context. 
            If the context doesn't contain any relevant information to the question, don't make something up and just say "I don't know":
            <context>
            {context}
            </context>
            """

        self.instructions = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful healthy manager. Answer all questions to the best of your ability.",
                ),
            ]
        )
        self.chat_chain = self.instructions | self.openai_llm
        '''
        self.ans_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    self.SYSTEM_TEMPLATE,
                ),
                MessagesPlaceholder(variable_name="chat_history"),
            ]
        )

        self.chat_chain = self.instructions | self.ans_prompt | self.openai_llm
        '''

    def chat_to_openai(self, user_input):
        return self.chat_chain.invoke(
            {

                "context": user_input

            }
        )

        # return self.chat_chain.invoke({"chat_history": chat_history_data, "context": user_input})
