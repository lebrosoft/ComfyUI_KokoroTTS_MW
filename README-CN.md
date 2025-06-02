[中文](README-CN.md) | [English](README.md) 

# ComfyUI 的 Kokoro 文本转语音节点

- 接近实时快速文本转语音, 
- **支持双人对话**
- 多种音色可选
- 支持多种语言的文本
- 与 ComfyUI 工作流轻松集成

## 📣 更新

[2025-06-02]⚒️: **支持双人对话**.

[2025-03-22]⚒️: 重构代码, 更快的生成速度.

[2025-03-05]⚒️: 支持 8 种语言, 150 种音色.

## 支持语言

- American English 美式英语
- British English 英语
- Japanese 日语
- Chinese 中文
- Spanish 西班牙语  
- French 法语  
- Hindi 印地语  
- Italian 意大利语  
- Brazilian Portuguese 巴西葡萄牙语  

## 使用

- 文本转语音:

![image](https://github.com/billwuhao/ComfyUI_KokoroTTS_MW/blob/master/images/2025-02-17_01-39-16.png)

- 英文双人对话:

![image](https://github.com/billwuhao/ComfyUI_KokoroTTS_MW/blob/master/images/2025-03-05_17-09-35.png)

- 中文双人对话:

![image](https://github.com/billwuhao/ComfyUI_KokoroTTS_MW/blob/master/images/2025-06-02_21-08-34.png)

## 安装

```
cd ComfyUI/custom_nodes
git clone https://github.com/billwuhao/ComfyUI_KokoroTTS_MW.git
cd ComfyUI_KokoroTTS_MW
pip install -r requirements.txt

# python_embeded
./python_embeded/python.exe -m pip install -r requirements.txt
```

## 模型下载

- 模型和音色需要手动下载放到 `ComfyUI\models\Kokorotts` 路径下:

[Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)  
[Kokoro-82M-v1.1-zh](https://huggingface.co/hexgrad/Kokoro-82M-v1.1-zh)

结构如下:
```
ComfyUI\models\Kokorotts
│ Kokoro-82M
   └── voices
   config.json
   kokoro-v1_0.pth
| Kokoro-82M-v1.1-zh
   └── voices
   config.json
   kokoro-v1_1-zh.pth
```

## 鸣谢

- [Kokoro](https://github.com/hexgrad/kokoro)