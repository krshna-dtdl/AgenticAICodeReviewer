from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools import code_executor, url_fetcher
from design_comparison.design_checker import compare_code_with_design_and_fix


class AgentExecutorFactory:
    def __init__(self, model_name="gpt-4o-mini", temperature=1):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

    def create_agent_executor(self):
        tools_for_agent = [code_executor.execute_code, url_fetcher.fetch_url_content, compare_code_with_design_and_fix]
        react_prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm=self.llm, tools=tools_for_agent, prompt=react_prompt)
        return AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
