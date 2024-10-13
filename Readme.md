# Perfume Recommendation System

## Overview

The Perfume Recommendation System is a web application built using Streamlit that recommends perfumes based on user-selected criteria. Users can filter perfumes by brand, price range, and location, and receive personalized recommendations based on their selection.

## Features

- **Brand Filter**: Select from various brands to narrow down the search results.
- **Price Range Filter**: Set a specific price range to find perfumes within your budget.
- **Location Filter**: Choose the item location to find perfumes available in a specific area.
- **Recommendation Engine**: Get recommendations for similar perfumes based on the selected title.

## Dataset

The application uses a CSV dataset containing information about various perfumes, including:

- `brand`: The brand of the perfume.
- `title`: The title/name of the perfume.
- `type`: The fragrance type.
- `price`: The price of the perfume.
- `priceWithCurrency`: The price with currency information.
- `availableText`: Availability status (e.g., "In Stock").
- `itemLocation`: The location where the item is available.

## Requirements

To run the application, ensure you have the following installed:

- Python 3.7 or higher
- Streamlit
- Pandas
- Scikit-learn

You can install the required packages using pip:

```bash
pip install streamlit pandas scikit-learn


1. Clone the repository
git clone <repository-url>
cd <repository-folder>

2. Prepare the Dataset:

Make sure your dataset (ebay_womens_perfume.csv) is available in the specified directory.
Update the file path in the code if necessary:

df = pd.read_csv('D:/Python Project/ebay_womens_perfume.csv')

3. Run the Application:

Open a terminal or command prompt.
Navigate to the folder containing the recommendation.py file.
Run the following command:

streamlit run recommendation.py

4. Access the Application:

After running the command, a new tab will open in your default web browser displaying the application.
You can now use the filters to explore the perfumes and get recommendations.

Usage
Use the sidebar to select your desired filters.
After selecting a perfume title from the filtered options, click the "Get Recommendations" button to view similar perfumes.

Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request.

Acknowledgements
Thank you to the contributors of the libraries used in this project: Streamlit, Pandas, and Scikit-learn.