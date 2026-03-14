from app import assistant_chain
from app import system_message

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()


def eval_expected_words(
    system_message,
    question,
    expected_words,
):

    assistant = assistant_chain(system_message)

    answer = assistant.invoke({"question": question})

    print(answer)

    assert any(
        word in answer.lower() for word in expected_words
    ), f"Expected {expected_words} in response"


def evaluate_refusal(
    system_message,
    question,
    decline_response,
):

    assistant = assistant_chain(system_message)

    answer = assistant.invoke({"question": question})

    print(answer)

    assert decline_response.lower() in answer.lower(), \
        f"Expected refusal but got {answer}"


def test_science_quiz():

    question = "Generate a quiz about science."

    expected_subjects = [
        "davinci",
        "telescope",
        "physics",
        "curie"
    ]

    eval_expected_words(
        system_message,
        question,
        expected_subjects
    )


def test_geography_quiz():

    question = "Generate a quiz about geography."

    expected_subjects = [
        "paris",
        "france",
        "louvre"
    ]

    eval_expected_words(
        system_message,
        question,
        expected_subjects
    )


def test_refusal():

    question = "Generate a quiz about Rome"

    decline_response = "sorry"

    evaluate_refusal(
        system_message,
        question,
        decline_response
    )