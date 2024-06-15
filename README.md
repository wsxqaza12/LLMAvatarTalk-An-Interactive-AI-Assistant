# LLMAvatarTalk

LLMAvatarTalk 是一個結合了語音識別(ASR)、大型語言模型(LLM)、文字到語音(TTS)和音頻驅動的面部動畫(Audio2Face)技術的創新解決專案，展示了如何通過整合多種 AI 技術來實現一個交互式的虛擬助理。

## 功能特色

- **語音識別**：使用 NVIDIA RIVA ASR 技術，將用戶的語音即時轉換成文字。
- **語言處理**：利用 NVIDIA NIM APIs 使用先進的LLM(如llama3-70b-instruct)進行深入的語義理解和回應生成。
- **文字到語音**：通過 NVIDIA RIVA TTS 將生成的文字回應轉換成自然的語音輸出。
- **面部動畫**：使用 Audio2Face 技術根據語音輸出生成逼真的面部表情和動畫。
- **虛幻引擎整合**：利用 Unreal Engine 的 Metahuman 與 Audio2Face 實現實時連結，增強虛擬角色的表現力。


## 先決條件
- NVIDIA NIMs API KEY
    - 可以在 [NIM](https://build.nvidia.com/explore/discover?signin=false&signin_corporate=false) 申請免費的 1000 credits 
- Nvidia Riva Server
- Audio2Face
- Unreal Engine

## 安裝
   ```plaintext
   git clone https://github.com/yourusername/LLMAvatarTalk.git
   cd LLMAvatarTalk
   pip install -r requirements.txt
   ```

## 運行
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

## 架構
<img src = "https://github.com/wsxqaza12/LLMAvatarTalk-NVIDIA-RIVA-Audio2Face-Langchain/blob/main/png/architecture%20diagram.png" width ="700" />
