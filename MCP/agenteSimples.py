from praisonaiagents import Agent, MCP

agent = Agent(
    instructions="""You help book apartments on Airbnb.""",
    llm="ollama/gemma3:1b",
    tools = MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
)

agent.start("I want to book an apartment in Paris for 2 nights. 04/28 - 04/30 for 2 adults")
