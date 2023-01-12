from fastapi import APIRouter
from common.model_req import WorldTime

import pytz
from datetime import datetime

router = APIRouter()


@router.post("/world-time", tags=["post"])
async def world_time(item: WorldTime):
    """
    지역코드를 받아서 현재 시간을 리턴한다.
    나중에는 도시이름을 받아서 처리하도록 기능을 추가해보자. (City name to Timezone)
    :param item: WorldTime
    :return: "년-월-일 시:분:초"
    """

    tz = pytz.timezone(item.timezone)
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")


@router.get("timezone-list", tags=["get"])
async def timezone_list():
    """
    timezone 리스트를 알 수 있다
    :return: list
    """

    return pytz.all_timezones
