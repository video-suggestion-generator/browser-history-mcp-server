from os.path import expandvars
from sqlite3 import Connection, Cursor, connect

from fastmcp import FastMCP

from utils.time import get_webkit_timestamp_n_days_ago


BRAVE_HISTORY_PATH: str = expandvars("%LocalAppData%/BraveSoftware/Brave-Browser/User Data/Default/History")
BRAVE_HISTORY_READ_ONLY_IMMUTABLE_URI: str = "file:" + BRAVE_HISTORY_PATH + "?mode=ro&immutable=1"

mcp: FastMCP = FastMCP()

@mcp.tool
def get_search_history_for_last_n_days(days: int) -> list[str]:
    connection: Connection = connect(BRAVE_HISTORY_READ_ONLY_IMMUTABLE_URI, uri=True)
    cursor: Cursor = connection.cursor()
    rows: list[tuple[str]] = cursor.execute(f"SELECT DISTINCT title FROM urls WHERE last_visit_time > {get_webkit_timestamp_n_days_ago(days)}").fetchall()
    search_history: list[str] = [row[0] for row in rows]
    connection.close()
    return search_history

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )
