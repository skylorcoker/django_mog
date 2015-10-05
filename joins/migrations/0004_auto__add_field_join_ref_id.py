# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Join.ref_id'
        db.add_column('joins_join', 'ref_id',
                      self.gf('django.db.models.fields.CharField')(max_length=120, default='ABC'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Join.ref_id'
        db.delete_column('joins_join', 'ref_id')


    models = {
        'joins.join': {
            'Meta': {'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '120', 'default': "'ABC'"}),
            'ref_id': ('django.db.models.fields.CharField', [], {'max_length': '120', 'default': "'ABC'"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['joins']