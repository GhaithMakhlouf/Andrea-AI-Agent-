import os
from typing import List, Optional
from pydantic import BaseModel
import openai

class Task(BaseModel):
    id: int
    description: str
    status: str = "pending"
    result: Optional[str] = None

class AndreaAgent:
    """
    Andrea is an advanced AI Agent designed for autonomous task orchestration.
    She can decompose complex goals into smaller, executable sub-tasks.
    """
    def __init__(self, name: str = "Andrea", model: str = "gpt-4o"):
        self.name = name
        self.model = model
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.task_list: List[Task] = []

    def plan(self, goal: str):
        print(f"[{self.name}] Planning for goal: {goal}")
        prompt = f"Decompose the following goal into 3 concrete sub-tasks: {goal}. Return only a JSON list of descriptions."
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Simulating JSON parsing for brevity
        descriptions = ["Research the topic", "Analyze findings", "Generate report"]
        self.task_list = [Task(id=i, description=desc) for i, desc in enumerate(descriptions)]
        print(f"[{self.name}] Created {len(self.task_list)} tasks.")

    def execute_next(self) -> Optional[str]:
        for task in self.task_list:
            if task.status == "pending":
                print(f"[{self.name}] Executing Task {task.id}: {task.description}")
                task.status = "completed"
                task.result = f"Success: {task.description} completed."
                return task.result
        return None