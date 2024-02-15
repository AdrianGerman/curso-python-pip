import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4,5,6,7]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola, desde fastapi</h1>
    """

def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()