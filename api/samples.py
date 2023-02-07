from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from common.model_req import member_info
from common.model_res import ServerInfo

import psutil


router = APIRouter()


@router.get("/test1", tags=["get"])
async def test1():
    """
    입력값이 없고, text를 돌려주는 API
    :return:
    """

    return "Text를 돌려줍시다"


@router.get("/test2", tags=["get"])
async def test2(name: str, score: int):
    """
    입력값을 url로 받고 text를 돌려주자"
    :return:
    """

    grade = "F"

    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    else:
        grade = "F"

    return f"{name}님의 등급은 {grade}입니다"


@router.get("/test3", tags=["get"])
async def test3(value: int = 10):
    square_number = value * value

    return f"{value} 의 제곱수는 {square_number} 입니다"


@router.post("/test4", tags=["post"])
async def test4(info: member_info):
    print(f"{info.id}:{info.name}/{info.email}")

    return f"{info.name}님의 회원 가입이 완료되었습니다"


import psutil

@router.get("/res_test1", tags=["get"], response_model=ServerInfo)
async def res_test1():

    info = ServerInfo(
        server_id=1,
        server_name="MYPC",
        cpu_rate=psutil.cpu_percent(),
        mem_rate=psutil.virtual_memory().percent
    )

    json_info = jsonable_encoder(info)
    return JSONResponse(content=json_info)


#samples.py
from common.model_res import Article


@router.get("/res_test2/{article_id}", tags=["get"], response_model=Article)
async def res_test2(article_id: int):

    # article_id 로 DB select

    article = Article(
        article_id=2,
        title="안녕하세요",
        author="테스터",
        hit=3,
        like=1,
        content="첫번째 게시글 입니다",
        save_date="2023-02-07 17:00:01"
    )

    json_info = jsonable_encoder(article)
    return JSONResponse(content=json_info)


#samples.py
from common.model_req import ReqWrite
from common.model_res import ResWrite
from common.util import id_generator

gen = id_generator()

@router.post("/res_test3", tags=["post"], response_model=ResWrite)
async def res_test3(item: ReqWrite):

    print(item.user_id, item.title, item.content, item.save_date)

    res = ResWrite(
        status=1000,
        article_id=next(gen)
    )

    json_info = jsonable_encoder(res)
    return JSONResponse(content=json_info)
