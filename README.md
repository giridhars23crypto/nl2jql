# nl2jql

A tiny utility that turns natural language descriptions of Jira filters into Jira Query Language (JQL) using an OpenAI language model.

## Usage

1. Install dependencies:
   ```bash
   pip install openai
   ```
2. Set your `OPENAI_API_KEY` environment variable.
3. Run the translator:
   ```bash
   python nl2jql.py "issues assigned to me that are not done"
   ```

## Development

Run tests with:
```bash
pytest
```
