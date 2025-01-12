from dotenv import load_dotenv
from agent_executor.agent import AgentExecutorFactory
from langchain.prompts.prompt import PromptTemplate

from prompts import initiation_template

load_dotenv()

def main():
    python_code_url = 'http://raw.githubusercontent.com/krshna-dtdl/DeutscheTelekomDigitalLabsBlog/refs/heads/main/Code.py'
    puml2_url = 'http://raw.githubusercontent.com/krshna-dtdl/DeutscheTelekomDigitalLabsBlog/refs/heads/main/SecondDesign.puml'

    prompt = PromptTemplate(input_variables=['pycode', 'pumldesign'], template=initiation_template)

    agent_factory = AgentExecutorFactory()
    agent_executor = agent_factory.create_agent_executor()

    result = agent_executor.invoke(
        input={"input": prompt.format_prompt(pycode=python_code_url, pumldesign=puml2_url)}
    )
    print(result['output'])


if __name__ == "__main__":
    main()
