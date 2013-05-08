# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sprint'
        db.create_table(u'gotem_sprint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'gotem', ['Sprint'])

        # Deleting field 'Objective.title'
        db.delete_column(u'gotem_objective', 'title')

        # Adding field 'Objective.name'
        db.add_column(u'gotem_objective', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Objective.date'
        db.add_column(u'gotem_objective', 'date',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2013, 4, 25, 0, 0), blank=True),
                      keep_default=False)


        # Renaming column for 'Objective.sprint' to match new field type.
        db.rename_column(u'gotem_objective', 'sprint', 'sprint_id')
        # Changing field 'Objective.sprint'
        db.alter_column(u'gotem_objective', 'sprint_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gotem.Sprint']))
        # Adding index on 'Objective', fields ['sprint']
        db.create_index(u'gotem_objective', ['sprint_id'])


        # Changing field 'Objective.description'
        db.alter_column(u'gotem_objective', 'description', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # User chose to not deal with backwards NULL issues for 'Objective.title'
        raise RuntimeError("Cannot reverse this migration. 'Objective.title' and its values cannot be restored.")

    models = {
        u'gotem.objective': {
            'Meta': {'object_name': 'Objective'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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