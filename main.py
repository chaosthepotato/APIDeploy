#Main
import json
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

with open("Pesanan.json", "r") as read_file:
    Item = json.load(read_file)

with open("Produk.json", "r") as read_file:
    Produk = json.load(read_file)

with open("Member.json", "r") as read_file:
    Member = json.load(read_file)

@app.get('/')
def root():
    return{'pesanan':'Item'}

@app.get("/produk", response_model=List[Produk])
@app.get("/produk")
async def read_all_product():
    return Produk

@app.get("/produk/{id_produk}/")
async def read_produk(id_produk: str): 
    for id_produk in Produk['Produk']:
        if id_produk['id_produk'] == id_produk:
            return id_produk
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

@app.get("/pesanan/{id_pesanan}/")
async def read_pesanan(id_pesanan: str): 
    for id_pesanan in Pesanan['Pesanan']:
        if id_pesanan['id_pesanan'] == id_pesanan:
            return id_pesanan
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

@app.get("/profile/{username}/")
async def read_pesanan(id_pesanan: str): 
    for username in Member['Member']:
        if username['username'] == username:
            return username
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

@app.post('/pesanan')
async def post_pesanan(id_pesanan:str):
    id = 1
    if(len(Pesanan["Pesanan"]) > 0):
        id = Pesanan["Pesanan"][len(Pesanan["Pesanan"]) - 1]["id_pesanan"] + 1
    new_data = {'id_pesanan':id, 'id_pesanan':id_pesanan}
    Pesanan['Pesanan'].append(dict(new_data))
    read_file.close()
    
    with open("Pesanan.json", "w") as write_file: 
        json.dump(Pesanan,write_file, indent=4)
    write_file.close()

    return (new_data)
    raise HTTPException(
        status_code=500, detail=f'Internal Server Error'
        )
