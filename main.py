from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome():
    return {'success': True, 'message': 'Welcome to the FastAPI', }