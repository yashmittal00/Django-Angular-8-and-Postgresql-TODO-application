from todoApp.viewsets import todoAppViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todoApp' , todoAppViewSets),

#localhost:8000/api/
