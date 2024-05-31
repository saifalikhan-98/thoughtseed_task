import pandas as pd
from src.utils.convert_format import convert_to_number


class Database:
    def __init__(self):
        self.influencer_data = self.prepare_influencer_dataset()

    """
        here we load the dataset from csv file using pandas.
        then we convert all the number from str to number so that we can perform filter operation
    """
    def prepare_influencer_dataset(self):
        # Preprocess the dataframe
        self.influencer_data = pd.read_csv("src/top_insta_influencers_data.csv")
        self.influencer_data.fillna("", inplace=True)  # Handle missing values if necessary
        self.influencer_data.fillna("", inplace=True)  # Handle missing values if necessary
        self.influencer_data['posts'] = self.influencer_data['posts'].apply(convert_to_number)
        self.influencer_data['followers'] = self.influencer_data['followers'].apply(convert_to_number)
        self.influencer_data['avg_likes'] = self.influencer_data['avg_likes'].apply(convert_to_number)
        self.influencer_data['60_day_eng_rate'] = self.influencer_data['60_day_eng_rate'].apply(convert_to_number)
        self.influencer_data['new_post_avg_like'] = self.influencer_data['new_post_avg_like'].apply(convert_to_number)
        self.influencer_data['total_likes'] = self.influencer_data['total_likes'].apply(convert_to_number)
        return self.influencer_data

# Initialize the database
db = Database()
