# Generated by Django 4.0.4 on 2022-06-11 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(blank=True, default='https://th.bing.com/th/id/R.048fe00ae936f5b1ceef950ff314271d?rik=PPn3NcFhqZ46IA&riu=http%3a%2f%2fwww.vgmpf.com%2fWiki%2fimages%2fc%2fcb%2fNoPhoto.png&ehk=h28ESegf6decjqYgG7NuE1ZQ02oar%2bryghpicALBdeI%3d&risl=&pid=ImgRaw&r=0', max_length=100000, null=True)),
                ('url', models.CharField(blank=True, default='index', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('image', models.CharField(blank=True, default='https://th.bing.com/th/id/R.048fe00ae936f5b1ceef950ff314271d?rik=PPn3NcFhqZ46IA&riu=http%3a%2f%2fwww.vgmpf.com%2fWiki%2fimages%2fc%2fcb%2fNoPhoto.png&ehk=h28ESegf6decjqYgG7NuE1ZQ02oar%2bryghpicALBdeI%3d&risl=&pid=ImgRaw&r=0', max_length=100000, null=True)),
                ('food_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.foodgroup')),
            ],
        ),
    ]
