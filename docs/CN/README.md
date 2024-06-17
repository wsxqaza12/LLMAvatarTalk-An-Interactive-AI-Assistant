<div align="center">

<h1>LLMAvatarTalk: An Interactive AI Assistant</h1>
LLMAvatarTalk 是一個創新的專案，結合了最先進的 AI 技術，創建了一個互動式虛擬助理。通過整合自動語音識別(ASR)、大型語言模型(LLM)、文字到語音(TTS)、LangChain 和音頻驅動的面部動畫(Audio2Face)與虛幻引擎的 Metahuman，LLMAvatarTalk 展示了 AI 在實現無縫且引人入勝的人機互動中的潛力。 
<br><br>

[**English**](../../README.md)  | **中文**

</div>

## 功能特色
- **語音識別**：使用 NVIDIA RIVA ASR 技術，將用戶的語音即時轉換成文字。
- **語言處理**：利用 NVIDIA NIM APIs 使用先進的LLM(如llama3-70b-instruct)進行深入的語義理解和回應生成。
- **文字到語音**：通過 NVIDIA RIVA TTS 將生成的文字回應轉換成自然的語音輸出。
- **面部動畫**：使用 Audio2Face 技術根據語音輸出生成逼真的面部表情和動畫。
- **虛幻引擎整合**：利用 Unreal Engine 的 Metahuman 與 Audio2Face 實現實時連結，增強虛擬角色的表現力。
- **LangChain**：簡化 NVIDIA RIVA 和 NVIDIA NIM API 的集成，為 AI 開發提供無縫且高效的工作流程。

## 架構
<img src = "https://github.com/wsxqaza12/LLMAvatarTalk-An-Interactive-AI-Assistant/blob/main/images/architecture%20diagram.png" width ="700" />

## 先決條件
- NVIDIA NIMs API KEY
    - 可以在 [NVIDIA NIMs](https://build.nvidia.com/explore/discover?signin=false&signin_corporate=false) 申請免費的 1000 credits 
- Nvidia Riva Server
   - [Riva 教學](../RIVA/RIVA_Tutorial.md)
- Audio2Face
   - [Audio2Face 教學](../Audio2Face/Audio2Face_Tutorial.md)
- Unreal Engine & Metahuman
   - [Unreal Engine & Metahuman 教學](../UE/UE_Tutorial.md)

## 安裝
測試通過環境：windows 11 & python=3.9

```plaintext
git clone https://github.com/yourusername/LLMAvatarTalk.git
cd LLMAvatarTalk
pip install -r requirements.txt
```

## 執行
1. 確定你已經架設好 Riva 伺服器並設定好 Audio2Face 與 Unreal Engine
2. 創建 .env 並輸入 NVIDIA NIMs API KEY，你可以在 .env.sample 找到範例
   ```plaintext
   NVIDIA_API_KEY=nvapi-
   ```
4. 將 Riva 伺服器的 IP:PORT 填入 config.py 中的 URI，一般Riva 伺服器的 PORT 為 "50051"。
   ```plaintext
   URI = '192.168.1.205:50051'
   ```
5. 執行 `python main.py`

## 代辦事項
- [ ] LLM 功能優化，如加入 RAG 與 Agent
- [ ] TTS 優化
- [ ] 偵測情感和全身動畫
- [ ] 異步處理


## 致謝
感謝以下專案與文件：

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


