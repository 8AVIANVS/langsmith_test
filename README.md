# LangChain Test Project

This project demonstrates the usage of LangChain with OpenAI and LangSmith tracing capabilities.

## Environment Setup

Create a `.env` file in the root directory with the following variables:

```env
# LangSmith Configuration
LANGSMITH_TRACING=true              # Enable LangSmith tracing
LANGSMITH_ENDPOINT=https://api.smith.langchain.com  # LangSmith API endpoint
LANGSMITH_API_KEY=<your-langsmith-api-key>         # Get this from LangSmith dashboard
LANGSMITH_PROJECT=langsmith-quickstart              # Your project name

# OpenAI Configuration
OPENAI_API_KEY=<your-openai-api-key>              # Get this from OpenAI platform
```

### How to Get API Keys

1. **LangSmith API Key**:
   - Visit [LangSmith](https://smith.langchain.com/)
   - Create an account or sign in
   - Go to your settings to find your API key

2. **OpenAI API Key**:
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Create an account or sign in
   - Go to API settings to create an API key

## Running the Project

1. Install dependencies (if you haven't already):
   ```bash
   pip install langchain langchain-openai python-dotenv
   ```

2. Make sure your `.env` file is set up with the required API keys

3. Run the main script:
   ```bash
   python main.py
   ```
