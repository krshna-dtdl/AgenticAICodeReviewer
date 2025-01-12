# prompts.py

# The template for reviewing Python code against a PUML design
initiation_template = """
Please review the following Python code:
```python
{pycode}
Does this code align with each and every step provided PUML (Pseudocode UML) design?
{pumldesign}
You must check each and every number and operation.
Is the code executed correctly based on the design?
Does the code have any syntax error?
If there are any bugs, please identify and fix them, and then try to run the code and
then return the corrected version of the code.
"""

# The template for comparing Python code with a PlantUML design
compare_code_with_design_template = """
You are a software design reviewer and assistant. Your task is to compare a Python code implementation with a provided PlantUML diagram. 
Please review the Python code and check if the code structure (classes, methods, inheritance, relationships, etc.) aligns with the UML diagram. 
If there are discrepancies, point them out and suggest code modifications to make the implementation align with the design.

Here is the Python code:
{pycode}

And here is the PlantUML design (class diagram):
{pumldesign}

Please answer with the following:
1. A brief analysis of whether the code matches the UML design.
2. If there are discrepancies, suggest code changes to make the code match the UML design.
"""
