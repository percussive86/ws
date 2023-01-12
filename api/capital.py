from fastapi import APIRouter

from contents.capital_list import city_info

router = APIRouter()


@router.post("/get-country-by-city", tags=["post"])
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


@router.post("/get-city-by-country", tags=["post"])
async def city_by_country(country: str):
    """
    국가를 입력하면 수도가 무엇인지 알려주는 함수
    :param country: 국가 이름 (한글)
    :return: 수도 이름 (한글)
    """

    # TODO :: response 값을 만들어 보세요
    response = None

    return response

