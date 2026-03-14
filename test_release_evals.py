from app import assistant_chain
from eval_model import create_eval_chain
from app import system_message


def test_model_graded_eval_good():

    assistant = assistant_chain(system_message)

    question = "Generate a quiz about science."

    response = assistant.invoke({"question": question})

    eval_chain = create_eval_chain(response)

    grade = eval_chain.invoke({})

    print("\nGenerated Quiz:\n", response)
    print("\nEvaluation Result:", grade)

    assert grade.strip() == "Y"


def test_model_graded_eval_bad():

    bad_response = "There are lots of interesting facts. Tell me more about what you'd like to know."

    eval_chain = create_eval_chain(bad_response)

    grade = eval_chain.invoke({})

    print("\nBad Response:\n", bad_response)
    print("\nEvaluation Result:", grade)

    assert grade.strip() == "N"