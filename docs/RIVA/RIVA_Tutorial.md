# RIVA

NVIDIA RIVA is a GPU-accelerated SDK for building speech AI applications that require real-time performance. It provides state-of-the-art models for automatic speech recognition (ASR), text-to-speech (TTS), and natural language processing (NLP). By leveraging RIVA, developers can create applications with high accuracy and low latency, making it ideal for interactive AI assistants like LLMAvatarTalk.

**Recommended setup on different computer architectures.  
My environment is WSL Ubuntu 20.04.6 LTS**

## Installation

1. Download the [NGC CLI](https://org.ngc.nvidia.com/setup/installers/cli), selecting the version suitable for your environment.
    1. Alternatively, you can download, unzip, and install it from the command line:
        
        ```bash
        wget --content-disposition https://api.ngc.nvidia.com/v2/resources/nvidia/ngc-apps/ngc_cli/versions/3.43.0/files/ngccli_linux.zip -O ngccli_linux.zip && unzip ngccli_linux.zip
        ```
        
    2. Verify the binary's MD5 hash to ensure the file wasn't corrupted during download:
        
        ```bash
        find ngc-cli/ -type f -exec md5sum {} + | LC_ALL=C sort | md5sum -c ngc-cli.md5
        ```
        
    3. After verifying, make the NGC CLI binary executable and add your current directory to the path:
        
        ```bash
        chmod u+x ngc-cli/ngc
        echo "export PATH=\"\$PATH:$(pwd)/ngc-cli\"" >> ~/.bash_profile && source ~/.bash_profile
        ```
        
    4. Configure NGC CLI for your use by running the following command and entering your API key when prompted:
        
        ```bash
        ngc config set
        ```
        
        - You will need to set up your API key:
            1. Log in to your enterprise account on the NGC website [http://ngc.nvidia.com](http://ngc.nvidia.com).
            2. Click Setup from the side menu, then click API Key from the Setup page.
            3. On the API Key page, click Generate API Key.
            4. In response to the warning that your old API Key will become invalid, click CONTINUE to generate the key.
            5. Your API key is displayed with examples of how to use it.
            6. Note that the API key for NIM is different.

2. Download RIVA
    1. Go to [NVIDIA RIVA Quickstart](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/riva/resources/riva_quickstart/files) and choose your desired version.
    2. Use the CLI option provided to download it:
    
    ```bash
    ngc registry resource download-version "nvidia/riva/riva_quickstart:2.15.1"
    ```
    
3. Install RIVA server
    ```bash
    cd riva_quickstart_v2.15.1
    sudo bash riva_init.sh
    sudo bash riva_start.sh
    ```
4. Change port  
    - The Riva server will take a few seconds to start. By default, it starts on port 50050 as localhost.
    - You can change the port number and other configurations in `config.sh`. Note that you need to rerun `riva_init.sh` each time you change configurations inside `config.sh`.
