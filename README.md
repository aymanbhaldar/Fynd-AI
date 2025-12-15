# Fynd AI Intern Assessment

This repository contains the complete submission for the Fynd AI Intern Take-Home Assessment. It includes both the **Yelp Rating Prediction Model (Task 1)** and the **AI Feedback Dashboard (Task 2)**.

## 🚀 Live Deployments (Mandatory)

| Component | Status | Link |
| :--- | :--- | :--- |
| **User Dashboard** | 🟢 Live | https://fynd-aigit-ipmmd67rjcayaruhcqsnjk.streamlit.app/#leave-a-review |
| **Admin Dashboard** | 🟢 Live |  |
| **Project Report** | 📄 PDF | [] |

*(Note: The User and Admin dashboards are hosted on the same Streamlit app. Use the sidebar to toggle between them.)*

---

## 📂 Repository Structure

* `app.py`: The main Streamlit application source code for Task 2.
* `Task1_Yelp_Rating_Prediction_Prompting.ipynb`: The Jupyter Notebook containing the prompt engineering experiments and evaluation for Task 1.
* `requirements.txt`: List of Python dependencies required to run the project.
* `README.md`: Project documentation.

---

## 📝 Task 1: Rating Prediction via Prompting

**Objective:** Classify Yelp reviews into 1-5 star ratings using LLM prompting strategies without traditional model training.

**Approach:**
We implemented and evaluated three distinct prompting techniques using the `gpt-4o-mini` model:
1.  **Zero-Shot Prompting:** Baseline approach asking for a direct classification.
2.  **Rubric-Based Prompting:** Providing detailed criteria for each star rating to guide the model.
3.  **Reflexion (Self-Correction):** A multi-step prompt asking the model to reason first, then critique its own prediction before outputting the final score.

**Results:**
The **Reflexion** method proved to be the most robust, offering the best balance between accuracy and JSON validity. Full evaluation metrics and confusion matrices can be found in the notebook.

---

## 📊 Task 2: Two-Dashboard AI Feedback System

**Objective:** Build a web-based system with a public-facing User Dashboard for submitting reviews and an internal Admin Dashboard for analyzing them.

**Features:**
* **User Dashboard:**
    * Simple UI for users to rate and review products.
    * **Real-time AI Response:** The app instantly generates a polite, context-aware reply to the user upon submission.
* **Admin Dashboard:**
    * **Live Feed:** Displays incoming reviews in real-time.
    * **AI Summarization:** Automatically condenses long reviews into 5-10 word summaries.
    * **Actionable Insights:** The AI suggests concrete "Next Actions" for the business based on the sentiment of the review (e.g., "Investigate delivery delay").

**Tech Stack:**
* **Frontend/Backend:** Streamlit (Python)
* **AI Model:** OpenAI `gpt-4o-mini`
* **Data Storage:** Local JSON (simulated persistence for this assessment)

---

## 🛠️ Local Installation & Usage

If you wish to run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/aymanbhaldar/Fynd-AI
    cd Fynd-AI
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up credentials:**
    * Create a `.streamlit` folder in the root directory.
    * Create a `secrets.toml` file inside it.
    * Add your OpenAI API key:
        ```toml
        OPENAI_API_KEY = "sk-proj-..."
        ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

---

**Author:** Ayman Bhaldar
**Date:** December 2025
