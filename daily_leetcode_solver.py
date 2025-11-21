from dotenv import load_dotenv
import os
from openai import OpenAI
import requests
import json
load_dotenv()
# ---------------------------
# 1. FETCH LEETCODE DAILY PROBLEM
# ---------------------------

def fetch_daily_problem():
    url = "https://leetcode.com/graphql"
    query = """
    query questionOfToday {
      activeDailyCodingChallengeQuestion {
        date
        link
        question {
          questionId
          title
          content
          difficulty
          codeSnippets {
            lang
            code
          }
        }
      }
    }
    """

    response = requests.post(url, json={"query": query})
    data = response.json()

    q = data["data"]["activeDailyCodingChallengeQuestion"]

    problem_title = q["question"]["title"]
    problem_content = q["question"]["content"]
    difficulty = q["question"]["difficulty"]
    link = "https://leetcode.com" + q["link"]

    return {
        "title": problem_title,
        "content": problem_content,
        "difficulty": difficulty,
        "link": link
    }



# ---------------------------
# 2. SOLVE USING GPT
# ---------------------------


def solve_problem(problem):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
You are a competitive programming expert.

Solve the following LeetCode daily challenge:

### Title
{problem['title']}

### Difficulty
{problem['difficulty']}

### Problem
{problem['content']}

### Requirements
1. Give a short summary.
2. Explain constraints & edge cases.
3. Provide the optimal algorithm.
4. Give a clean C++ solution.
5. Explain one example.
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    # FIX: use .content instead of ["content"]
    return response.choices[0].message.content


# ---------------------------
# 3. MAIN FLOW
# ---------------------------

def main():
    print("--- Fetching Daily LeetCode Problem ---")
    problem = fetch_daily_problem()

    print(f"Today's Problem: {problem['title']} ({problem['difficulty']})")
    print("Link:", problem["link"])

    print("\n--- Solving... ---")
    solution = solve_problem(problem)
    
    # Save solution daily
    save_path = "leet.txt"  # <-- your required path

    with open(save_path, "w", encoding="utf-8") as f:
        # f.write(f"# {problem['title']}\n")
        # f.write(f"**Difficulty:** {problem['difficulty']}\n")
        # f.write(f"**Link:** {problem['link']}\n\n")
        f.write(solution)

    print("\nSolution saved to:", save_path)


if __name__ == "__main__":
    main()
