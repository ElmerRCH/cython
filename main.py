from fastapi import FastAPI, UploadFile, Form, Response
import subprocess
import ejemplo

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        result = subprocess.run(
            ["python", "setup.py", "build_ext", "--inplace"],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e.stderr}")

@app.get("/")
async def root(response: Response = Response()):
    response.status_code = 403
    return 'hola'

@app.get("/cargar-cython")
async def cython(response: Response = Response()):
    result = subprocess.run(["python", "setup.py", "build_ext", "--inplace"], capture_output=True, text=True)
    return 'echo'

@app.get("/llamar-cython")
async def cython(response: Response = Response()):
    n =  ejemplo.sum_of_squares(10)
    return 'echo'

@app.get("/llamar-normal")
async def cython(response: Response = Response()):
    n = sum_of_squares(10)
    return 'echo'
    
def sum_of_squares(n):
    total = 0
    for i in range(n):
        total += i * i
    return total
