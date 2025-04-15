from praisonaiagents import Agent, MCP

agent = Agent(
    instructions="""You are a helpful assistant that can check stock prices and perform other tasks.
    Use the available tools when relevant to answer user questions.""",
    llm="ollama/gemma3:1b",
    tools = MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
)

# NOTE: Python Path replace with yours: /Users/praison/miniconda3/envs/mcp/bin/python
# NOTE: custom-python-server.py file path, replace it with yours: /Users/praison/stockprice/custom-python-server.py

agent.start("What is the stock price of Tesla?")
