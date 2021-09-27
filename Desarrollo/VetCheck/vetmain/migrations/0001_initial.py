# Generated by Django 3.2.6 on 2021-09-26 23:59

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombre')),
                ('peso', models.FloatField()),
                ('edad', models.DateField()),
                ('sexo', models.IntegerField(choices=[(1, 'Macho'), (2, 'Hembra')])),
                ('descripcion', models.TextField(max_length=60, verbose_name='Descripcion de la mascota')),
                ('imagen', django_resized.forms.ResizedImageField(crop=None, default='default-image.png', force_format='JPEG', keep_meta=True, quality=75, size=[500, 300], upload_to='mascotas')),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.perfilcliente')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField(blank=True, max_length=150, null=True, verbose_name='Motivo de consulta')),
                ('subespecialidad', models.IntegerField(choices=[(1, 'Cita General'), (2, 'Cirugia'), (3, 'Examenes')], default=1)),
                ('examen_fisico', models.TextField(blank=True, max_length=350, null=True)),
                ('vacunas', models.CharField(blank=True, max_length=40, null=True)),
                ('antiparacito', models.CharField(blank=True, max_length=40, null=True)),
                ('examenes', models.FileField(blank=True, null=True, upload_to='archivos')),
                ('diagnostico', models.TextField(blank=True, max_length=350, null=True)),
                ('receta', models.TextField(blank=True, max_length=350, null=True)),
                ('fecha', models.DateTimeField()),
                ('confirmacion', models.BooleanField(default=False)),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vetmain.mascota')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.perfilcliente')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.perfilveterinario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
