import falcon
import pymongo
import bson.json_util

class CrawlersMetaListener:
	def on_get(self, req, res):
		conn = pymongo.MongoClient("mongodb://mongo/monitor")
		db   = conn["monitor"]

		docs = db.crawlers_meta.find({})
		docs = [doc for doc in docs]
		res.status = falcon.HTTP_200
		res.body   = bson.json_util.dumps(docs)