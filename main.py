# Running the Demo
from modules.asr import ASRService
from modules.llm import LLMService
from modules.tts import TTSService
from modules.audio2face import Audio2FaceService
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
