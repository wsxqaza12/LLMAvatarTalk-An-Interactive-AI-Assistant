from langchain_core.prompts import PromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv


class LLMService:
    def __init__(self, model="meta/llama3-70b-instruct", k=5):
        load_dotenv()
        self.api_key = os.getenv("NVIDIA_API_KEY")
        self.model = model
        self.k = k
        self.prompt = self.setup_prompt()
        self.llm = ChatNVIDIA(model=self.model)
        self.conversation = ConversationChain(
            prompt=self.prompt,
            llm=self.llm,
            verbose=False,
            memory=ConversationBufferWindowMemory(k=self.k),
        )

    def setup_prompt(self):
        template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

        Current conversation:
        {history}
        Human: {input}
        AI Assistant:"""
        prompt = PromptTemplate(
            input_variables=["history", "input"], template=template)
        return prompt

    def split_text_by_period(self, text, max_length=200):
        """
        Splits the text into chunks that are less than the max_length,
        cutting at sentence boundaries (periods).
        :param text: Full text to split
        :param max_length: Maximum length of each chunk
        :return: List of text chunks
        """
        sentences = text.split('.')
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            sentence = sentence.strip() + '.'
            if len(current_chunk) + len(sentence) <= max_length:
                current_chunk += ' ' + sentence
            else:
                chunks.append(current_chunk.strip())
                current_chunk = sentence
        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def invoke_conversation(self, user_input):
        result = self.conversation.invoke(user_input)
        response_chunks = self.split_text_by_period(result['response'])
        return response_chunks
