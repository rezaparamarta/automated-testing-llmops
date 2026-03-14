from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


def create_eval_chain(
    agent_response,
    llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
    output_parser=StrOutputParser()
):
    delimiter = "####"

    eval_system_prompt = f"""
You are an assistant that evaluates whether or not an assistant is producing valid quizzes.
The assistant should be producing output in the format of Question N:{delimiter} <question N>?
"""

    eval_user_message = f"""
You are evaluating a generated quiz based on the context that the assistant uses to create the quiz.

Here is the data:

[BEGIN DATA]
************
[Response]: {agent_response}
************
[END DATA]

Read the response carefully and determine if it looks like a quiz or test.

Do not evaluate if the information is correct.
Only evaluate if the data is in the expected format.

Output Y if the response is a quiz.
Output N if the response does not look like a quiz.
"""

    eval_prompt = ChatPromptTemplate.from_messages([
        ("system", eval_system_prompt),
        ("human", eval_user_message),
    ])

    return eval_prompt | llm | output_parser