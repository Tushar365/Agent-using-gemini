from crewai import Task
from tools import tool
from agents import web_researcher,script_writer

web_research_task = Task(
    description = (
        "Identify the next big trend in {topic}. "
        "Focus on analyzing the pros and cons of this emerging trend, considering the broader narrative. "
        "Your final report should clearly articulate the key points, including market opportunities and potential risks associated with the trend. "
        "Ensure that your analysis is well-supported with credible sources and relevant data."
    ),
    expected_output="A comprehensive, three-paragraph report on {topic}, detailing the trend, its advantages and disadvantages, market opportunities, and potential risks.",
    tools=[tool],
    agent=web_researcher,
)
  
script_writer_task = Task(
    description = (
        "Compose an insightful and engaging YouTube script on {topic}. "
        "Focus on recent trends and their impact on the industry. "
        "The script should be easy to understand, engaging, and convey a positive perspective."
    ),
    expected_output="A well-crafted YouTube script for {topic}, ready for video production.",
    tools=[tool],
    agent=script_writer,
    async_execution=False,
    output_file='New_script1.md'
    )