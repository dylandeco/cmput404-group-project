# Generated by Django 3.2 on 2021-10-07 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(default='author', editable=False, max_length=6)),
                ('host', models.URLField(editable=False, max_length=32)),
                ('url', models.URLField(editable=False, max_length=128)),
                ('displayName', models.CharField(max_length=32)),
                ('github', models.TextField(max_length=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(default='post', editable=False, max_length=4)),
                ('contentType', models.TextField(default='text/plain', editable=False)),
                ('content', models.TextField(default='lorem ipsum dolor sit amet')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.author')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(default='comment', editable=False, max_length=7)),
                ('published', models.DateTimeField(default='2021-10-07T20:34:44.018696+00:00', editable=False)),
                ('contentType', models.TextField(default='text/markdown', editable=False)),
                ('comment', models.CharField(max_length=280)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.post')),
            ],
        ),
    ]
