from django.db import models
from django.contrib.auth.models import User #traigo la tabla User que crea django por defecto
from django.db.models.signals import post_save

# PERFIL DE USUARIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario' )
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name='Imagen de perfil')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Direccion') #El max_length me permite definir el tamano de los caracteres
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Localidad')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Telefono')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id'] #Arriba queda el registro mas reciente creado

    def __str__(self):
        return self.user.username
# MOMENTO DE CREAR MI USUARIO CREAR EL PERFIL
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
# FUNCION CUANDO SE GRABE EL PERFIL IMPACTE EN LA BASE DE DATOS DE PERFILES
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User) #LOGRO CONECTAR EL USUARIO CON EL PERFIL
post_save.connect(save_user_profile, sender=User) #LOGRO CONECTAR EL USUARIO CON EL PERFIL