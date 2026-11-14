from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-tools")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Do numbers ka jama (sum) nikalta hai."""
    return a + b

if __name__ == "__main__":
    mcp.run()