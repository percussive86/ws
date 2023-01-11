from pydantic import BaseModel


class WorldTime(BaseModel):
    """
    세계시간 API에 사용하는 class
    timezone 은 pytz에서 제공하는 리스트여야 한다
    """
    timezone: str = 'UTC'


class Rectangle(BaseModel):
    """
    사각형의 정보
    """

    x_point: int = 0
    y_point: int = 0
    width: int
    height: int

