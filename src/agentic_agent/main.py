# agentic_agent/src/agentic_agent/main.py

#!/usr/bin/env python
import os
import warnings
from datetime import datetime

from agentic_agent.crew import AgenticAgent

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the Agentic AI crew to research and report on Agentic AI tutorials.
    """
    inputs = {
        'current_year': '2025',
        'question': 'comprehensive agentic ai list',
    }

    # Create and run the crew, passing inputs
    result = AgenticAgent().crew().kickoff(inputs=inputs)

    # Print the raw output
    print("\n\n=== FINAL AGENTIC AI TUTORIALS REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/spiritual_growth_consciousness_development_course_blueprint_and_content_guide.md")

if __name__ == "__main__":
    run()
