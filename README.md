# EchoSynth 🎙️➡️📝🖼️

## Repository Description
EchoSynth is an intelligent audio processing pipeline that transforms spoken content into polished text and visual representations using AI agents. Built with CrewAI, it seamlessly transcribes audio, refines speech content, generates summaries, and creates matching images—all orchestrated through an agent-based workflow architecture.

## Tags
`ai-agents`, `audio-processing`, `transcription`, `text-generation`, `image-generation`, `crewai`, `openai`, `whisper`, `dalle`, `agent-based-workflows`

---

# EchoSynth: AI-Powered Audio Processing Pipeline

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
- **Email Integration** - Optional email delivery of processed content

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

print(f"Processed {flow.audio_file_path}")
print(f"Generated image saved to: {image_path}")
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

EchoSynth uses a multi-agent architecture powered by CrewAI:

1. **Audio-to-Text Transcriber Agent** - Converts audio to accurate text using Whisper API
2. **Speech Writer Agent** - Refines raw transcripts into polished, structured speech
3. **Image Summary Writer Agent** - Creates descriptive content for image generation
4. **Summary Writer Agent** - Produces concise summaries of the key content
5. **Image Painter Agent** - Generates visual representations using DALL-E

The flow is coordinated through CrewAI's sequential pipeline, ensuring each agent receives the proper inputs from previous steps.

## 📁 Project Structure

```
EchoSynth/
├── configs/
│   ├── agents/           # Agent configuration YAML files
│   └── tasks/            # Task configuration YAML files
├── data/                 # Directory for audio files
├── src/
│   └── echo_synth/
│       ├── agents/       # Agent implementations
│       ├── crews/        # CrewAI crew definitions
│       ├── flows/        # Flow orchestration logic
│       └── tools/        # Custom tools (Whisper, DALL-E, etc.)
├── tests/                # Unit and integration tests
├── .env.example          # Example environment variables
├── LICENSE               # MIT License
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

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

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

