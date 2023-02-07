# common/model_req.py
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


class member_info(BaseModel):
    """
    회원가입 필요정보
    """

    id: str
    name: str
    email: str


class bbs_write(BaseModel):
    user_id: str
    title: str
    secret: bool
    text: str


from typing import Optional
# common/model_req.py
class ReqWrite(BaseModel):
    user_id: str
    title: str
    content: str
    save_date: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "user_id": 102,
                "title": "게시글 제목을 입력하세요",
                "content": "게시글 내용을 입력하세요",
                "save_date": "YYYY-mm-dd HH:MI:SS",
            }
        }


class EmailWrite(BaseModel):
    sender: str
    recipient: str
    cc: str
    title: str
    text: str
