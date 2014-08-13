from app.views import CidadeViewSet, BairroViewSet, ImovelViewSet, SlideViewSet, ContatoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'cidades' , CidadeViewSet )
router.register(r'bairros' , BairroViewSet )
router.register(r'imoveis' , ImovelViewSet )
router.register(r'slides'  , SlideViewSet  )
router.register(r'contatos', ContatoViewSet)
urlpatterns = router.urls