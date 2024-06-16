# Unreal Engine and MetaHuman
Unreal Engine (UE) is a powerful game engine developed by Epic Games, widely used for creating high-quality games, simulations, and visualizations. It offers advanced real-time 3D creation tools, a robust rendering engine, and an extensive suite of features for developers, making it a popular choice in the gaming and entertainment industry.

MetaHuman is a groundbreaking tool within Unreal Engine that allows for the creation of highly realistic human characters. Developed by Epic Games, MetaHuman Creator enables users to design and customize digital humans with ease, offering a wide range of facial features, skin tones, hairstyles, and more. This tool significantly reduces the time and effort required to create lifelike characters for games, films, and other interactive applications.

## Step-by-Step Guide
1. Download Epic Lunch from the [official website](https://www.unrealengine.com/en-US/metahuman)
2. Go to UE-Library and install version 5.3, not 5.4, because the current plugins only support 5.3
![EPIC](../../images/UE/EPIC.png)
3. (Optional) You can create your character on the Metahuman official website
    1. [Metahuman official website](https://metahuman.unrealengine.com/)
        ![Metahuman](../../images/UE/Metahuman.png)     
    2. Make sure to select version 5.3
    3. You need to log in with your EPIC account
2. Open the MetaHuman project, and remember the project path
3. Install plugins
    1. Copy the plugins from the audio2face directory
        1. `Library\audio2face-2023.2\ue-plugins\audio2face-ue-plugins\ACEUnrealPlugin-5.3\ACE`
    2. Paste them into the plugins folder in your project path. If it does not exist, create it yourself
    3. Restart MetaHuman
4. Use Live Link to connect audio2face
    1. Select Live Link under Virtual Production
    ![LiveLink](../../images/UE/LiveLink.png)      
    2. Adjust the Audio Sample Rate to match your settings
    ![NVIDIA_LiveLink](../../images/UE/NVIDIA_LiveLink.png)    
    3. In Live Link, select Audio2Face and check the `Use ARKfit face`
    ![ARKit_LiveLink](../../images/UE/ARKit_LiveLink.png)  