from fastapi import FastAPI

app = FastAPI()
@app.get('/')
async def name():
    return {'ФИО':'Юрьев Максим Андреевич'}
@app.get('/users')
async def name():
    return {'Контактные данные':'8-913-333-**-**'}
@app.get('/tools')
async def name():
    return {'Навыки разработчика':'Начал знакомство с FastAPI'}
