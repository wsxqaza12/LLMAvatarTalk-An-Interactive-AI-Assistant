# Running the Demo

from asr import ASRService
from llm import LLMService
from tts import TTSService
from audio2face import Audio2FaceService
from langchain_core.prompts import PromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA


asr_service = ASRService()
llm_service = LLMService()
tts_service = TTSService()
audio2face_service = Audio2FaceService()

while True:
    # speech recognition
    asr_service.run()
    print(asr_service.transcript)

    # llm chat
    response_chunks = llm_service.invoke_conversation(asr_service.transcript)
    print(response_chunks)

    for response_chunk in response_chunks:
        # text-to-speech
        audio_bytes = tts_service.get_audio_bytes(response_chunk)

        # Audio2Face Animation
        audio2face_service.make_avatar_speaks(audio_bytes)
