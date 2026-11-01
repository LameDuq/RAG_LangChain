from dotenv import load_dotenv
import os

load_dotenv()


def main() -> None:
    print("Hello from rag-langchain!")
    print(os.environ.get("ANTHROPIC_API_KEY"))


if __name__ == "__main__":
    main()
