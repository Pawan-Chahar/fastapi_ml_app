# FastAPI + Streamlit ML App - Insurance Premium Category Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-red)
![scikit--learn](https://img.shields.io/badge/scikit--learn-1.5+-orange)

A complete **end-to-end Machine Learning application** that predicts **Insurance Premium Categories** using a trained ML model, served via **FastAPI** backend and a beautiful **Streamlit** frontend.

## Project Overview

This project demonstrates a production-ready ML deployment pattern:
- Train a classification model on health/insurance data
- Save the model using pickle
- Expose prediction endpoint with **FastAPI**
- Build an interactive user interface with **Streamlit**
- Simple, clean, and easy to deploy (Docker-ready in future)

**Use case**: Predict whether an insurance premium falls into **Low**, **Medium**, **High** (or similar) category based on patient features like age, BMI, smoking status, children, region, etc.

## Folder & File Structure

fastapi_ml_app/
├── .venv/                    # Virtual environment (git ignored)
├── pycache/              # Python cache (git ignored)
├── pydantic/                 # Pydantic models / schemas (if used)
├── README.md                 # This file
├── app.py                    # Main FastAPI application (API endpoints)
├── main.py                   # Alternative/alternate entry point (sometimes used)
├── frontend.py               # Streamlit frontend application
├── fastapi_ml_model.ipynb    # Jupyter notebook - model training & experimentation
├── insurance.csv             # Dataset used for training (Medical Cost Personal Datasets or similar)
├── model.pkl                 # Trained & serialized ML model (pickle format)
├── patient.json              # Sample input JSON for testing the API
└── requirements.txt          # All Python dependencies



## Tech Stack

- **Backend/API**: FastAPI (modern, fast, async Python web framework)
- **Frontend/UI**: Streamlit (quick & beautiful data apps)
- **Machine Learning**: scikit-learn (RandomForest, XGBoost, or similar classifier)
- **Model Serialization**: pickle
- **Data Handling**: pandas, numpy
- **Validation**: Pydantic (likely used in API)

## How to Run the Project Locally

### 1. Clone the repository

Here is a well-structured, professional **README.md** file for your GitHub repository:  
https://github.com/Pawan-Chahar/fastapi_ml_app

You can copy-paste this content directly into your `README.md` file (or create one if it doesn't exist yet).

```markdown
# FastAPI + Streamlit ML App - Insurance Premium Category Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-red)
![scikit--learn](https://img.shields.io/badge/scikit--learn-1.5+-orange)

A complete **end-to-end Machine Learning application** that predicts **Insurance Premium Categories** using a trained ML model, served via **FastAPI** backend and a beautiful **Streamlit** frontend.

## Project Overview

This project demonstrates a production-ready ML deployment pattern:
- Train a classification model on health/insurance data
- Save the model using pickle
- Expose prediction endpoint with **FastAPI**
- Build an interactive user interface with **Streamlit**
- Simple, clean, and easy to deploy (Docker-ready in future)

**Use case**: Predict whether an insurance premium falls into **Low**, **Medium**, **High** (or similar) category based on patient features like age, BMI, smoking status, children, region, etc.

## Folder & File Structure

```
fastapi_ml_app/
├── .venv/                    # Virtual environment (git ignored)
├── __pycache__/              # Python cache (git ignored)
├── pydantic/                 # Pydantic models / schemas (if used)
├── README.md                 # This file
├── app.py                    # Main FastAPI application (API endpoints)
├── main.py                   # Alternative/alternate entry point (sometimes used)
├── frontend.py               # Streamlit frontend application
├── fastapi_ml_model.ipynb    # Jupyter notebook - model training & experimentation
├── insurance.csv             # Dataset used for training (Medical Cost Personal Datasets or similar)
├── model.pkl                 # Trained & serialized ML model (pickle format)
├── patient.json              # Sample input JSON for testing the API
└── requirements.txt          # All Python dependencies
```

## Tech Stack

- **Backend/API**: FastAPI (modern, fast, async Python web framework)
- **Frontend/UI**: Streamlit (quick & beautiful data apps)
- **Machine Learning**: scikit-learn (RandomForest, XGBoost, or similar classifier)
- **Model Serialization**: pickle
- **Data Handling**: pandas, numpy
- **Validation**: Pydantic (likely used in API)

## How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Pawan-Chahar/fastapi_ml_app.git
cd fastapi_ml_app
```

### 2. Create & activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI backend

```bash
uvicorn app:app --reload --port 8000
# or sometimes: python main.py
```

API will be available at:  
→ http://127.0.0.1:8000  
→ Docs/Swagger: http://127.0.0.1:8000/docs

### 5. Run the Streamlit frontend (in new terminal)

```bash
streamlit run frontend.py
```

Frontend will open at: http://localhost:8501

Now enter patient details → get instant premium category prediction!

## API Endpoint (example)

**POST** `/predict`

**Sample request body** (from patient.json):

```json
{
  "age": 28,
  "sex": "male",
  "bmi": 33.0,
  "children": 3,
  "smoker": "yes",
  "region": "southeast"
}
```

**Response example** (actual key may vary – check your code):

```json
{
  "predicted_category": "High",
  "probability": 0.87
}
```

## Development & Training

1. Open `fastapi_ml_model.ipynb` in Jupyter/VS Code
2. Explore data (`insurance.csv`)
3. Train/test model
4. Save final model as `model.pkl`

## Future Improvements (Roadmap)

- [ ] Add Docker + docker-compose support
- [ ] Implement model versioning
- [ ] Add authentication to API
- [ ] Deploy to Render / Railway / AWS / Heroku
- [ ] Add confidence/probability visualization in UI
- [ ] CI/CD with GitHub Actions

## Contributing

Feel free to open issues or PRs!  
Especially welcome: better model accuracy, UI enhancements, deployment guides.

## License

MIT License – feel free to use, modify, and distribute.

Made with ❤️ by [Pawan Chahar](https://github.com/Pawan-Chahar)

Last updated: January 2026
```

### Quick Tips Before Committing

- If your actual prediction key is **not** `predicted_category` (e.g. `category`, `prediction`, `premium_level`), update the example in the README.
- Add screenshots! (Streamlit UI + Swagger docs + notebook outputs) → upload to repo and link with `![screenshot](images/ui.png)`
- If you have a live demo link later (Render/HuggingFace/etc.), add it at the top!

Let me know if you want me to add sections (like screenshots placeholders, badges, or more detailed API examples) or adjust anything. Good luck with your project! 🚀
