# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Objective.date'
        db.alter_column(u'gotem_objective', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'Objective.date'
        db.alter_column(u'gotem_objective', 'date', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        u'gotem.objective': {
            'Meta': {'object_name': 'Objective'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sprint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gotem.Sprint']"})
        },
        u'gotem.sprint': {
            'Meta': {'object_name': 'Sprint'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['gotem']