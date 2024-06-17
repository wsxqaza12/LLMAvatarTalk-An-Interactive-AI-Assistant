# speech to Audio2Face module utilizing the gRPC protocal from audio2face_streaming_utils

import riva.client
import io
import numpy as np
from pydub import AudioSegment
from scipy.io.wavfile import read
from modules.audio2face_streaming_utils import push_audio_track


class Audio2FaceService:
    def __init__(self, sample_rate=44100):
        """
        :param sample_rate: sample rate
        """
        self.a2f_url = 'localhost:50051'   # Set it to the port of your local host
        self.sample_rate = 44100
        # Set it to the name of your Audio2Face Streaming Instance
        self.avatar_instance = '/World/audio2face/PlayerStreaming'

    def tts_to_wav(self, tts_byte, framerate=22050) -> str:
        """
        :param tts_byte: tts data in byte
        :param framerate: framerate
        :return: wav byte
        """
        seg = AudioSegment.from_raw(io.BytesIO(
            tts_byte), sample_width=2, frame_rate=22050, channels=1)
        wavIO = io.BytesIO()
        seg.export(wavIO, format="wav")
        rate, wav = read(io.BytesIO(wavIO.getvalue()))
        return wav

    def wav_to_numpy_float32(self, wav_byte) -> float:
        """
        :param wav_byte: wav byte
        :return: float32
        """
        return wav_byte.astype(np.float32, order='C') / 32768.0

    def get_tts_numpy_audio(self, audio) -> float:
        """
        :param audio: audio from tts_to_wav
        :return: float32 of the audio
        """
        wav_byte = self.tts_to_wav(audio)
        return self.wav_to_numpy_float32(wav_byte)

    def make_avatar_speaks(self, audio) -> None:
        """
        :param audio: tts audio
        :return: None
        """
        push_audio_track(self.a2f_url, self.get_tts_numpy_audio(
            audio), self.sample_rate, self.avatar_instance)
