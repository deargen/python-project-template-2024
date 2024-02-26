from dotenv import load_dotenv

load_dotenv()

from mlproject import health

if __name__ == "__main__":
    health.main()
