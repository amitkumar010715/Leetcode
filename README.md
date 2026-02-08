# 🚀 LeetCode Problem Solver Automation

An end-to-end **agentic AI system** that automatically fetches LeetCode problems, generates optimized solutions using a **multi-LLM collaborative pipeline**, submits them on schedule, and notifies the user via email.

---

## 🔥 Features

* 📥 **Automated Problem Retrieval** – Fetches daily/targeted LeetCode problems using the **LeetCode GraphQL API**
* 🤖 **Multi-Agent LLM Reasoning** – Uses the **AutoGen framework** with GPT & Google Gemini models for enhanced solution quality
* ⏱ **Scheduled Submissions** – YAML-based CI/CD workflow for timed execution and auto-submission
* 📧 **Email Notifications** – Sends solution reports and submission status
* ⚙ **Fully Autonomous Workflow** – Zero manual intervention once configured
* 🧩 Modular & Extensible – Easy to plug additional models or strategies

---

## 🧠 Architecture Overview

1. **Fetcher Agent** – Retrieves problem metadata & description from LeetCode via GraphQL
2. **Reasoning Agents** – Multiple LLM agents collaborate to generate and refine solutions
3. **Evaluator Agent** – Validates complexity, edge cases, and formatting
4. **Submitter Agent** – Automatically submits solution to LeetCode
5. **Notifier Service** – Emails final solution and status

---

## 🛠 Tech Stack

* **Framework:** AutoGen
* **LLMs:** OpenAI GPT, Google Gemini
* **API:** LeetCode GraphQL
* **Automation:** YAML CI/CD workflows
* **Backend:** Python
* **Notifications:** SMTP / Email service

---

## 🚀 Setup

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd leetcode-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create `.env`:

```env
OPENAI_API_KEY=
GEMINI_API_KEY=
LEETCODE_SESSION=
EMAIL_USER=
EMAIL_PASS=
```

### 4. Run Locally

```bash
python main.py
```

---

## ⏱ YAML Scheduler Example

```yaml
name: leetcode-agent

on:
  schedule:
    - cron: "0 9 * * *"

jobs:
  solve:
    runs-on: ubuntu-latest
    steps:
      - run: python main.py
```

---

## 📩 Output

* Auto-submitted solution on LeetCode
* Email containing:

  * Problem link
  * Generated solution
  * Complexity analysis
  * Submission status

---

## 📌 Roadmap

* [ ] Add multi-language solution support
* [ ] Reinforcement feedback from submissions
* [ ] Difficulty-based agent strategy
* [ ] Web dashboard

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

MIT License
