


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

> +⭐ 08th Sep. News:
You can now access our dataset using [Google Cloud Storage](https://storage.googleapis.com/ragwg/Wiener_2023.txt) as well! if you want to utilize our data with [LlamaIndex Vertex AI for RAG](https://cloud.google.com/vertex-ai/generative-ai/docs/use-feature-store-with-rag/)!


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

- Open_llm_leaderboard for select llm: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard 

- Opensource LLama model: https://github.com/jzhang38/TinyLlama/blob/main/EVAL.md

# RAG Ablation Study (Support Vertex AI and OpenAI both)

<p align="center">
  <img alt="H&PS Hallucination Traffic Incidents Dataset" style="width: 728px; max-width: 100%; height: auto;" src="webfile/RAG.png"/>
  <p align="center"><b>🌟LangFlow and Vector Store RAG With our Dataset as Context Embedding + Spatio/ Temporal Query Embedding 🌟</h1> 
 </b></p>

```

| Category           | Prompt/Questions                                                                                      | GPT 4 Response | RAG embedded GPT-4 
|--------------------|------------------------------------------------------------------------------------------------------|----------------| ----------------
| **Space**          | From Schloss Schönbrunn to Musikverein Wien on 21st Nov 2023, am my trip affected?                    | ✓              | x
|                    | From Haus des Meeres to U-Bahn-Station Roßauer Lände on 21st Nov 2023, am my trip affected?           | ~              | x
|                    | From Theater in der Josefstadt to Naturhistorisches Museum Wien on 19th September 2023, am my trip affected? | ~          | x 
|                    | From Museum für angewandte Kunst to Wiener Kriminalmuseum on 19th September 2023, am my trip affected? | ✓             | x 
| **Time**           | List of disruption causes per hour?                                                                   | ✓              |  ✗
|                    | Lines with most disruptions during peak hours?                                                        | ✗              |  ✓
|                    | Time spans with most disruptions?                                                                     | ✗              | ~
|                    | First and last disruption of the year?                                                                | ✗              |  ✓
|                    | 3 disruptions with the greatest impact?                                                               | ✗              |  ~
|                    | 3 events with the longest duration?                                                                   | ✓              |  ✗
|                    | The average duration of all events?                                                                   | ✓              | ✗
|                    | All events starting between 6 AM and 6 PM                                                             | ✗              | ✗
|                    | All 'Long events' and their average duration                                                          | ✗              | ✗
|                    | The total duration of events by time of day?                                                          | ✗              | ✗


| Question  (selective)                                     | RAG OUTPUT sample                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average duration of all events                 | "To calculate the average duration of all events, we need to determine the duration for each event from the provided context. Identify the events: Each event has a start time and, where applicable, an estimated end time or an indication of how long it lasts. Calculate the duration of each event: For events with a specified end time, subtract the start time from the end time. For those with a duration stated (like ""until X"" or ""lasts until X""), use that information to calculate the duration. Convert the duration to a consistent unit: For this calculation, we can convert all durations to minutes. Average the durations: Sum all the durations and divide by the total number of events. However, since the detailed calculation requires processing each event, I can provide a general outline of how you would do this, but I cannot compute the exact average without all the specific durations calculated from the data provided. If you need further assistance in calculating this or need a specific approach, please let me know!" |
| 3 disruptions with the greatest impact?        | "Based on the provided context, the three disruptions with the greatest impact are: U3: Polizeieinsatz - The U3 line in the direction of Simmering is unable to proceed due to a police operation at the Landstraße S U station, with no estimated end time. 40A: Falschparker - The 40A line is hindered in the direction of Döblinger Friedhof due to a parked vehicle in the Sechsschimmelgasse area, with an expected disruption until 13:15. 40 , 41: Falschparker - Both the 40 and 41 lines are blocked in the direction of Gersthof and Pötzleinsdorf due to a parked vehicle in the Gentzgasse area, with an expected disruption until 12:45. These disruptions are significant as they involve major lines and ongoing police actions, which tend to affect larger numbers of passengers." |
| Total duration of events by time of day        | "To calculate the total duration of events by time of day, we need to extract the start and end times from the provided context and determine the duration of each event. Here's a breakdown of the events along with their respective durations: 40A: Falschparker Start: 12:46:57 End: 13:15:00 (assumed based on the duration stated) Duration: 28 minutes U3: Polizeieinsatz Start: 12:26:12 Duration: Unknown (stated as not foreseeable) 40 , 41: Falschparker Start: 12:20:54 End: 12:45:00 (assumed based on the duration stated) Duration: 24 minutes U6: Betriebsstörung Start: 12:11:12 End: 12:26:02 Duration: 15 minutes 44: Schadhaftes Fahrzeug Start: 12:02:47 End: 12:30:00 (assumed based on the duration stated) Duration: 27 minutes 66A: Rettungseinsatz Start: 11:27:16 End: 11:30:00 (assumed based on the duration stated) Duration: 3 minutes U3: Schadhaftes Fahrzeug Start: 10:51:03 End: 12:25:01 Duration: 94 minutes 10: Feuerwehreinsatz Start: 10:08:10 End: 10:40:00 (assumed based on the duration stated) Duration: 32 minutes 12A: Schadhaftes Fahrzeug Start: 10:02:33 End: 10:36:00 (assumed based on the duration stated) Duration: 34 minutes O: Demonstration Start: 09:55:25 End: 10:30:00 (assumed based on the duration stated) Duration: 35 minutes ... and so forth for each event listed. The total duration of events can be calculated by summing the durations of all events that have an explicit duration. For events without a clear end time, we cannot contribute to the total. To summarize, if we were to categorize all of them by hour and add the durations, we would have a total duration of the events per hour. Finally, the results would look something like this: 09:00 - 10:00: Total Duration = X minutes 10:00 - 11:00: Total Duration = Y minutes 11:00 - 12:00: Total Duration = Z minutes 12:00 - 13:00: Total Duration = W minutes You would need to sum all the durations for each time slot accordingly." |
| Time spans with most disruptions               | "Based on the provided context, the time spans with the most disruptions can be identified as follows: 12:00 PM - 1:00 PM (UTC+1): Multiple disruptions affecting lines 40A, U3, and 41 due to various issues including false parking and police actions. 11:00 AM - 12:00 PM (UTC+1): Disruptions noted for lines U3, 66A, and 44, including police actions and faulty vehicles. 10:00 AM - 11:00 AM (UTC+1): Multiple incidents including police actions affecting lines O and U3, along with disruptions on lines 10, 12A, and 66A. These time spans indicate periods where multiple transit lines experienced significant service interruptions due to various incidents." |
| Lines with most disruptions during peak hours  | "Based on the provided context, here are the lines with the most disruptions during peak hours (which typically include busy times such as mornings and late afternoons): U3: This line has multiple disruptions due to police activity, a faulty vehicle, and irregular service noted on several occasions. U4: There are numerous mentions of disruptions due to rescue operations and faulty vehicles impacting service. 10: This line has faced disruptions due to both a fire department operation and a traffic accident. 43: This line has been affected by police interventions and traffic accidents, leading to service interruptions. 40A: This line has seen disruptions due to parking violations and traffic congestion. 49: This line has been impacted by traffic accidents causing delays. 2: This line has experienced several disruptions from rescue operations and vehicle issues. These lines have shown a pattern of disturbances during peak hours, making them significant in terms of service reliability." |
| First and last disruption of the year          | "The first disruption of the year was on January 1, 2023, with a title related to a 'Falschparker' (wrongfully parked vehicle) affecting the line 5. The last disruption recorded was on November 21, 2023, involving a 'Falschparker' that hindered the line 40A, expected to last until 13:15." |

```



## Setup/Installation LangFlow


### Install LangFlow using pip. Ensure you have [Python 3.10](https://www.python.org/downloads/) or above installed.

- **Command to check Python version:**

```bash
python --version
```

or

```bash
python3 --version
```

- **If Python is not installed:**
  - **Download and install it from** [python.org](https://www.python.org/).
  - **Open your terminal and run the following command:**

```bash
pip install langflow --pre --force-reinstall
```

**Explanation:**

- `pip install` is the command to install Python packages.
- `langflow` is the name of the package.
- `--pre` allows the installation of pre-release versions.
- `--force-reinstall` forces the reinstallation of the package even if it's already installed.

### Run LangFlow locally.

- **Command to run LangFlow:**

```bash
langflow run 
```
- **Open LangFlow in your browser:**
  - Navigate to `http://localhost:7860` if it doesn't open automatically.
  - Can also insert our H&PS langflow Json

### Create a new flow.

- **Steps:**
  1. Click "New Project."
  2. Select "Blank Flow."

### Add text and chat inputs:

1. **From the sidebar, drag and drop the "Text Input" and "Chat Input" components.**
2. **Rename "Text Input" to "Name":**
   * Set it to capture the user's name.
3. **Connect the output of "Name" to the sender name input of "Chat Input."**

### Create a prompt template:

1. **Add a "Prompt" component.**
2. **Edit the template to include placeholders for context, question, and history:**

```markdown
Hey, answer the user's question based on the following context:
The context is this: {context}
And this is the message History: {history}
The users question is this: {question}
```

### Add chat memory:

1. **Drag and drop the "Chat Memory" component.**
2. **Connect the name input to the session ID of the chat memory.**

### Add a chat output:

1. **Drag and drop the "Chat Output" component.**
2. **Connect the output of the OpenAI component to the chat output.**
3. **Set the sender name to "AI."**
   
---

## OpenAI Integration

### Create an OpenAI account.

- **Sign up at** [OpenAI](https://platform.openai.com/).

### Generate an OpenAI API key.

- **Steps:**
  1. Go to API keys in your OpenAI dashboard.
  2. Click "Create new secret key."
  3. Name the key to LangFlow-API (Makes things easier if you use more than one OpenAI API key)
  4. Give it access to everything.
  5. Copy the generated key.

### Connect to OpenAI:

1. **Add an "OpenAI" component.**
2. **Name it OpenAI_Key_New.**
3. **Paste your OpenAI API key in the Value field (Box).**
4. **Make the 'Type' Credential.**
5. **Click Save Variable.**
6. **Drag the Chat Output from the menu and drag it to the left of OpenAI and place it beside.**
7. **Drag and link the connection from OpenAI 'text' to the Chat Output 'Message'.**
8. **Connect the prompt to the OpenAI component.**

---

## VectorStore Databases

### Create a free account on DataStax Astra.

- **Go to** [DataStax Astra](https://dtsx.io/3vZk6n2) **and sign up.**

### Create a new database.

- **Steps:**
  1. Click on "Create Database."
  2. Select "Serverless Vector Database."
  3. Name your database (e.g., " you can directly use our H&PS LangFlow").
  4. Choose your cloud provider and region.
  5. Click "Create Database."

### Configure Astra DB:

1. **Add an "Astra DB" component.**
2. **Enter your Astra DB endpoint, token, and collection name.**
3. **Connect the embeddings to the Astra DB component.**

---

## Adding RAG

### Load the Dataset file:

1. **Add a "File Loader" component.**
2. **Upload your Json file (e.g., monthly or Yearly dataset).**

### Split the text:

1. **Add a "Split Text" component.**
2. **Connect the file loader to the split text component.**

### Set up OpenAI embeddings:

1. **Add an "OpenAI Embeddings" component.**
2. **Connect the split text output to the embeddings input.**

### Add a Vector Search component:

1. **Connect the chat input to the Vector Search component.**
2. **Connect the embeddings to the Vector Search component.**
3. **Connect the output of the Vector Search component to the prompt context input.**



