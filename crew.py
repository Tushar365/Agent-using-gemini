from crewai import Crew,Process
from agents import web_researcher,script_writer
from tasks import web_research_task,script_writer_task

# forming the crew with some cofigurations 
crew = Crew(
    agents=[web_researcher,script_writer],
    tasks=[web_research_task,script_writer_task],
    process=Process.sequential,
)

# starting the task execution process with enhanced feedback

# Starting the task execution process with enhanced feedback
input_data = {'topic': 'Rabindranath tagore in bengali literatures'}

try:
    # Execute the tasks sequentially
    result = crew.kickoff(input_data)  # Updated method call

    # Print the results of the task execution
    print("Execution Result:")
    print(result)

except Exception as e:
    # Handle any errors that occur during execution
    print("An error occurred during task execution:")
    print(e)