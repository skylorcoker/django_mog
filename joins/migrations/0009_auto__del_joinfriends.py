# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'JoinFriends'
        db.delete_table('joins_joinfriends')

        # Removing M2M table for field friends on 'JoinFriends'
        db.delete_table(db.shorten_name('joins_joinfriends_friends'))


    def backwards(self, orm):
        # Adding model 'JoinFriends'
        db.create_table('joins_joinfriends', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emailall', self.gf('django.db.models.fields.related.ForeignKey')(related_name='emailall', to=orm['joins.Join'])),
            ('email', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Sharer', to=orm['joins.Join'], unique=True)),
        ))
        db.send_create_signal('joins', ['JoinFriends'])

        # Adding M2M table for field friends on 'JoinFriends'
        m2m_table_name = db.shorten_name('joins_joinfriends_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('joinfriends', models.ForeignKey(orm['joins.joinfriends'], null=False)),
            ('join', models.ForeignKey(orm['joins.join'], null=False))
        ))
        db.create_unique(m2m_table_name, ['joinfriends_id', 'join_id'])


    models = {
        'joins.join': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'unique': 'True', 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['joins']