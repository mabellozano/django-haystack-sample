from haystack import indexes
from django_haystack_sample.models import Document

class DocumentIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Document