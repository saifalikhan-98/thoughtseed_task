from pydantic import BaseModel, Field, validator, field_validator
from typing import Optional
from src.utils.convert_format import format_number

"""
    This model holds all the fields present in Dataset csv file
"""
class Influencers(BaseModel):
    rank: str
    channel_info: str
    influence_score: str
    posts: str
    followers: str
    avg_likes: str
    day_60_eng_rate: str = Field(..., alias='60_day_eng_rate')
    new_post_avg_like: str
    total_likes: str
    country: str

    """
        we are converting numbers back to str before we send it as a response,
        Although the conversion and maintaining the value in str and numbers is tedious task
        It is only being done so that the value is returned as it is in dataset
    """
    @field_validator('rank', 'influence_score', 'posts', 'followers', 'avg_likes', 'day_60_eng_rate', 'new_post_avg_like', 'total_likes')
    def convert_to_str(cls, v):
        return format_number(v)

    @field_validator('day_60_eng_rate', )
    def add_percentage(cls, v):
        return f"{format_number(v)}%"



    class Config:
        from_attributes = True
        populate_by_name = True

"""
    This class holds all the available filter options
"""
class InfluencerFilters(BaseModel):
    min_rank: Optional[int] = Field(None, ge=1)
    rank: Optional[int] = Field(None, ge=1)
    max_rank: Optional[int] = Field(None, ge=1)
    channel_info: Optional[str] = None
    min_influence_score: Optional[float] = Field(None, ge=0)
    influence_score: Optional[float] = Field(None, ge=0)
    max_influence_score: Optional[float] = Field(None, ge=0)
    min_posts: Optional[float] = Field(None, ge=0)
    posts: Optional[float] = Field(None, ge=0)
    max_posts: Optional[float] = Field(None, ge=0)
    min_followers: Optional[float] = Field(None, ge=0)
    followers: Optional[float] = Field(None, ge=0)
    max_followers: Optional[float] = Field(None, ge=0)
    min_avg_likes: Optional[float] = Field(None, ge=0)
    avg_likes: Optional[float] = Field(None, ge=0)
    max_avg_likes: Optional[float] = Field(None, ge=0)
    min_day_60_eng_rate: Optional[float] = Field(None, ge=0.0, alias='60_day_eng_rate')
    day_60_eng_rate: Optional[float] = Field(None, ge=0.0, alias='60_day_eng_rate')
    max_day_60_eng_rate: Optional[float] = Field(None, ge=0.0, alias='60_day_eng_rate')
    min_new_post_avg_like: Optional[float] = Field(None, ge=0)
    new_post_avg_like: Optional[float] = Field(None, ge=0)
    max_new_post_avg_like: Optional[float] = Field(None, ge=0)
    min_total_likes: Optional[float] = Field(None, ge=0)
    total_likes: Optional[float] = Field(None, ge=0)
    max_total_likes: Optional[float] = Field(None, ge=0)
    country: Optional[str] = None

    class Config:
        from_attributes = True
        populate_by_name = True
