# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Join.friend'
        db.add_column('joins_join', 'friend',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='referral', null=True, to=orm['joins.Join']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Join.friend'
        db.delete_column('joins_join', 'friend_id')


    models = {
        'joins.join': {
            'Meta': {'object_name': 'Join', 'unique_together': "(('email', 'ref_id'),)"},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'referral'", 'null': 'True', 'to': "orm['joins.Join']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'unique': 'True', 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        }
    }

    complete_apps = ['joins']