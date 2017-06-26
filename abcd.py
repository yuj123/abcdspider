# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy import signals, Spider
from twisted.internet import reactor, defer, task, threads
import time
import os
import logging
import datetime
import sys
import traceback

class MyItem(scrapy.Item):
    item_type = scrapy.Field()

class BaseSpider(scrapy.Spider):

	def spider_opened(self, spider):
		self.setup()
		
	def spider_closed(self, spider):
		self.tearDown()
		
	def logInfo(self, msg, *args, **kwargs):
		msg = ">>> " + msg
		self.logger.info(msg, *args, **kwargs)
		
	def setup(self):
		self.logInfo("setup")
		pass
		
	def tearDown(self):
		self.logInfo("tearDown")
		pass
		
	def blockingCallFromThread(self, func):
		out = defer.Deferred()
		
		def inThread(out):
			result = None
			try:
				result = threads.blockingCallFromThread(
					reactor, func)
			except: 
				traceback.print_exc()
				reactor.callFromThread(out.errback, BaseException("Exception in Thread"))
			reactor.callFromThread(out.callback, result)
			
		reactor.callInThread(inThread, out)
			
		return out	

	def enqueueRequest(self, req):
		self.crawler.engine.schedule(req, self)
		
	def has_pending_requests(self):
		return self.crawler.engine.slot.scheduler.has_pending_requests()

class SpinSpider(BaseSpider):

	name = 'spinning'
	
	def __init__(self):
		self.dummyPage  = getattr(self, 'dummyPage1', 'file:///' + os.path.abspath("dummy1"))
		self.dummyPage2 = getattr(self, 'dummyPage2', 'file:///' + os.path.abspath("dummy2"))
		
	@classmethod
	def from_crawler(cls, crawler, *args, **kwargs):
		spider = super(SpinSpider, cls).from_crawler(crawler, *args, **kwargs)
		crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
		crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
		return spider
	
	def start_requests(self):
		return [Request(self.dummyPage, self.parse_A, dont_filter=True)]
		
	def parse_A(self, response):
		try:
			d1 = defer.ensureDeferred(self.taskA())
		except:
			self.logError("Unexpected error:%s", sys.exc_info()[0]);
		return d1

	async def taskA(self):
		self.logInfo("TaskA - start")
		item = await self.blockingCallFromThread(self.doTaskA)
		self.enqueueRequest(Request(self.dummyPage, self.parse_B, dont_filter=True))
		self.logInfo("TaskA - end")
		return item
		
	def doTaskA(self):
		time.sleep(2)
		return None
		
	def parse_B(self, response):
		try:
			d1 = defer.ensureDeferred(self.taskB())
		except:
			self.logError("Unexpected error:%s", sys.exc_info()[0]);
		return d1
		
	async def taskB(self):
		self.logInfo("TaskB - start")
		item = await self.blockingCallFromThread(self.doTaskB)
		self.enqueueRequest(Request(self.dummyPage, self.parse_C, dont_filter=True))
		self.logInfo("TaskB - end")
		return item
		
	def doTaskB(self):
		time.sleep(2)
		return [MyItem(item_type="TaskB"), MyItem(item_type="TaskB")]
		
	def parse_C(self, response):
		self.enqueueRequest(Request(self.dummyPage, self.parse_C_, dont_filter=True))
		self.enqueueRequest(Request(self.dummyPage, self.parse_C_, dont_filter=True))
		self.enqueueRequest(Request(self.dummyPage, self.parse_C_, dont_filter=True))
		return None
		
	def parse_C_(self, response):
		try:
			d1 = defer.ensureDeferred(self.taskC())
		except:
			self.logError("Unexpected error:%s", sys.exc_info()[0]);
		return d1
		
	async def taskC(self):
		self.logInfo("TaskC - start")
		item = await self.blockingCallFromThread(self.doTaskC_)
		
		if self.has_pending_requests() == False:
			self.enqueueRequest(Request(self.dummyPage2, self.parse_D))
		
		self.logInfo("TaskC - end")
		return item
		
	def doTaskC_(self):
		time.sleep(2)
		return [MyItem(item_type="TaskC"), MyItem(item_type="TaskC")]
		
	def parse_D(self, response):
		try:
			d1 = defer.ensureDeferred(self.taskD())
		except:
			self.logError("Unexpected error:%s", sys.exc_info()[0]);
		return d1
		
	async def taskD(self):
		self.logInfo("TaskD - start")
		item = await self.blockingCallFromThread(self.doTaskD)
		self.logInfo("TaskD - end")
		return item
		
	def doTaskD(self):
		time.sleep(2)
		return None

