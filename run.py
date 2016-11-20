from lib.listener.crawlers_meta import CrawlersMetaListener
import falcon

class Main:
	def create(self):
		self.api = falcon.API()
		self.api.add_route("/crawlers_meta", CrawlersMetaListener())
		return self.api

api = Main().create()