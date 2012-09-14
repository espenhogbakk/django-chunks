# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Chunk', fields ['key']
        db.delete_unique('chunks_chunk', ['key'])


    def backwards(self, orm):
        
        # Adding unique constraint on 'Chunk', fields ['key']
        db.create_unique('chunks_chunk', ['key'])


    models = {
        'chunks.chunk': {
            'Meta': {'object_name': 'Chunk'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '5'})
        }
    }

    complete_apps = ['chunks']
