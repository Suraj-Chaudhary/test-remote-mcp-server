from fastmcp import FastMCP
import random
import json

# Create the FastMCP server instance
mcp = FastMCP("Simple Calculator Server")

# Tool: Add two numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b

# Tool: Generate a random number
@mcp.tool()
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Generate a random number between min_val and max_val.
    
    Args:
        min_val (int): The minimum value (inclusive).
        max_val (int): The maximum value (inclusive).
    
    Returns:
        int: A random number between min_val and max_val.
    """
    return random.randint(min_val, max_val)

# Resource: Server information
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Suraj Chaudhary"
    }
    return json.dumps(info)

# Start the FastMCP server
if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=3001)