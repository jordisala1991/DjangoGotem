# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Objective'
        db.create_table(u'gotem_objective', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sprint', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'gotem', ['Objective'])


    def backwards(self, orm):
        # Deleting model 'Objective'
        db.delete_table(u'gotem_objective')


    models = {
        u'gotem.objective': {
            'Meta': {'object_name': 'Objective'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sprint': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['gotem']