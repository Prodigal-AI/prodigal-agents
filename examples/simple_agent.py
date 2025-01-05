from prodigal_agents.core.agent import Agent, AgentConfig

config = AgentConfig(name="SimpleAgent", model="gpt-4")
agent = Agent(config)

response = agent.run("Tell me a story about teamwork.")
print(response)