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
    portada_url: Optional[str] = None

@api.get("/llibres", response=List[LlibreOut])
def obtenir_libres(request):
    llibres = Llibre.objects.all()
    for llibre in llibres:
        if hasattr(llibre, 'portada') and llibre.portada:
            llibre.portada_url = request.build_absolute_uri(llibre.portada.url)
        else:
            llibre.portada_url = None
    return llibres