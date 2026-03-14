# 🤖 Andrea- (AI Agent Framework)

[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-orange)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Andrea-** is a lightweight yet powerful AI Agent framework designed for autonomous task planning and execution. Built with OpenAI's gpt-4o, Andrea can take a high-level goal, decompose it into actionable tasks, and execute them sequentially.

## 🚀 Features
- **Autonomous Planning:** Automatically breaks down complex goals into sub-tasks.
- **Sequential Execution:** Executes tasks one-by-one with state management.
- **Rich Interface:** Uses ich for professional terminal output.
- **Type Safety:** Built with pydantic for robust data handling.

## 🛠️ Installation

`ash
git clone https://github.com/GhaithMakhlouf/Andrea-.git
cd Andrea-
pip install -r requirements.txt
`

## 🚀 Quick Start

1. **Set your API Key:**
`ash
export OPENAI_API_KEY="your-api-key"
`

2. **Run the Agent:**
`ash
python main.py
`

## 🏗️ Architecture
Andrea uses a **Plan-then-Execute** pattern:
1. **The Planner:** Uses LLM reasoning to identify dependencies and steps.
2. **The Executor:** Iterates through the task list, updating status and storing results.

---
**Recoded with AI expertise by [Ghaith Makhlouf](https://www.linkedin.com/in/ghaith-makhlouf)**