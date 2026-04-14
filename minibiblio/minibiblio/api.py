import datetime
from ninja import NinjaAPI, Schema
from typing import List, Optional
from .models import Llibre 

api = NinjaAPI()

class LlibreOut(Schema):
    id: int
    titol: str
    autor: str
    data_edicio: datetime.date
    resum: Optional[str] = None
    imatge: Optional[str] = None

@api.get("/llibres", response=List[LlibreOut])
def obtenir_libres(request):
    llibres = Llibre.objects.all()
    return llibres