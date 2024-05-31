from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.apps.influencer_search.logics.influencers import InfluencersLogic
from src.apps.influencer_search.models import Influencers, InfluencerFilters
from src.utils.response_handlers import response

"""
    our router classs would hold all the endpoints dedicated to this app.
    
    we are using response wrapper function to keep the uniformed response throughout the project.
"""


router = APIRouter(prefix="/influencers", tags=["influencers"])


@router.get("/", response_model=List[Influencers])
@response
async def read_all_influencers():
    data = await InfluencersLogic().get_all_influencers()
    print(data)
    return data


@router.get("/filter", response_model=List[Influencers])
@response
async def read_influencers(filters: InfluencerFilters = Depends()):
    if not any(filters.dict().values()):
        filter_options = ", ".join(filters.__fields__.keys())
        raise HTTPException(status_code=400,
                            detail=f"At least one filter criteria must be provided. Available filter options: {filter_options}")

    return await InfluencersLogic().filter_influencers(filters)
