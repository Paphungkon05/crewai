import os

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

MODEL = os.getenv("MODEL", "ollama/llama3")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")


def build_llm() -> LLM:
    """Build the LLM based on the MODEL env var.

    - If MODEL starts with "ollama/", force the local Ollama base_url.
    - Otherwise (e.g. "gemini/..."), let LiteLLM/crewai resolve the provider
      using GOOGLE_API_KEY / GEMINI_API_KEY from the environment.
    """
    if MODEL.startswith("ollama/"):
        return LLM(
            model=MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0.3,
        )
    return LLM(
        model=MODEL,
        temperature=0.3,
    )


llm = build_llm()


@CrewBase
class CareerPlanAgentsClassic:
    """Career Plan Agents crew (Classic / YAML)."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def career_profile_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["career_profile_analyst"],
            llm=llm,
            verbose=True,
        )

    @agent
    def qualification_gap_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["qualification_gap_analyst"],
            llm=llm,
            verbose=True,
        )

    @agent
    def development_plan_designer(self) -> Agent:
        return Agent(
            config=self.agents_config["development_plan_designer"],
            llm=llm,
            verbose=True,
        )

    @agent
    def self_assessment_coach(self) -> Agent:
        return Agent(
            config=self.agents_config["self_assessment_coach"],
            llm=llm,
            verbose=True,
        )

    @task
    def analyze_profile_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_profile_task"],
        )

    @task
    def analyze_gap_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_gap_task"],
        )

    @task
    def create_development_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_development_plan_task"],
        )

    @task
    def write_final_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_final_report_task"],
            output_file="output/career_plan_report.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
