import json
from app import assistant_chain, system_message


def load_dataset():
    with open("datasets/quiz_topics.json") as f:
        return json.load(f)


def test_dataset_driven_quizzes():

    dataset = load_dataset()

    assistant = assistant_chain(system_message)

    for topic, keywords in dataset.items():

        question = f"Generate a quiz about {topic}."

        response = assistant.invoke({"question": question})

        print("\nTopic:", topic)
        print(response)

        assert any(word in response.lower() for word in keywords)