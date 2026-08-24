CALCULATOR_TOOLS = [{
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Calculate a mathematical expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Mathematical expression to calculate."
                }
            },
            "required": ["expression"],
            "additionalProperties": False,
        },
    },
}
]

CALCULATOR_TOOLS_RESPONSES = [
    {
        "type": "function",
        "name": "calculate",
        "description": "Calculate a mathematical expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Mathematical expression to calculate."
                }
            },
            "required": ["expression"],
            "additionalProperties": False
        },
        "strict": True
    }
]