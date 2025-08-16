import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found! Please add GEMINI_API_KEY to your .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

# Use correct Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def aiops_assistant(query: str) -> str:
    prompt = f"""
    You are an AIOps assistant specialized in DevOps.
    Always return working code/scripts in the correct format.
    Examples include:
    - Terraform IaC
    - Kubernetes YAML
    - CI/CD pipeline scripts
    - Dockerfiles
    - Ansible playbooks

    My request: {query}
    """
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("🤖 AIOps Assistant is ready! Type 'exit' to quit.\n")
    while True:
        query = input("Ask AIOps Assistant: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break
        try:
            answer = aiops_assistant(query)
            print("\n" + "="*50)
            print(answer)
            print("="*50 + "\n")
        except Exception as e:
            print(f"❌ Error: {e}")
