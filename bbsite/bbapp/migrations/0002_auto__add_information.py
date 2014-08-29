# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Information'
        db.create_table(u'bbapp_information', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(default='uploaded_files/informations/default-img-information.jpg', max_length=100)),
        ))
        db.send_create_signal(u'bbapp', ['Information'])


    def backwards(self, orm):
        # Deleting model 'Information'
        db.delete_table(u'bbapp_information')


    models = {
        u'bbapp.information': {
            'Meta': {'object_name': 'Information'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'default': "'uploaded_files/informations/default-img-information.jpg'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bbapp.news': {
            'Meta': {'object_name': 'News'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'default': "'uploaded_files/news/default-img-news.jpg'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bbapp']