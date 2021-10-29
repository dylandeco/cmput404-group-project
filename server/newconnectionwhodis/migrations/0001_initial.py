# Generated by Django 3.2 on 2021-10-29 00:23

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
                ('type', models.TextField(default='author', editable=False)),
                ('host', models.TextField()),
                ('url', models.TextField()),
                ('displayName', models.TextField()),
                ('github', models.TextField()),
                ('profileImage', models.URLField(default='https://i.imgur.com/7MUSXf9.png')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.TextField(default='comment', editable=False)),
                ('published', models.DateTimeField(default='2021-10-29T00:23:08.591612+00:00', editable=False)),
                ('contentType', models.TextField(default='text/markdown', editable=False)),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.author')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.TextField(default='post', editable=False)),
                ('source', models.URLField(editable=False)),
                ('origin', models.URLField(editable=False)),
                ('contentType', models.TextField(default='text/plain', editable=False)),
                ('published', models.DateTimeField(default='2021-10-29T00:23:08.591250+00:00', editable=False)),
                ('visibility', models.TextField(default='PUBLIC')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.author')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.TextField(default='Like', editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.author')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.post')),
            ],
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(default='inbox', editable=False)),
                ('items', models.TextField(default='[]')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.author')),
            ],
        ),
        migrations.CreateModel(
            name='FollowReq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestee', to='newconnectionwhodis.author')),
                ('requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestor', to='newconnectionwhodis.author')),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='newconnectionwhodis.author')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='newconnectionwhodis.author')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newconnectionwhodis.post'),
        ),
    ]
