
# **Introduction:**

<p align="center">
  <img alt="H&PS Hallucination Traffic Incidents Dataset" style="width: 728px; max-width: 100%; height: auto;" src="webfile/Dataset.png"/>
  <h1 align="center">🌟H&PS Hallucination Traffic Incidents Dataset  🌟</h1> 
  <p align="center"><b>A novel cross-lingual benchmark dataset comprising nearly 99,869 real traffic incident records from Vienna (2013-2023) to evaluate LLMs’  Spatio and Temproal robustness as multilingual agents for hallucination problem
</b></p>


![](https://user-images.githubusercontent.com/18329471/234640541-a6a65fbc-d7a5-4ec3-9b65-55305b01a7aa.png)
[![License](https://img.shields.io/badge/license-CCBY.4.0-black)](https://github.com/ComputerVisionFans/llm_hallucination)
[![Downloads](https://img.shields.io/badge/Downloads-red)](https://github.com/ComputerVisionFans/llm_hallucination)
[![Documentation](https://img.shields.io/badge/Read-Documentation-green)](https://sites.google.com/view/llmhallucination/home)
[![Follow](https://img.shields.io/badge/Follow-Authors-blue)](https://qiangli.de/)
[![Paper](https://img.shields.io/badge/Paper-yellow)](https://openreview.net/forum?id=iOuHlsKHf7#discussion)

> +⭐ Follow [Authors]((https://qiangli.de/)) for project updates.


**Website:** [H&PS Hallucination Traffic Incidents Dataset](https://sites.google.com/view/llmhallucination/home)


The H&PS Traffic Incidents Dataset comprises 99,869 real incident records in Vienna public transportation system, categorized into 14 distinct scenarios: Faulty Vehicles, Acute Track Damages, Acute Switch Damages, Overhead Line Faults, Signal Faults, Rescue Operations, Police Interventions, Fire Brigade Interventions, Illegal Parking, Traffic Accidents, Demonstrations, Events, Delays, and Other Incidents.


# Statics of Dataset?
This dataset has been/could be downloaded via Kaggle, paper with code, and Hugging face!

| **Category**                | **Details**                                                                                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LLM Models Covered**      | GPT series include GPT-4, TinyLlama, Claude-3-Haiku, Claude-3-Sonnet, Gemini-Pro 1.0, Mistral Medium, Mistral-8x7B, Llama-3-70B                                                                     |
| **Dataset Complexity**      | - Both Temporal and Spatio domain logical reasoning tasks.                                                                                                                                          |
| **Number of Records**       | - 99,869 real traffic incident records.                                                                                                                                                             |
| **Year of Records**         | - Over ten years (2013 to 2023).                                                                                                                                                                    |
| **Covered Variants**        | - Over 500 tramcars, more than 131 bus lines.                                                                                                                                                       |
| **Covered Variants**        | - 5 underground lines (U1, U2, U3, U4, U6).                                                                                                                                                         |
| **Covered Variants**        | - 24 night lines.                                                                                                                                                                                   |
| **Covered Variants**        | - More than 1,076 Tram Stop Stations.                                                                                                                                                               |
| **Covered Variants**        | - 4,291 Bus Stop Stations.                                                                                                                                                                          |
| **Prompt Torken Length**    | - Daily sentence tokens > 4K.                                                                                                                                                                       |
| **Language Types**          | - Both in German and English.                                                                                                                                                                       |
| **Format of Representation** | json format                                                                                                                                                                                         |
| **Sample of Dataset**       | {                                                                                                                                                                                                   |
| **IncidentID**              | "id": 1,                                                                                                                                                                                            |
| **Incident Category**       | "title": "U3: Polizeieinsatz",                                                                                                                                                                      |
| **Incident Description**    | "description": "Wegen eines Polizeieinsatzes in der Station Landstrasse S U ist die Linie U3 in Fahrtrichtung Simmering an der Weiterfahrt gehindert...Das Störungsende ist derzeit nicht absehbar.", |
| **Incident Start Time**     | "start": "2023-11-21 12:26:12",                                                                                                                                                                     |
| **Traffic Delay Start time** | "traffic_start": "2023-11-21 12:27:42",                                                                                                                                                             |
| **Incident End Time**       | "end": "",                                                                                                                                                                                          |
| **Effect Lines**            | "lines": "U3"                                                                                                                                                                                       |
| **Sample of Dataset**        | }                                                                                                                                                                                                   |
* The actual start time of a traffic delay can sometimes differ from the recorded start time. The recorded start time refers to when support services first receive the incident report. Due to the current legacy manual system for incident reporting and monitoring, the end time is optional and is sometimes not documented in the database, adding to the complexity.
* The total number of incident categories could exceed 20, given that definitions have evolved over the past decade. However, for this study, we focus on testing LLMs against 14 distinct scenarios: Faulty Vehicles, Acute Track Damages, Acute Switch Damages, Overhead Line Faults, Signal Faults, Rescue Operations, Police Interventions, Fire Brigade Interventions, Illegal Parking, Traffic Accidents, Demonstrations, Events, Delays, and Other Incidents.



| **Störungen nach Jahr**      | **2013*** | **2014** | **2015** | **2016** | **2017** | **2018** | **2019** | **2020** | **2021** | **2022** | **2023** | **Gesamt** |
|-----------------------------|-----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| **Schadhafte Fahrzeuge** (Faulty Vehicles) | 132 (446) | 477      | 592      | 966      | 1282     | 921      | 949      | 1062     | 1527     | 1753     | 2326     | 11987    |
| **Akute Gleisschäden** (Acute Track Damages) | 11 (37)   | 46       | 38       | 63       | 48       | 53       | 33       | 52       | 50       | 54       | 70       | 518      |
| **Akute Weichenschäden** (Acute Switch Damages) | 1 (3)     | 4        | 11       | 57       | 58       | 59       | 68       | 64       | 45       | 57       | 69       | 493      |
| **Fahrleitungsgebrechen** (Overhead Line Faults) | 16 (54)   | 69       | 77       | 94       | 104      | 114      | 101      | 70       | 108      | 80       | 100      | 933      |
| **Signalstörungen** (Signal Faults) | 2 (7)     | 20       | 21       | 45       | 25       | 27       | 28       | 21       | 40       | 48       | 65       | 342      |
| **Rettungseinsätze** (Rescue Operations) | 198 (669) | 701      | 912      | 1247     | 1341     | 1224     | 1378     | 1188     | 1693     | 1955     | 2413     | 14250    |
| **Polizeieinsätze** (Police Interventions) | 54 (183)  | 266      | 442      | 783      | 759      | 702      | 653      | 679      | 1062     | 1236     | 1289     | 7925     |
| **Feuerwehreinsätze** (Fire Brigade Interventions) | 17 (57)   | 84       | 152      | 267      | 274      | 305      | 325      | 287      | 325      | 323      | 403      | 2562     |
| **Falschparker** (Illegal Parking) | 137 (463) | 507      | 778      | 953      | 975      | 1017     | 1124     | 932      | 1246     | 1328     | 1229     | 10126    |
| **Verkehrsunfälle** (Traffic Accidents) | 394 (1332) | 1386     | 1466     | 1749     | 1549     | 1457     | 1528     | 1292     | 1761     | 1879     | 2102     | 16563    |
| **Demonstrationen** (Demonstrations) | 0 (0)     | 25       | 40       | 44       | 40       | 89       | 147      | 122      | 215      | 239      | 252      | 1213     |
| **Veranstaltungen** (Events) | 0 (0)     | 0        | 0        | 20       | 70       | 71       | 70       | 107      | 122      | 107      | 81       | 648      |
| **Verspätungen** (Delays) | 1675 (5661) | 4838    | 2608     | 1213     | 325      | 468      | 944      | 1137     | 3320     | 8048     | 2502     | 26976    |
| **Sonstige** (Other Incidents) | 220 (744) | 651      | 655      | 339      | 410      | 394      | 428      | 503      | 647      | 943      | 1724     | 6914     |
| **Störungen gesamt** (Total Incidents) | 2863 (9676) | 9074    | 7812     | 7890     | 7261     | 6900     | 7813     | 7431     | 12258    | 17877    | 14625    | 102804   |

*Please note: Data collection for 2013 covers only from September 14th to December 31st. 
The numbers in parentheses represent a hypothetical projection for the entire year.*





# Code Structure


    ├── hypothesize  # Our hypothesized dataset based on hypothesis: given sentence indexing, date-to-text conversion, and German-to-English translation.
    ├── original     # Original incident records in a JSON file, includes real traffic records from Vienna.
    ├── results-1    # Results files and logs for hypothesis 1.
    ├── results-2    # Results files and logs for hypothesis 2.
    ├── results-3    # Results files and logs for hypothesis 3.
    ├── Spatio       # Results files and logs for spatial-related experiments, includes prompt samples, and all the traffic logs and ground truth.
    ├── Temporal     # Results files and logs for time/temporal-related experiments, includes prompt samples, and all the traffic logs and ground truth.
    ├── webfile      # Web files used for building the website and README, and incidents.
    ├── database.json  # Simple dataset you can easily play with using LLMs, since the original file includes 99K incidents, major LLMs won't accept such token length input.
    ├── gptapt-ipynb   # GPT Jupyter notebook for experiments, typically closed-source, enterprise LLM. You will need to have an API key (key.txt) for experiments.
    ├── tinyllama.ipynb  # TinyLlama Jupyter notebook for experiments, open-source LLM. You can download the model weights and do local testing.
    ├── Licence and legal declaration  # CC BY 4.0 but with imporant Declaration
    └── README.md




# Acknowledgement and Legal Declaration
If you find this dataset useful in your research, please consider citing it. We extend our sincere thanks to those who contributed to our paper, helped significantly with the development of GenAI applications, dataset cleaning, and hypothesis brainstorming sessions:

- Alam, Touhidul
- Alikhanian, Aik
- Grimm, Christine
- Kirisits, Julia
- Oh, Jung-Hyun
- Stöhr, Stefan

**_Special thanks_** go to Mingkun, Tan, and Martin Piskernig for their help with dataset queries and cleaning. We also thank Open Government Data (OGD) program in EU for academic research.

This dataset, including our hypothesized data, **adheres to strict regulations for responsible AI**. _For any enterprise or researcher, using this dataset means taking intentional actions to design, deploy, and use it to create value and build trust by mitigating potential risks._

We **strongly against** using this dataset for any kind of warfare or activities targeting human beings. We reserve the right to revoke or completely remove our dataset for such purposes and will not be responsible for any kind of loss resulting from such actions.

This dataset is intended to **encourage public thinking about how LLMs might responsibly answer spatio-temporal queries, thereby helping to build robust systems for our community.**

# LLM  Open Board and important link

Ongoing XAI Project with targeting of exploring llm hallucination problem

Open_llm_leaderboard for select llm: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard 

Opensource LLama model: https://github.com/jzhang38/TinyLlama/blob/main/EVAL.md


