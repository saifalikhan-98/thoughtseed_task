import numpy as np
import pandas as pd

from src.apps.influencer_search.models import InfluencerFilters, Influencers
from typing import Optional
from src.db import db

class InfluencersLogic:

    """
        In init function we are loading the in memory dataset loaded at the initializing server running server
    """

    def __init__(self):
        self.__influencer_data = db.influencer_data
    """
        the below method gets all influencers
    """
    async def get_all_influencers(self) -> list:
        all_influencers = self.convert_to_str(self.__influencer_data)
        all_influencers = all_influencers.to_dict(orient='records')
        return all_influencers
    """
        in the below method, we are applying filter to the in memory dataset , 
        InfluencerFilters models give all the available filter option
        
        We iterate the filters requested by user and process the filters on
        every datasets if the value of that filter field is not null
    """
    async def filter_influencers(self, filters: InfluencerFilters) -> list:
        filtered_df = self.__influencer_data.copy()

        for field, value in filters.dict().items():
            if value is not None:
                field=field.replace("min_","")
                field=field.replace("max_","")
                if field in filtered_df.columns:
                    column_dtype = filtered_df[field].dtype
                    if np.issubdtype(column_dtype, np.number):
                        filtered_df = filtered_df[filtered_df[field] == value]
                    else:
                        filtered_df = filtered_df[filtered_df[field] == str(value)]

        filtered_df = self.convert_to_str(filtered_df)
        return filtered_df.to_dict(orient='records')

    @staticmethod
    def convert_to_str(df: pd.DataFrame) -> pd.DataFrame:
        # Convert numeric fields to string using the convert_to_str method defined in Influencers model
        return df.apply(lambda x: x.apply(Influencers.convert_to_str) if x.dtype == 'float64' else x)