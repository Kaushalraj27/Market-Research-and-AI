# 🚀 Market Research and AI Use Case Generation Using Multi-Agent Architecture (CrewAI)

## 📌 Objective
This project automates **AI-driven market research**, **use case generation**, and **dataset resource mapping** for any given company using a **multi-agent system** powered by **CrewAI** and **Groq's Llama3-70B model**.

It simulates domain experts' workflows to:
- Perform in-depth company and market research.
- Propose innovative AI/ML/GenAI use cases.
- Identify relevant public datasets to support the proposed use cases.
---

## 🛠️ Technologies Used
- **Python 3.10+**: Core programming language.
- **Streamlit**: Front-end UI for input and report download.
- **CrewAI**: Multi-agent orchestration framework.
- **Groq Llama3-70B**: Cognitive reasoning and text generation via API.
- **LangChain** *(Optional)*: For future web search and LLM tooling.
- **Markdown (.md) Generation**: Structured professional report format.
- **Environment Variables (.env)**: Secure API key management.

---

## 🏛️ System Architecture

1. **User Input**: Company name via Streamlit form.
2. **Streamlit Application**: Captures input and displays output.
3. **CrewAI Crew**:
   - **Research Agent**: Gathers company and industry information.
   - **Use Case Agent**: Generates 5 tailored AI/ML/GenAI use cases.
   - **Resource Agent**: Suggests public datasets relevant to the use cases.
4. **Groq Llama3-70B Model**: Provides cognitive intelligence to all agents.
5. **Markdown Report Generation**: Compiles outputs into a structured report.
6. **Downloadable Output**: Report available for download via Streamlit.
   
![Architecture](https://github.com/user-attachments/assets/bd735c80-d84f-46ba-aa19-e468368d52e9)

---

## 🔄 Working Flow

- **Step 1**: User enters a company name via Streamlit.
- **Step 2**: Backend initializes CrewAI and multi-agent orchestration.
- **Step 3**: Agents execute sequential tasks using Groq Llama3-70B.
- **Step 4**: Outputs compiled into a structured Markdown (.md) report.
- **Step 5**: User reviews and downloads the final AI Assignment report.

---

## 📋 Sample Output Structure

- **Company and Industry Research**
- **AI/ML/GenAI Use Case Proposals**
- **Relevant Public Dataset Suggestions**

Example Company: **Nextcode**

Example Use Case: **Predictive Maintenance Alerts using AI**

---

## 📈 Future Scope

- Real-time web search integration for updated company insights.
- Competitor benchmarking and comparative analysis.
- Dynamic dataset search automation from Kaggle, GitHub, HuggingFace.
- Export reports in PDF, DOCX, and HTML formats.
- Enhanced natural language report writing and executive summaries.
- SaaS platform deployment for wider adoption.

---

## 🤝 Contributions

Contributions are welcome!  
Feel free to fork the repository, open issues, and submit pull requests.

---

## 📄 License

This project is developed for academic, research, and professional prototyping purposes.  
Formal licensing information will be added soon.

---

## 📬 Contact

For any queries, collaborations, or feedback, please feel free to reach out.

---
