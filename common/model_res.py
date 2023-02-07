# common/model_res.py
from pydantic import BaseModel


class ServerInfo(BaseModel):
    server_id: int
    server_name: str
    cpu_rate: int
    mem_rate: int


# common/model_res.py
class Article(BaseModel):
    article_id: int
    title: str
    author: str
    hit: int
    like: int
    content: str
    save_date: str


# common/model_res.py
class Email_detail(BaseModel):
    mail_id: int
    title: str
    sender: str
    recipient: str
    cc: str
    contents: str


# common/model_res.py
class ResWrite(BaseModel):
    status: int = 1000
    article_id: int
