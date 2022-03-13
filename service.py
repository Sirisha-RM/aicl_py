
from time import time
from urllib import request
from fastapi import FastAPI
from fastapi import FastAPI,Request
from typing import Optional
from pydantic import BaseModel
from typing import List
import pybase64 
import time

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


#HTML LIBRARY
from fastapi.responses import HTMLResponse#to render the output in HTML format- text to HTML
from fastapi.staticfiles import StaticFiles#to access the files and folders that web app needs
from fastapi.templating import Jinja2Templates#render the output in HTML format -file to html



app = FastAPI()
@app.get("/hello/{my_query}")
async def home(my_query, q:Optional[str]=None):
    return{"siri":"prathi","user_input":my_query,"query":q}

class PROFILE(BaseModel):
    name: str
    age: int #str int bool-mandatory
    DOB: str
    hobby:Optional[list]#keyvalue pairs-name,age,dev,hobby
    skills:Optional[list]
    interests:List[str]

class COLLEGESTUDENT(BaseModel):
    name:str
    rollno:int
    course:str
    branch:str
    collegename:str
    yop:int
    student:bool

app = FastAPI()
@app.put("/endpoint")
async def endpoint(user: PROFILE):
    return{"username": user.name,"userage":user.age,"userDOB":user.DOB,"userskills":user.skills,"userinterests":user.interests}
    
@app.post("/mypostendpoint")
async def mypostendpoint(stud: COLLEGESTUDENT):
    return{"studname": stud.name,"studrollno":stud.rollno,"studcourse":stud.course,"studbranch":stud.branch,"studcollegename":stud.collegenamecan}

@app.get("/mySecureEndpoint")
async def mysecureendpoint(token:str):
    
    file=eval(str(open("token.txt","r+").readlines()))#we'll get list function if we use readlines function,sp we're directly read files from here

    for each in file:
        if token in each:
            authorisation="welcome home!"
            break
        else:
            authorisation="get out!"
            pass 
    return{"server_pass":authorisation}
    #ctrl+/ -to stop particular lines from execution
    authToken ="YWljbHB5dGhvbndlYg"
    if token!="" and token==authToken:
        authorisation="welcome home!"
    else :
        authorisation="get out!"
        return{"server.pass": authorisation}#we call as server pass

app = FastAPI()
@app.get("/token")
async def tokenGenerator():
    timenow = bytes(str(time.time()),"utf-8")
    token= pybase64.b64encode(timenow, altchars='_:')
    with open("token.txt","a+")as tokenfile:
        tokenfile.write(str(token)+"|\n")#|-token.txt file
        return {"token":token}


app = FastAPI()
@app.get("/mypage/", response_class=HTMLResponse)
async def mypage():
    html_code="""
            <html>
            <head>
            </head>
            <body>
            <h1>HOLA
            </body>
            </html>
    
     """ 
    return html_code

app = FastAPI()# class is initialised
app= app.mount("/static",StaticFiles(directory="static"),name="static") 
templates = Jinja2Templates(directory="templates") 


app = FastAPI()
@app.get("/htmlfile", response_class=HTMLResponse)
async def mypage(request:Request):
    return templates.TemplateResponse('index.html',context={'request':request})


    