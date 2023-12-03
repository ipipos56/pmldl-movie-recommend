import pandas as pd
from surprise import Dataset, Reader, KNNBasic, dump
from surprise.model_selection import train_test_split
from surprise import accuracy


model_filename = '../models/collaborative_filtering_model'
loaded_model = dump.load(model_filename)[1]


# Function to get movie recommendations for a user
def get_top_n_recommendations(predictions, user_id, n=10):
    user_predictions = [pred for pred in predictions if pred.uid == user_id]
    user_predictions.sort(key=lambda x: x.est, reverse=True)
    return user_predictions[:n]


# read u1.test
u1_test = pd.read_csv('/data/u1.test', sep='\t', header=None)
u1_test.columns = ['user_id', 'item_id', 'rating', 'timestamp']

# Create Surprise Dataset
reader = Reader(rating_scale=(1, 5))

# Evaluate the model on the test set (u1_test)
test_data = Dataset.load_from_df(u1_test[['user_id', 'item_id', 'rating']], reader)
testset = test_data.build_full_trainset().build_testset()
test_predictions = loaded_model.test(testset)

# Calculate RMSE and MAE for the test set
test_rmse = accuracy.rmse(test_predictions)
test_mae = accuracy.mae(test_predictions)

print(f"\nTest Set RMSE: {test_rmse}")
print(f"Test Set MAE: {test_mae}")
