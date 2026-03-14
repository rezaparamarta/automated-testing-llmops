from app import assistant_chain, system_message
from quality_eval import create_quality_eval_chain


def test_quality_score():

    assistant = assistant_chain(system_message)

    response = assistant.invoke({
        "question": "Generate a quiz about science."
    })

    print("\nGenerated Quiz:\n", response)

    evaluator = create_quality_eval_chain(response)

    score = evaluator.invoke({})

    print("\nQuality Score:\n", score)

    assert "Score" in score