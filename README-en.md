[中文](README.md) | [English](README-en.md) 

# Kokoro TextToSpeech Node for ComfyUI

![image](https://github.com/billwuhao/ComfyUI_KokoroTTS_MW/blob/master/images/2025-02-17_01-39-16.png)

## Features

- High-quality text-to-speech synthesis
- Multiple voice options
- Support for multilingual text
- Easy integration with ComfyUI workflows

## Supported Language

'a' => American English 

'b' => British English 

'j' => Japanese 

'z' => Chinese 

## Available Voices

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

## Model and Voices Download

1. The model will be automatically downloaded to `C:\Users\xxx\.cache\huggingface\hub\models--hexgrad--Kokoro-82M`
2. Voices, please [here](https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices) Manually download and place it in the `ComfyUI\models\Kokorotts\voices` path

### Thank You

- [Kokoro](https://github.com/hexgrad/kokoro)