# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Question.multiple_answers'
        db.add_column(u'home_question', 'multiple_answers',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Question.multiple_answers'
        db.delete_column(u'home_question', 'multiple_answers')


    models = {
        u'home.answer': {
            'Meta': {'object_name': 'Answer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Question']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'home.page': {
            'Meta': {'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Test']"})
        },
        u'home.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple_answers': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Page']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'home.result': {
            'Meta': {'object_name': 'Result'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_points': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Test']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'home.test': {
            'Meta': {'object_name': 'Test'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['home']