from haystack import indexes
from search.models import Club


class ClubIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    abbreviation = indexes.CharField(model_attr='abbreviation')
    # genre = indexes.CharField(model_attr='genre')

    def get_model(self):
        return Club

    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())