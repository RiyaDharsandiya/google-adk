def calculator_tool(expression: str) -> str:
    """
    Evaluates a basic mathematical expression and returns the result as a string.
    Supports addition, subtraction, multiplication, division, exponents, and parentheses.
    Example: "2 * (3 + 4) / 7"
    """
    import math

    # Security: Only allow safe characters (digits, operators, parentheses, decimal points, whitespace)
    allowed_chars = "0123456789+-*/().e E"
    if not all(char in allowed_chars for char in expression):
        return "Error: Invalid characters in expression."

    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt, "pow": math.pow, "abs": abs, "round": round})
        return str(result)
    except Exception as e:
        return f"Error: Could not evaluate expression ({str(e)})"