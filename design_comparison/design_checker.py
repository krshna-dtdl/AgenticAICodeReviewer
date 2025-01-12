from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

from prompts import compare_code_with_design_template


@tool
def compare_code_with_design_and_fix(input_data: dict) -> str:
    """
    This tool compares Python code to a PlantUML design and checks if the implementation
    aligns with the design. If there are discrepancies, the tool also suggests fixes
    to make the code conform to the design.

    Args:
    - input_data (dict): A dictionary containing 'pycode' and 'pumldesign'.

    Returns:
    - str: A detailed analysis of whether the code matches the design, along with any necessary code fixes.
    """
    pycode = input_data.get('pycode')
    pumldesign = input_data.get('pumldesign')

    if not pycode or not pumldesign:
        raise ValueError("Both 'pycode' and 'pumldesign' fields are required.")


    llm = ChatOpenAI(model="gpt-4o-mini", temperature=1)  # Use a deterministic response
    prompter = compare_code_with_design_template.format(pycode=pycode, pumldesign=pumldesign)
    response = llm(prompter)
    response_text = response.text  # Correct way to access the text of the response

    return response_text
