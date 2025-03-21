[中文](README-CN.md) | [English](README.md) 

# ComfyUI 的 Kokoro 文本转语音节点

![image](https://github.com/billwuhao/ComfyUI_KokoroTTS_MW/blob/master/images/2025-03-05_17-09-35.png)

## 📣 更新

[2025-03-22]⚒️: 重构代码, 更快的生成速度.

[2025-03-05]⚒️: 支持 8 种语言, 150 种音色.

- 新增语言支持: 

'e' => Spanish 西班牙语  
'f' => French 法语  
'h' => Hindi 印地语  
'i' => Italian 意大利语  
'p' => Brazilian Portuguese 巴西葡萄牙语  

- 对应的新增音色: 

"e": ["ef_dora.pt",
        "em_alex.pt",
        "em_santa.pt"]

"f": ["ff_siwis.pt"]

"h": ["hf_alpha.pt",
        "hf_beta.pt",
        "hm_omega.pt",
        "hm_psi.pt"]

"i": ["if_sara.pt",
        "im_nicola.pt"]

"p": ["pf_dora.pt",
"pm_alex.pt",
"pm_santa.pt"]

- 新增 100 种中文音色:

['zf_001.pt', 'zf_002.pt', 'zf_003.pt', 'zf_004.pt', 'zf_005.pt', 'zf_006.pt', 'zf_007.pt', 'zf_008.pt', 'zf_017.pt', 'zf_018.pt', 'zf_019.pt', 'zf_021.pt', 'zf_022.pt', 'zf_023.pt', 'zf_024.pt', 'zf_026.pt', 'zf_027.pt', 'zf_028.pt', 'zf_032.pt', 'zf_036.pt', 'zf_038.pt', 'zf_039.pt', 'zf_040.pt', 'zf_042.pt', 'zf_043.pt', 'zf_044.pt', 'zf_046.pt', 'zf_047.pt', 'zf_048.pt', 'zf_049.pt', 'zf_051.pt', 'zf_059.pt', 'zf_060.pt', 'zf_067.pt', 'zf_070.pt', 'zf_071.pt', 'zf_072.pt', 'zf_073.pt', 'zf_074.pt', 'zf_075.pt', 'zf_076.pt', 'zf_077.pt', 'zf_078.pt', 'zf_079.pt', 'zf_083.pt', 'zf_084.pt', 'zf_085.pt', 'zf_086.pt', 'zf_087.pt', 'zf_088.pt', 'zf_090.pt', 'zf_092.pt', 'zf_093.pt', 'zf_094.pt', 'zf_099.pt', 'zm_009.pt', 'zm_010.pt', 'zm_011.pt', 'zm_012.pt', 'zm_013.pt', 'zm_014.pt', 'zm_015.pt', 'zm_016.pt', 'zm_020.pt', 'zm_025.pt', 'zm_029.pt', 'zm_030.pt', 'zm_031.pt', 'zm_033.pt', 'zm_034.pt', 'zm_035.pt', 'zm_037.pt', 'zm_041.pt', 'zm_045.pt', 'zm_050.pt', 'zm_052.pt', 'zm_053.pt', 'zm_054.pt', 'zm_055.pt', 'zm_056.pt', 'zm_057.pt', 'zm_058.pt', 'zm_061.pt', 'zm_062.pt', 'zm_063.pt', 'zm_064.pt', 'zm_065.pt', 'zm_066.pt', 'zm_068.pt', 'zm_069.pt', 'zm_080.pt', 'zm_081.pt', 'zm_082.pt', 'zm_089.pt', 'zm_091.pt', 'zm_095.pt', 'zm_096.pt', 'zm_097.pt', 'zm_098.pt', 'zm_100.pt']


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

---

![image](https://github.com/billwuhao/ComfyUI_KokoroTTS_MW/blob/master/images/2025-02-17_01-39-16.png)

## 特性

- 高质量文本转语音
- 多种音色可选
- 支持多种语言的文本
- 与ComfyUI工作流轻松集成

## 支持语言

'a' => American English 美式英语

'b' => British English 英语

'j' => Japanese 日语

'z' => Chinese 中文

## 可用音色

"a": 

["af_alloy", "af_aoede", "af_bella", "af_heart", "af_jessica", 
   "af_kore", "af_nicole", "af_nova", "af_river", "af_sarah", 
   "af_sky", "am_adam", "am_echo", "am_eric", "am_fenrir", 
   "am_liam", "am_michael", "am_onyx", "am_puck", "am_santa"]

"b": 

["bf_alice", "bf_emma", "bf_isabella", "bf_lily", "bm_daniel",
   "bm_fable", "bm_george", "bm_lewis"]

"j": 

["jf_alpha", "jf_gongitsune", "jf_nezumi", "jf_tebukuro", "jm_kumo"]

"z": 

["zf_xiaobei", "zf_xiaoni", "zf_xiaoxiao", "zf_xiaoyi",
   "zm_yunjian", "zm_yunxi", "zm_yunxia", "zm_yunyang"]

## 感谢

- [Kokoro](https://github.com/hexgrad/kokoro)