from django.apps import AppConfig


<<<<<<<< HEAD:apps/finanzas/produccion/apps.py
class ProduccionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.finanzas.produccion'
========
class ActividadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.trazabilidad.actividad'
>>>>>>>> Trazabilidad2:apps/trazabilidad/actividad/apps.py
