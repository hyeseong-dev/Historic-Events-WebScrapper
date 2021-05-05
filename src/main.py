import services as _services
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'welcome to this cool historial events api'}

@app.get('/events')
async def events():
    return _services.get_all_events()

@app.get('/events/{month}')
async def events_of_month(month: str):
    return _services.month_events(month)

@app.get('/events/{month}/{day}')
async def events_of_day(month: str, day: int):
    return _services.day_events(month,day)

@app.get('/evnets/today')
async def today():
    return _services.todays_events()