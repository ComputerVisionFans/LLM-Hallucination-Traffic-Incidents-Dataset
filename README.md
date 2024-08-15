
# **Introduction:**

<p align="center">
  <img alt="H&PS Hallucination Traffic Incidents Dataset" style="width: 728px; max-width: 100%; height: auto;" src=""/>
  <h1 align="center">🌟H&PS Hallucination Traffic Incidents Dataset  🌟</h1> 
  <p align="center"><b>A novel cross-lingual benchmark dataset comprising nearly 99,869 real traffic incident records from Vienna (2013-2023) to evaluate LLMs’  Spatio and Temproal robustness as multilingual agents for hallucination problem
</b></p>
</p>

![](https://user-images.githubusercontent.com/18329471/234640541-a6a65fbc-d7a5-4ec3-9b65-55305b01a7aa.png)
[![license](https://img.shields.io/github/license/vietanhdev/anylabeling.svg)](https://github.com/vietanhdev/anylabeling/blob/master/LICENSE)
[![Downloads](https://img.shields.io/badge/Downloads-red)](https://github.com/ComputerVisionFans/llm_hallucination)
[![Documentation](https://img.shields.io/badge/Read-Documentation-green)](https://sites.google.com/view/llmhallucination/home)
[![Follow](https://img.shields.io/badge/Follow-Qiang-blue)](https://qiangli.de/)
[![Paper](https://img.shields.io/badge/Paper-yellow)](https://openreview.net/forum?id=iOuHlsKHf7#discussion)

> +⭐ Follow [Authors]((https://qiangli.de/)) for project updates.


**Website:** [H&PS Hallucination Traffic Incidents Dataset](https://sites.google.com/view/llmhallucination/home)/



# Number of Dataset?
this dataset has been/could be downloaded via Kagglg, paper with code, and hugging face!

| **Category**               | **Details**                                                                                                                                          |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LLM Models Examined**     | GPT series, TinyLlama, Claude-3-Haiku, Claude-3-Sonnet, Gemini-Pro 1.0, Mistral Medium, Mistral-8x7B, Llama-3-70B                                     |
| **Dataset Complexity**      | - Both Temporal and Spatio domain logical reasoning tasks.                                                                                           |
|                            | - 99,869 real traffic incident records.                                                                                                              |
|                            | - Over ten years (2013 to 2023).                                                                                                                     |
|                            | - Over 500 tramcars, more than 131 bus lines.                                                                                                        |
|                            | - 5 underground lines (U1, U2, U3, U4, U6).                                                                                                          |
|                            | - 24 night lines.                                                                                                                                   |
|                            | - More than 1,076 Tram Stop Stations.                                                                                                                |
|                            | - 4,291 Bus Stop Stations.                                                                                                                           |
|                            | - Daily sentence tokens > 4K.                                                                                                                        |
|                            | - Both in German and English.                                                                                                                        |
| **Sample Representation**   | json format                                                                                                                                            |
|                            | {                                                                                                                                                    |
|                            |   "id": 1,                                                                                                                                           |
|                            |   "title": "U3: Polizeieinsatz",                                                                                                                     |
|                            |   "description": "Wegen eines Polizeieinsatzes in der Station Landstrasse S U ist die Linie U3 in Fahrtrichtung Simmering an der Weiterfahrt gehindert...Das Störungsende ist derzeit nicht absehbar.", |
|                            |   "start": "2023-11-21 12:26:12",                                                                                                                    |
|                            |   "traffic_start": "2023-11-21 12:27:42",                                                                                                            |
|                            |   "end": "",                                                                                                                                         |
|                            |   "lines": "U3"                                                                                                                                      |
|                            | }                                                                                                                                                    |
|                            | ```                                                                                                                                                  |


# Code Structure


    
    ├── showmask.py             # show the mask of the image, you can use it for showing the segmentation mask generated with fully back mask image
    ├── removebg.py             # remove the jpg image
    ├── transparent.py          # remove the background of the image and convert it into transparent form and save the output as png image
    ├── Segmentbackground.py    # generate fully transpanrent background image ( currently the one used during the demostration)
    ├── json_into_mask.py       # convert the json file into mask image
    ├── segementwithRGB.py      # the code NOT used for generating the background with real environment, bit-wise and operation cannot create optimal result
    ├── generate_background.py  # generate the background with real environment, the code used for generating the background with real environment,the addWeighted method is used for generating the optimal result and it is the best method for generating the background with real environment, it is blending the image with the weight of the image, which performs an element-wise addition of the two images with equal weights.
    └── README.md



# **Citation:**
If you find Dataset useful in your research, please consider citing:
```
```



# llm_hallucination

Ongoing XAI Project with targeting of exploring llm hallucination problem

Next Step: comparing with latest GPT-4 model performance and https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard 

https://github.com/jzhang38/TinyLlama/blob/main/EVAL.md


