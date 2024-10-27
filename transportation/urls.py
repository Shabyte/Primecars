
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
#for Routing

urlpatterns = [
    path('',views.home,name = 'home'),
    path('vehicle/',views.vehicle,name = 'vehicle'),
    path('vehicle/<int:pk>/details/',views.car_details,name = 'car_details'),
    path('drivers/',views.drivers,name = 'drivers'),
    path('drivers/details',views.driver_details,name = 'driver_details'),
    path("shop/", views.shop, name="shop"),
    path("shop/details", views.shop_details, name="shop_details"),
    path("contacts/", views.contacts, name="contacts"),
    path('createaccount/',views.createaacount, name='createaacount'),
    path('login/',views.signin, name='signin'),
    path('verify/',views.verify_email, name='verify_email'),
    path('logout/',views.logoutUser, name='logoutUser'),
    path("profile/",views.profile, name="profile"),
    #======================================================


    path('administrator/', views.admin, name='admin'),
    path('blank/', views.blank, name='blank'),
    path('list/admins/', views.list_administrators, name='list_administrators'),
    path('shops/', views.shops, name='shops'),
    path('shops/<int:pk>/', views.unlock_shops, name='unlock_shops'),
    path('published/cars/<int:pk>/', views.published_cars, name='published_cars'),
    path('vehicles/', views.vehicles_list, name='vehicles_list'),

    #======================================================
    path('primecars/', views.users, name='users'),
    path('my/registered/shops/', views.myshops, name='myshops'),
    path('my/registered/shops/<slug:slug>/edit/', views.edit_myshops, name='edit_myshops'),
    path('my/registered/shops/<slug:slug>/delete/', views.delete_myshops, name='delete_myshops'),
    path('my/shop/', views.mylistshop, name='mylistshop'),
    path('registered/shops/', views.registered_shops, name='registered_shops'),
    path('registered/shops/<slug:slug>/', views.details_shops, name='details_shops'), 

    path('myshop/details/<slug:slug>/', views.myshop_details, name='myshop_details'),
    path('myshop/vehicles/<slug:slug>/', views.vehicles, name='vehicles'),
    path('myshop/<slug:slug>/vehicles/edit/<int:pk>/', views.edit_vehicles, name='edit_vehicles'),
    path('myshop/<slug:slug>/vehicles/delete/<int:pk>/', views.delete_vehicles, name='delete_vehicles'),
    path('myshop/drivers/<slug:slug>/', views.shopdrivers, name='shopdrivers'),
    path('myshop/drivers/<slug:slug>/list/', views.mydrivers, name='mydrivers'),
    path('myshop/drivers/<slug:slug>/approved/<int:pk>/', views.approved_driver, name='approved_driver'),
    path('myshop/drivers/<slug:slug>/delete/<int:pk>/', views.delete_driver, name='delete_driver'),
    
    


    path('shop/<slug:slug>/unit/<int:pk>/', views.shop_unit, name='shop_unit'), 
    
    path('registered/vehicles/', views.registered_vehicles, name='registered_vehicles'),
    path('rent/vehicles/<int:pk>/', views.rent_vehicles, name='rent_vehicles'),
    path('rent/vehicles/<int:renteid>/unit/<int:unit>/edit/', views.rent_vehicles_edit, name='rent_vehicles_edit'),


    path('driver/details/<int:pk>/', views.driverdetails, name='driverdetails'),


    #path('features/', views.feature_view, name='features'),
    #path('developers/', views.Developers, name='developers'),
    #path('contact/', views.ContactUS, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
