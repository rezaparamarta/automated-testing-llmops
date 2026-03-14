from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

delimiter = "####"

quiz_bank = """1. Subject: Leonardo DaVinci
   Categories: Art, Science
   Facts:
    - Painted the Mona Lisa
    - Studied zoology, anatomy, geology, optics
    - Designed a flying machine

2. Subject: Paris
   Categories: Art, Geography
   Facts:
    - Location of the Louvre, the museum where the Mona Lisa is displayed
    - Capital of France
    - Most populous city in France
    - Where Radium and Polonium were discovered by scientists Marie and Pierre Curie

3. Subject: Telescopes
   Category: Science
   Facts:
    - Device to observe different objects
    - The first refracting telescopes were invented in the Netherlands in the 17th Century
    - The James Webb space telescope is the largest telescope in space

4. Subject: Starry Night
   Category: Art
   Facts:
    - Painted by Vincent van Gogh in 1889
    - Captures the east-facing view of van Gogh's room in Saint-Rémy-de-Provence

5. Subject: Physics
   Category: Science
   Facts:
    - The sun doesn't change color during sunset
    - Water slows the speed of light

6. Subject: Rendang
   Category: Food
   Facts:
    - Traditional Indonesian dish from West Sumatra
    - Made from beef slow-cooked with coconut milk and spices
    - Often considered one of the most delicious foods in the world

7. Subject: Nasi Goreng
   Category: Food
   Facts:
    - Indonesian fried rice dish
    - Commonly served with egg and crackers
    - Often cooked with sweet soy sauce (kecap manis)

8. Subject: Sate
   Category: Food
   Facts:
    - Skewered and grilled meat dish
    - Served with peanut sauce
    - Popular street food across Indonesia
"""

system_message = f"""
Follow these steps to generate a customized quiz for the user.

Step 1:{delimiter} Identify the category:
* Geography
* Science
* Art
* Food

Step 2:{delimiter} Determine subjects from the quiz bank.

{quiz_bank}

Pick up to two subjects that match the category.

Step 3:{delimiter} Generate 3 quiz questions.

Format:

Question 1:{delimiter} <question>

Question 2:{delimiter} <question>

Question 3:{delimiter} <question>

Rules:

- Only use explicit matches for the category
- If the category does not exist say you don't have information
- If subject not known answer "I'm sorry I do not have information about that"
"""


def assistant_chain(
    system_message=system_message,
    human_template="{question}",
    llm=ChatOpenAI(model="gpt-4o-mini", temperature=0),
    output_parser=StrOutputParser()
):

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", human_template),
    ])

    return chat_prompt | llm | output_parser