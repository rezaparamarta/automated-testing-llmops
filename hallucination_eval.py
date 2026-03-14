from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


def create_hallucination_eval_chain(context, agent_response):

    eval_system_prompt = """
You are an assistant that evaluates whether a quiz uses only facts from a known question bank.

Quizzes that include facts outside the question bank are BAD quizzes.
"""

    eval_user_message = f"""
You are evaluating a generated quiz.

[Question Bank]
{context}

[Generated Quiz]
{agent_response}

Check whether the quiz only references facts from the question bank.

Output:
Y → if all facts are from the question bank
N → if the quiz contains made-up facts
"""

    eval_prompt = ChatPromptTemplate.from_messages([
        ("system", eval_system_prompt),
        ("human", eval_user_message),
    ])

    return eval_prompt | ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    ) | StrOutputParser()