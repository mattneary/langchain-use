import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from langchain import OpenAI
from langfn import use_prompt, use_llm

@use_llm(OpenAI())
@use_prompt
def assign_to(task):
    return f'''
        Determine whether the listed task should be assigned to Human Secretary or Computer Algorithm.

        Task: Summarize this report.
        Assign to: Human Secretary

        Task: Compute total profit and loss.
        Assign to: Computer Algorithm

        Task: {task}
        Assign to:
    '''.strip()

print(assign_to.predict(task='Fold laundry'))
