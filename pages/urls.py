from django.urls import path
from .views import *
from pages.utils import ImageLocalStorage
	
urlpatterns = [
	    path('', HomePageView.as_view(), name="home"),
        path('about/', AboutPageView.as_view(), name='about'),
        path('contacts/', ContactsPageView.as_view(), name='contacts'),
        path('products/', ProductIndexView.as_view(), name='index'),
        path('products/create', ProductCreateView.as_view(), name='form'),
        path('products/<str:id>', ProductShowView.as_view(), name='show'),
        path('monda', MessagePageView.as_view(), name='message'),
        path('cart/', CartView.as_view(), name='cart_index'),
        path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
        path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
        path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
        path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
        path('image-not-di/', ImageViewNoDI.as_view(), name='imagenodi_index'),
        path('image/save', ImageViewNoDI.as_view(), name='imagenotdi_save'), 


	]
