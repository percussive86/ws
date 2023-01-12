from fastapi import APIRouter
from common.model_req import Rectangle

router = APIRouter()


@router.post("/rectangle-area", tags=["post"])
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
