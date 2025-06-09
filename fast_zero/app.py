from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def rear_root():
    return {'message': 'Olá Mundo'}
