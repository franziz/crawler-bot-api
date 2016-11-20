import falcon
import pymongo
import bson.json_util
import re

class StatusListener:
	def on_get(self, req, res, crawler_name):
		conn = pymongo.MongoClient("mongodb://220.100.163.132/monitor")
		db   = conn["monitor"]

		docs = db.status.find({"crawler_name": re.compile(crawler_name, re.IGNORECASE)})
		docs = [doc for doc in docs]
		res.status = falcon.HTTP_200
		res.body   = bson.json_util.dumps(docs)