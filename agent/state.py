from typing import Annotated, TypedDict, Optional
from langgraph.graph.message import add_messages


class UserProfile(TypedDict, total=False):
    budget: Optional[str]
    budget_min: Optional[float]
    budget_max: Optional[float]
    use_case: Optional[str]           # commute, family, off-road, sport, etc.
    annual_mileage: Optional[int]
    ownership_preference: Optional[str]  # buy, lease, finance, open
    fuel_preference: Optional[str]    # gas, hybrid, electric, any
    passengers: Optional[int]
    cargo_needs: Optional[str]        # low, medium, high
    home_charging: Optional[bool]
    location: Optional[str]
    timeline: Optional[str]


class CarBuyingState(TypedDict):
    messages: Annotated[list, add_messages]
    user_profile: UserProfile
    recommendations: list[dict]
    comparison_table: Optional[list[dict]]
    ownership_advice: Optional[str]
    missing_info: list[str]
    step: str  # gather, recommend, compare, advise, complete
