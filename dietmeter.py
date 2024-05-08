import langchain_openai
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


class dietmeter:

    def __init__(self):
        print("begin")
        api_key = ''
        self.chat_history_data = ChatMessageHistory()

        self.openai_llm = langchain_openai.ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2, api_key=api_key)

        self.SYSTEM_TEMPLATE = \
            """
            "You are a helpful healthy manager. Answer all questions to the best of your ability.",
            Answer the user's questions based on the below context. 
            If the context doesn't contain any relevant information to the question, don't make something up and just say "I don't know":
            <context>
            {context}
            </context>
            """

        self.chain = self.init_chain()

    def init_chain(self):
        # chain setup

        ans_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    self.SYSTEM_TEMPLATE,
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
            ]
        )

        chat_chain = ans_prompt | self.openai_llm

        return RunnableWithMessageHistory(
            chat_chain,
            lambda session_id: self.chat_history_data,
            input_messages_key="input",
            history_messages_key="chat_history",
        )

    def chat_to_openai(self, user_input):
        return self.chain.invoke(
            {
                "input": user_input,
                'chat_history': self.chat_history_data
            },  # Mapping values to placeholders
            {"configurable": {"session_id": "unused"}},
        )

        # return self.chat_chain.invoke({"chat_history": chat_history_data, "context": user_input})
