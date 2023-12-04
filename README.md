# Practical Machine Learning and Deep Learning - Assignment 2 - Movie Recommender System

## Author
- Name: Artur Eremov
- Email: a.eremov@innopolis.university
- Group Number: B20-RO-01

## Overview
This repository contains the implementation and documentation of a movie recommender system developed as part of the Practical Machine Learning and Deep Learning course assignment.

## Assignment Description
A recommender system is a type of information filtering system that suggests items or content to users based on their interests, preferences, or past behavior. In this assignment, we have created a movie recommender system that suggests movies to users based on their demographic information (age, gender, occupation, zip code) and favorite movies (list of movie IDs). The assignment involves implementing a machine learning model, creating a benchmark for evaluation, and documenting the process.

## Dataset
I used the [MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/), which consists of 100,000 ratings from 943 users on 1682 movies. The dataset includes user demographics, movie information, and user ratings.

## Repository Structure
The repository is organized as follows:

- `data`: Contains directories for external, interim, and raw data.
- `models`: For trained and serialized models or final checkpoints.
- `notebooks`: Jupyter notebooks for data exploration and solution implementation.
- `reports`: Documentation and reports, including figures and the final report.
- `benchmark`: Contains the dataset used for evaluation and the evaluation script.

## Report Structure
The report for this assignment follows the structure below:

### Introduction
A recommender system is a vital tool in modern information systems, providing personalized recommendations to users. In this assignment, we aim to build a movie recommender system using collaborative filtering techniques.

### Data Analysis
I started by loading and exploring the MovieLens 100K dataset. The data consists of 100,000 ratings from 943 users on 1682 movies. We analyzed user demographics, movie details, and the distribution of ratings.

### Model Implementation
I implemented a collaborative filtering recommender system using the Surprise library in Python. The KNNBasic algorithm with cosine similarity was chosen for its simplicity and effectiveness in capturing user-item interactions.

### Model Advantages and Disadvantages
#### Advantages
- **Personalization**: The model provides personalized recommendations based on user preferences.
- **Scalability**: Collaborative filtering is scalable and can handle large datasets.
- **No Need for Feature Engineering**: Collaborative filtering does not require explicit feature engineering.

#### Disadvantages
- **Cold Start Problem**: The model struggles with new users or items with limited interaction history.
- **Sparsity**: The user-item interaction matrix can be highly sparse, affecting the model's accuracy.
- **Lack of Interpretability**: Collaborative filtering models lack transparency in explaining recommendations.

### Training Process
I trained the model on the MovieLens dataset, splitting it into training and test sets to assess its performance. The training parameters were set to default values for simplicity.

### Evaluation
I evaluated the model using both the training set and a separate test set (`u1_test`). The evaluation metrics included Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE). The results showed that the model performed reasonably well in predicting user preferences.

### Results
The model achieved the following results:

- **Training Set RMSE**: 0.8640246570455596
- **Training Set MAE**: 0.6765519172465901

- **Test Set RMSE**: 0.826080041507462
- **Test Set MAE**: 0.6474142119506778

These metrics provide insights into the model's performance, with lower values indicating better accuracy. Further optimizations and experimentation with different algorithms can be explored to improve the recommender system's effectiveness.

## How to Run
To reproduce the work and run the movie recommender system, follow these steps:

1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the Jupyter notebooks in the `notebooks` directory for data exploration and solution implementation.
4. Use the provided evaluation script in the `benchmark` directory to assess the model's performance.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
I would like to acknowledge the MovieLens dataset and the Surprise library for their contributions to this project.

