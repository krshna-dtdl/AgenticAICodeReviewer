import subprocess

from langchain_core.tools import tool


@tool
def execute_code(code: str) -> str:
    """Executes a code snippet and returns stdout or error output."""
    try:
        codeoutput = subprocess.run(
            ["python3", "-c", code],
            capture_output=True,
            text=True
        )
        if codeoutput.returncode == 0:
            return f"Code has no exceptions: {codeoutput.stdout}"
        else:
            return f"Code have exceptions: {codeoutput.stderr}"
    except Exception as e:
        return f"Execution failed: {str(e)}"
