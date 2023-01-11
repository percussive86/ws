from fastapi import FastAPI

import pytz
from datetime import datetime

from common.model_req import WorldTime, Rectangle
from contents.capital_list import city_info


app = FastAPI()


@app.get("/")
def read_root():
    """
    Hello World!
    :return: "Test Project by FastAPI"
    """
    return "Test Project by FastAPI"


@app.post("/api/world-time")
async def world_time(item: WorldTime):
    """
    지역코드를 받아서 현재 시간을 리턴한다.
    나중에는 도시이름을 받아서 처리하도록 기능을 추가해보자. (City name to Timezone)
    :param item: WorldTime
    :return: "년-월-일 시:분:초"
    """

    tz = pytz.timezone(item.timezone)
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")


@app.post("/api/timezone-list")
async def timezone_list():
    """
    timezone 리스트를 알 수 있다
    :return: list
    """

    return pytz.all_timezones


@app.post("/api/get-country-by-city")
async def country_by_city(city: str):
    """
    수도를 입력하면 어느 국가의 수도인지 알려주는 함수
    :param city: 수도 이름 (한글)
    :return: 국가 이름 (한글)
    """

    if city in city_info:
        response = city_info[city]
    else:
        response = f"{city}를 수도로 하는 국가정보를 찾을 수 없습니다."
    return response


@app.post("/api/get-city-by-country")
async def city_by_country(country: str):
    """
    국가를 입력하면 수도가 무엇인지 알려주는 함수
    :param country: 국가 이름 (한글)
    :return: 수도 이름 (한글)
    """

    # TODO :: response 값을 만들어 보세요
    response = None

    return response


@app.post("/api/rectangle-area")
async def rectangle_area(item: Rectangle):
    """
    밑변, 높이 값이 주어지면 사각형의 면적을 구해주는 함수
    width, height 값이 필수로 들어와야 한다
    :param item: Rectangle
    :return:
    """

    # TODO :: response 값을 만들어 보세요
    response = 0
    return response
