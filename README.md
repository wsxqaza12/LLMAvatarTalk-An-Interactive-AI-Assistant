<div align="center">

<h1>LLMAvatarTalk: An Interactive AI Assistant</h1>
LLMAvatarTalk is an innovative project that combines state-of-the-art AI technologies to create an interactive virtual assistant. By integrating automatic speech recognition (ASR), large language models (LLM), LangChain, text-to-speech (TTS), audio-driven facial animation (Audio2Face), and Unreal Engine's Metahuman, LLMAvatarTalk showcases the potential of AI in achieving seamless and engaging human-computer interaction
<br><br>

**English** | [**中文**](./docs/CN/README.md) 

</div>

## Demo
Click the thumbnail below to watch the demo on YouTube:
[![Watch the video](./images/DemoCover.jpg)](https://www.youtube.com/watch?v=G17fgkN3e0w)

## Features
- **Speech Recognition**: Converts user speech into text in real-time using NVIDIA RIVA ASR technology.
- **Language Processing**: Leverages advanced LLM (such as llama3-70b-instruct) via NVIDIA NIM APIs for deep semantic understanding and response generation.
- **Text-to-Speech**: Transforms generated text responses into natural-sounding speech using NVIDIA RIVA TTS.
- **Facial Animation**: Generates realistic facial expressions and animations based on audio output using Audio2Face technology.
- **Unreal Engine Integration**: Enhances virtual character expressiveness by real-time linking Audio2Face with Unreal Engine's Metahuman.
- **LangChain Integration**: Simplifies the integration of NVIDIA RIVA and NVIDIA NIM APIs, providing a seamless and efficient workflow for AI development.

## Architecture
<img src="https://github.com/wsxqaza12/LLMAvatarTalk-An-Interactive-AI-Assistant/blob/main/images/architecture%20diagram.png" width="650" />

## Prerequisites
- NVIDIA NIMs API KEY
  - Apply for free 1000 credits at [NVIDIA NIMs](https://build.nvidia.com/explore/discover?signin=false&signin_corporate=false)
- Nvidia Riva Server
  - [RIVA Step-by-step Tutorial](./docs/RIVA/RIVA_Tutorial.md)
- Audio2Face
  - [Audio2Face Step-by-step Tutorial](./docs/Audio2Face/Audio2Face_Tutorial.md)
- Unreal Engine & Metahuman
  - [Unreal Engine & Metahuman Step-by-step Tutorial](./docs/UE/UE_Tutorial.md)

## Installation
Tested Environment: Windows 11 & Python 3.9

```plaintext
git clone https://github.com/yourusername/LLMAvatarTalk.git
cd LLMAvatarTalk
pip install -r requirements.txt
```

## Execution
1. Ensure you have set up the Riva server and configured Audio2Face and Unreal Engine.
2. Create a `.env` file and input the NVIDIA NIMs API KEY. You can find a sample in .env.sample.
   ```plaintext
   NVIDIA_API_KEY=nvapi-
   ```
3. Input the Riva server's IP into the URI field in `config.py`. The default port for Riva servers is "50051".
   ```plaintext
   URI = '192.168.1.205:50051'
   ```
4. In the `config.py` file, you can also specify the language for the application interface and responses. The available options are 'en-US' for English and 'zh-CN' for Chinese. The default language is set to English.
   ```plaintext
   LANGUAGE = 'en-US'  # Change to 'zh-CN' for Chinese.
   ```
5. Run `python main.py`

## To-Do List
- [ ] Optimize LLM functionality, including adding RAG and Agent
- [ ] Improve TTS
- [ ] Implement emotion detection and full-body animation
- [ ] Integrate asynchronous processing
- [ ] Integration with LangChain (RIVA's ASR and TTS), currently using a temporary alternative
## Acknowledgments
Special thanks to the following projects and documentation:

### RIVA:
  - [NVIDIA CLI Install](https://org.ngc.nvidia.com/setup/installers/cli)
  - [Developing the Next Generation of Extended Reality Applications with Speech AI](https://developer.nvidia.com/blog/developing-the-next-generation-of-extended-reality-applications-with-speech-ai/)
  - [NVIDIA RIVA ASR Overview](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/asr/asr-overview.html)
  - [NVIDIA RIVA TTS Overview](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/tts/tts-overview.html)

### Audio2Face:
  - [Streaming Audio Player](https://docs.omniverse.nvidia.com/audio2face/latest/user-manual/audio2face-tool/streaming-audio-player.html)
  - [Audio2Face to UE Live Link Plugin](https://docs.omniverse.nvidia.com/audio2face/latest/user-manual/livelink-ue-plugin.html)

### LangChain
  - [LangChain Integrates NVIDIA NIM for GPU-optimized LLM Inference in RAG](https://blog.langchain.dev/nvidia-nim/)
  - [NVIDIA NIMs](https://python.langchain.com/v0.2/docs/integrations/chat/nvidia_ai_endpoints/)
  - [NVIDIA Riva: ASR and TTS](https://python.langchain.com/v0.1/docs/integrations/tools/nvidia_riva/)
  
### Projects
- [Omniverse-Virtual-Assisstant](https://github.com/zslrmhb/Omniverse-Virtual-Assisstant)
