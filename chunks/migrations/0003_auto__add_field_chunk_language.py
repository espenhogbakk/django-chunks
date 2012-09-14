# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Chunk.language'
        db.add_column('chunks_chunk', 'language', self.gf('django.db.models.fields.CharField')(default='en', max_length=5), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Chunk.language'
        db.delete_column('chunks_chunk', 'language')


    models = {
        'chunks.chunk': {
            'Meta': {'object_name': 'Chunk'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '5'})
        }
    }

    complete_apps = ['chunks']
