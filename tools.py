from dotenv import load_dotenv
load_dotenv()
import os

# SerperDevTool This tool is designed to perform a semantic search for a specified query from a text's content across the internet.
# It utilizes the serper.dev API to fetch and display the most relevant search results based on the query provided by the user.
os.environ['SERPER_API_KEY'] = os.getenv("serper_api_key")

from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()