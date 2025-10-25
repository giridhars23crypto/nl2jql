import sys
from typing import Optional

try:
    from openai import OpenAI
except ImportError as exc:  # pragma: no cover - handled in tests via mock
    raise SystemExit("openai package is required: pip install openai") from exc


SYSTEM_PROMPT = (
    "You are an expert Jira assistant. "
    "Convert natural language descriptions of issue filters into Jira Query "
    "Language (JQL). Respond with only the JQL string and no explanation."
)


def to_jql(nl_query: str, *, client: Optional[OpenAI] = None, model: str = "gpt-4o-mini") -> str:
    """Translate a natural language query into Jira Query Language using an LLM."""
    if client is None:
        client = OpenAI()

    user_prompt = (
        "Convert the following natural language description into a JQL query:\n\n"
        f"{nl_query}"
    )

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,
    )
    return completion.choices[0].message.content.strip()


def main(argv: list[str]) -> int:
    if not argv:
        print("Usage: python nl2jql.py <natural language query>")
        return 1
    nl_query = " ".join(argv)
    print(to_jql(nl_query))
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main(sys.argv[1:]))
