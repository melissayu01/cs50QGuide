from haystack import indexes
from search.models import Club

# haystack index for Club model
class ClubIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	abbreviation = indexes.CharField(model_attr='abbreviation')

	def get_model(self):
		return Club