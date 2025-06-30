import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv[1:])==0:
    print("Usage: python3 main.py <prompt>")
    # sys.exit(1) = abnormal termination   (0) would be normal
    sys.exit(1)



def main():
    try:
        input = sys.argv[1:]
    except Exception as e:
        print("Usage: python3 main.py <prompt>")
        # sys.exit(1) = abnormal termination   (0) would be normal
        sys.exit(1) 


    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=input
    )
    print(response.text)
    print("---------------")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")











if __name__ == "__main__":
    main()