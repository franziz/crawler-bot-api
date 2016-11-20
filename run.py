from lib.listener.crawlers_meta import CrawlersMetaListener
from falcon_cors                import CORS
import falcon

class Main:
	def create(self):
		self.cors = CORS(allow_all_origins=True)
		self.api  = falcon.API(middleware=[self.cors.middleware])
		self.api.add_route("/crawlers_meta", CrawlersMetaListener())
		return self.api

api = Main().create()
