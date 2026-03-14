from app import assistant_chain, system_message
from hallucination_eval import create_hallucination_eval_chain


def load_quiz_bank():
    with open("datasets/quiz_bank.txt") as f:
        return f.read()


def test_model_graded_eval_hallucination():

    quiz_bank = load_quiz_bank()

    assistant = assistant_chain(system_message)

    quiz_request = "Write me a quiz about books."

    result = assistant.invoke({"question": quiz_request})

    print("\nGenerated Quiz:\n", result)

    evaluator = create_hallucination_eval_chain(quiz_bank, result)

    eval_response = evaluator.invoke({})

    print("\nHallucination Check:", eval_response)

    assert "N" in eval_response.upper()