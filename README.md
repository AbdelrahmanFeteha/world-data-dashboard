# world-data-dashboard
This repository contains an interactive dashboard built with Streamlit, designed to visualize and analyze the Gapminder dataset. The Gapminder dataset provides insights into global development trends across various countries and years, including metrics such as life expectancy, GDP per capita, and population.

## Features

- **Data Overview**: Examine the structure, unique values, and descriptive statistics of the dataset.
- **Time Series Analysis**: Analyze how metrics such as life expectancy, GDP per capita, and population have changed over time.
- **Comparative Analysis**: Compare different metrics across countries and continents.
- **Heatmap Analysis**: Visualize correlations between key metrics.
- **Box Plot Analysis**: Examine the distribution of metrics across continents.

## Technologies Used

- **Streamlit**: A framework for creating interactive web applications in Python.
- **Plotly Express**: A library for creating interactive plots and visualizations.
- **Pandas**: A data manipulation and analysis library for Python.

## Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/world-data-dashboard.git
    cd world-data-dashboard
    ```

2. **Create a Virtual Environment**

    ```sh
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Local Development

1. **Run the Streamlit Application**

    ```sh
    streamlit run app.py
    ```

2. **Open Your Web Browser**

    Navigate to `http://127.0.0.1:8501` to access the dashboard.

### Access the Deployed Application

You can access the deployed version of this dashboard directly at:

[World Data Dashboard](https://world-data-dashboard-abdelrahman-feteha.streamlit.app/#data-overview)

## Code Structure

- **`app.py`**: The main application file containing functions for various analyses and the navigation system.
- **`requirements.txt`**: A file listing the dependencies required to run the application.

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.
