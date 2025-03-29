# EchoSynth 🎙️➡️📝🖼️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Powered-green.svg)](https://github.com/joaomdmoura/crewai)

EchoSynth transforms audio content into refined text and visual assets through a coordinated team of AI agents. It's designed for podcasters, content creators, educators, and anyone working with spoken media who wants to automatically generate high-quality derivative content.

## 🌟 Features

- **Audio Transcription** - Accurate text conversion from various audio formats
- **Speech Refinement** - Transforms raw transcripts into polished speeches
- **Smart Summarization** - Creates concise text summaries capturing key points
- **Image Generation** - Produces relevant visuals that match content themes
- **Coordinated AI Agents** - Specialized AI agents working together via CrewAI
- **Flexible Pipeline** - Modular architecture that supports customization
- **JSON Output** - Saves all generated content in structured JSON format

## 🛠️ Tech Stack

- **[CrewAI](https://github.com/joaomdmoura/crewai)** - Agent orchestration framework
- **[OpenAI Whisper](https://openai.com/research/whisper)** - Speech-to-text transcription
- **[OpenAI GPT-4o](https://openai.com/gpt-4)** - Text processing and refinement
- **[OpenAI DALL-E 3](https://openai.com/dall-e-3)** - Image generation
- **Python 3.9+** - Core programming language

## 📋 Prerequisites

- Python 3.9 or higher
- OpenAI API key with access to Whisper, GPT-4, and DALL-E models
- Audio files (.mp3, .mp4, .mpeg, .mpga, .m4a, .wav, or .webm)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/EchoSynth.git
   cd EchoSynth
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```

## 💻 Usage

### Basic Example

```python
from echo_synth.flows import EchoSynthFlow

# Initialize the flow with your audio file
flow = EchoSynthFlow(audio_file_path="data/your_audio_file.mp3")

# Run the processing pipeline
flow.run()

# Access the results
transcription = flow.state.transcribed_text
speech = flow.state.speech_text
summary = flow.state.summary_text
image_path = flow.state.image_file
results_json = flow.state.results_json

print(f"Processed {flow.audio_file_path}")
print(f"Generated image saved to: {image_path}")
print(f"Results JSON saved to: {results_json}")
```

### Using Environment Variables

You can also set the audio file path via environment variables:

```bash
export AUDIO_FILE_PATH="data/your_audio_file.mp3"
```

```python
from echo_synth.flows import EchoSynthFlow

# The audio path will be read from environment variables
flow = EchoSynthFlow()
flow.run()
```

## 🧠 Architecture

![EchoSynth Architecture](https://github.com/user-attachments/assets/ee64e336-69b0-4d20-8878-1630cc4b9c13)

EchoSynth uses a multi-agent architecture powered by CrewAI:

1. **Agent 1 (Text Transcribe)** - Converts audio to accurate text using Whisper API
2. **Agent 2 (Speech Writer)** - Refines raw transcripts into polished, structured speech
3. **Agent 3 (Summary for Image)** - Creates descriptive content for image generation
4. **Agent 4 (Summarizer)** - Produces concise summaries of the key content
5. **Agent 5 (Generate Image)** - Creates visual representations using DALL-E
6. **Agent 6 (Save data to JSON)** - Compiles all outputs into a structured JSON file

The flow is coordinated through CrewAI's sequential pipeline, ensuring each agent receives the proper inputs from previous steps and all results are saved in a structured format.

### Tools Used by Agents:

- **Tool 1 (Whisper STT)** - Used by Agent 1 for transcription
- **Tool 2 (Sentiment Analysis)** - Used by Agent 1 for audio content analysis
- **Tool 3 (DALL-E)** - Used by Agent 5 for image generation
- **Tool 4 (FileWriter)** - Used by Agent 6 to save outputs to JSON

## 🔍 Troubleshooting

### Common Issues:

#### Audio File Not Found
Ensure your audio file exists and the path is correct. EchoSynth will search in:
- The absolute path provided
- The current working directory
- A `data/` subdirectory in the working directory

#### API Key Issues
Make sure your OPENAI_API_KEY environment variable is correctly set and has access to the required models.

#### File Size Limits
OpenAI's Whisper API has a 25MB file size limit. For larger files, consider splitting them or using a different method.

#### JSON Output
If you encounter issues with JSON output:
- Check that all agent outputs are valid and complete
- Ensure the FileWriter tool has proper permissions to write to the output directory
- Verify the JSON structure matches your expected schema

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
