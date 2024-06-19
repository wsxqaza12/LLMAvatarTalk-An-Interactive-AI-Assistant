# Audio to Speech Module utilizing the Riva SDK

import riva.client
import riva.client.audio_io
import riva.client.proto.riva_asr_pb2 as rasr
from typing import Iterable
from config import URI
from config import LANGUAGE


config = riva.client.StreamingRecognitionConfig(
    config=riva.client.RecognitionConfig(
        encoding=riva.client.AudioEncoding.LINEAR_PCM,
        language_code=LANGUAGE,
        max_alternatives=1,
        profanity_filter=False,
        enable_automatic_punctuation=True,
        verbatim_transcripts=True,
        sample_rate_hertz=16000
    ),
    interim_results=False,
)


class ASRService:
    def __init__(self):
        """
        """
        self.auth = riva.client.Auth(uri=URI)
        self.service = riva.client.ASRService(self.auth)
        self.sample_rate_hz = 16000
        self.file_streaming_chunk = 1600
        self.transcript = ""
        self.default_device_info = riva.client.audio_io.get_default_input_device_info()
        self.default_device_index = None if self.default_device_info is None else self.default_device_info[
            'index']

    def run(self) -> None:
        """
        :return: None
        """
        with riva.client.audio_io.MicrophoneStream(
                rate=self.sample_rate_hz,
                chunk=self.file_streaming_chunk,
                device=1,
        ) as audio_chunk_iterator:
            self.print_response(responses=self.service.streaming_response_generator(
                audio_chunks=audio_chunk_iterator,
                streaming_config=config))

    def print_response(self, responses: Iterable[rasr.StreamingRecognizeResponse]) -> None:
        """
        :param responses: Streaming Response
        :return: None
        """
        self.transcript = ""
        for response in responses:
            if not response.results:
                continue

            for result in response.results:
                if not result.alternatives:
                    continue
                if result.is_final:
                    partial_transcript = result.alternatives[0].transcript
                    self.transcript += partial_transcript
                    # print(self.transcript)
                    return
                    # key = input("Press 'q' to finished recording\n"
                    #             "Press 'r' to redo\n"
                    #             "Press 'c' to continue record\n")
                    #
                    # micStream.closed = True
                    # while key not in ['q', 'r', 'c']:
                    #     print("Please input the correct key!\n")
                    #     key = input()
                    # micStream.closed = False
                    # if key == "q": return
                    # elif key == "r": self.transcript = ""
                    # else: continue
