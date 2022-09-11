from fastapi import FastAPI

from application.user_data.router import router as user_data_router


app = FastAPI(redoc_url=None, title='x-lab-test')
app.include_router(user_data_router, prefix='', tags=['user-data'])
