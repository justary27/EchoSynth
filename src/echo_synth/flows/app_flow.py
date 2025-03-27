import os
import traceback
from typing import List
from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start
from crewai.tasks import TaskOutput

from echo_synth.crews import AudioProcessingCrew, EmailSendingCrew


class EchoSynthState(BaseModel):
    
    transcribed_text: str = ""
    image_file: str = ""
    speech_text: str = ""
    summary_text: str = ""
    summary_for_image: str = ""
    
    email_sent: bool = False


class EchoSynthFlow(Flow[EchoSynthState]):

    def __init__(self, audio_file_path=None):
        """Initialize the flow with optional parameters"""
        super().__init__()
        self.audio_file_path = audio_file_path
    
    @start()
    def process_audio(self) -> None:
        """
        Process an audio file using the AudioProcessingCrew.
        
        Args:
            state: The current state of the flow
            audio_file_path: Path to the audio file to process
            openai_api_key: OpenAI API key for Whisper and DALL-E
            
        Returns:
            Updated state with transcription, speech, summary and image
        """
        try:
            print("=== STARTING PROCESS_AUDIO ===")
            
            audio_crew = AudioProcessingCrew().crew()
            
            # Set up context for the first task
            initial_context = {
                "audio_file_path": os.path.abspath(self.audio_file_path)
            }
                        
            # Run the crew with the initial context
            results = audio_crew.kickoff(inputs=initial_context).tasks_output
            
            # Extract task outputs by task ID
            self.state.transcribed_text = self._get_task_output_by_name(results, "convert_audio_to_text")
            self.state.speech_text = self._get_task_output_by_name(results, "write_speech")
            self.state.summary_text = self._get_task_output_by_name(results, "write_summary")
            self.state.summary_for_image = self._get_task_output_by_name(results, "write_image_summary")
            self.state.image_file = self._get_task_output_by_name(results, "create_image")
            
            print("=== AUDIO PROCESSING COMPLETE ===")
            print(f"State after processing: {self.state}")
            
        except Exception as e:
            print(f"Error in process_audio: {e}")
            print(traceback.format_exc())
            raise

    @listen(process_audio)
    def send_email(self) -> None:
        print("Sending email with results...")

    @listen(send_email)
    def show_results(self) -> None:
        # Print summary of results
        print("\n--- EchoSynth Flow Complete ---")
        print(f"Audio processed: {self.audio_file_path}")
        print(f"Transcription length: {len(self.state.transcribed_text)} characters")
        print(f"Speech length: {len(self.state.speech_text)} characters")
        print(f"Summary length: {len(self.state.summary_text)} characters")
        print(f"Image generated: {'Yes' if self.state.image_file else 'No'}")
        print(f"Email sent: {'Yes' if self.state.email_sent else 'No'}")

    def _get_task_output_by_name(self, tasks_output: List[TaskOutput], task_name):
        """
        Helper method to extract output from a specific task by ID
        
        Args:
            task_outputs: List of TaskOutput objects
            task_id: ID of the task to find
            
        Returns:
            The output of the task or empty string if not found
        """
        for task_output in tasks_output:
            if hasattr(task_output, 'name') and task_output.name == task_name:
                return task_output.raw
                
        print(f"No task output found with name: {task_name}")
        return ""
