# Tourist Recommender App 🌍

This project utilizes a dataset that was generated using **GitHub Copilot**. The dataset includes popular tourist destinations in India, classified based on different categories like **beach**, **nature**, **historical**, etc. This dataset is then used to train a machine learning model that helps users find the best destinations based on their preferences.
A Streamlit-powered app that recommends tourist destinations in India based on user preferences like budget, weather, region, and trip duration. This project uses machine learning to predict the ideal tourist category (e.g., beach, historical, nature) and suggest matching destinations.

## Features 🛠️

- **User Preferences**: Users can select their:
  - **Budget** (low, medium, high)
  - **Weather preference** (sunny, rainy, cold)
  - **Region** (North, South, East, West, Central)
  - **Trip Duration** (short, medium, long)

- **AI Recommendation**: The app uses a machine learning model to recommend destinations based on the input criteria and predicts the best destination category (Beach, Historical, Nature, etc.).

- **Matching Destinations**: After category prediction, the app filters destinations and shows matching results with descriptions.

## Tech Stack ⚙️

- **Streamlit**: For creating the interactive web app.
- **Scikit-learn**: For machine learning model.
- **Pandas**: For data processing.
- **Joblib**: For saving and loading the trained model.
- **GitHub**: For version control and hosting the repository.

## Installation 📥

1. **Clone the repo**:

    ```bash
    git clone https://github.com/Charmi-ptl/tourist-recommender-india.git

2. **Install dependencies**:

    You’ll need Python 3.6 or higher. Run the following to install required libraries:
    ```bash
    pip install -r requirements.txt
    
    Make sure you have the following in your `requirements.txt` file:
    streamlit
    pandas
    scikit-learn
    joblib

3. **Run the app**:

    Navigate to the project directory and run:
    ```bash
    streamlit run app.py
    This will open the app in your browser.

## File Structure 📁

tourist-recommender-india/ │ ├── app.py # Streamlit app file ├── tourist_model.pkl # Trained machine learning model ├── label_encoder.pkl # Label encoder for model predictions ├── destination_data_india.csv # CSV file with destinations data ├── requirements.txt # Python dependencies └── README.md # Project documentation


## How It Works 🔧

1. **Data Collection**: The `destination_data_india.csv` file contains a list of popular tourist destinations in India, including their category, weather, region, budget, and description. The dataset was generated with the help of **GitHub Copilot**.
2. **Model Training**: A machine learning model was trained to predict the destination category based on the user's preferences (budget, weather, region, trip duration). The model is saved in the `tourist_model.pkl` file.
3. **User Interaction**: Users input their preferences in the Streamlit app, which then:
   - Encodes the inputs.
   - Uses the trained model to predict a destination category.
   - Filters matching destinations and displays them with descriptions.

## Contributing 🤝

We welcome contributions to improve the app! Here’s how you can contribute:
1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Open a pull request

Thanks for checking out the **Tourist Recommender App**! ✈️ Enjoy your travels! 🌍
