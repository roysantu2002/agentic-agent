# agentic_agent/src/agentic_agent/crew.py

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Dict, Any
from crewai_tools import SerperDevTool
from crewai_tools import YoutubeChannelSearchTool


@CrewBase
class AgenticAgent:
    """AgenticAgent crew for researching and reporting Agentic AI tools"""

    agents: List[BaseAgent]
    tasks: List[Task]
    agents_config: Dict[str, Any]
    tasks_config: Dict[str, Any]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[
                YoutubeChannelSearchTool(),  # ✅ now directly a tool
                # CustomRAGSearchTool(pdf_path=pdf_path),  # ✅ now directly a tool
                SerperDevTool()  # optional: if you still want web search
            ]
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='output/full_stack_ai_enabled_developer_course.md'  # Match your YAML
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AgenticAgent crew with sequential execution"""
        return Crew(
            agents=self.agents,  # Auto-created by @agent
            tasks=self.tasks,    # Auto-created by @task
            process=Process.sequential,
            verbose=True,
        )
