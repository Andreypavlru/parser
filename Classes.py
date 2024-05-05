from pydantic import BaseModel, Field

class ResultRace(BaseModel):
    qualification: str = Field(default = '0')
    rating: str = Field(default = '0')

class TableRow(BaseModel):
    place: list[int] = Field()
    car_name: list[int] = Field()
    driver_name: list[str] = Field()
    races: list[ResultRace] = Field()
    total_rating: list[int] = Field()


def TableRow_get_result(dict: dict):
    table = TableRow(**dict)
    print(table)
    return table