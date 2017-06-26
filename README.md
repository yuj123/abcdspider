The flow of the spider:
1. "start_requests" request Task A
2. At the end of Task A, request Task B
3. At the end of Task B, request Task C
4. Task C, request Task C1, C2, C3
5. At the end of Task C1, C2, C3, request Task D

Playing around, Deferred, Async/Await and Twisted Thread. Have Fun.

scrapy runspider abcd.py

2017-06-26 11:37:49 [scrapy.utils.log] INFO: Scrapy 1.4.0 started (bot: spinbot)
2017-06-26 11:37:49 [scrapy.utils.log] INFO: Overridden settings: {'BOT_NAME': 'spinbot', 'NEWSPIDER_MODULE': 'spinbot.spiders', 'SPIDER_LOADER_WARN_ONLY': True, 'SPIDER_MODULES': ['spinbot.spiders']}
2017-06-26 11:37:49 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2017-06-26 11:37:49 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2017-06-26 11:37:49 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2017-06-26 11:37:49 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2017-06-26 11:37:49 [scrapy.core.engine] INFO: Spider opened
2017-06-26 11:37:49 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2017-06-26 11:37:49 [spinning] INFO: >>> setup
2017-06-26 11:37:49 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2017-06-26 11:37:49 [scrapy.core.engine] DEBUG: Crawled (200) <GET file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1> (referer: None)
2017-06-26 11:37:49 [spinning] INFO: >>> TaskA - start
2017-06-26 11:37:51 [spinning] INFO: >>> TaskA - end
2017-06-26 11:37:51 [scrapy.core.engine] DEBUG: Crawled (200) <GET file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1> (referer: None)
2017-06-26 11:37:52 [spinning] INFO: >>> TaskB - start
2017-06-26 11:37:54 [spinning] INFO: >>> TaskB - end
2017-06-26 11:37:54 [scrapy.core.scraper] DEBUG: Scraped from <200 file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1>
{'item_type': 'TaskB'}
2017-06-26 11:37:54 [scrapy.core.scraper] DEBUG: Scraped from <200 file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1>
{'item_type': 'TaskB'}
2017-06-26 11:37:54 [scrapy.core.engine] DEBUG: Crawled (200) <GET file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1> (referer: None)
2017-06-26 11:37:54 [scrapy.core.engine] DEBUG: Crawled (200) <GET file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1> (referer: None)
2017-06-26 11:37:54 [scrapy.core.engine] DEBUG: Crawled (200) <GET file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1> (referer: None)
2017-06-26 11:37:54 [scrapy.core.engine] DEBUG: Crawled (200) <GET file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1> (referer: None)
2017-06-26 11:37:54 [spinning] INFO: >>> TaskC - start
2017-06-26 11:37:54 [spinning] INFO: >>> TaskC - start
2017-06-26 11:37:54 [spinning] INFO: >>> TaskC - start
2017-06-26 11:38:00 [spinning] INFO: >>> TaskC - end
2017-06-26 11:38:00 [spinning] INFO: >>> TaskC - end
2017-06-26 11:38:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy2> (referer: None)
2017-06-26 11:38:00 [scrapy.core.scraper] DEBUG: Scraped from <200 file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1>
{'item_type': 'TaskC'}
2017-06-26 11:38:00 [scrapy.core.scraper] DEBUG: Scraped from <200 file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1>
{'item_type': 'TaskC'}
2017-06-26 11:38:00 [scrapy.core.scraper] DEBUG: Scraped from <200 file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1>
{'item_type': 'TaskC'}
2017-06-26 11:38:00 [scrapy.core.scraper] DEBUG: Scraped from <200 file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1>
{'item_type': 'TaskC'}
2017-06-26 11:38:00 [scrapy.dupefilters] DEBUG: Filtered duplicate request: <GET file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy2> - no more duplicates will be shown (see DUPEFILTER_DEBUG to show all duplicates)
2017-06-26 11:38:00 [spinning] INFO: >>> TaskC - end
2017-06-26 11:38:00 [scrapy.core.scraper] DEBUG: Scraped from <200 file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1>
{'item_type': 'TaskC'}
2017-06-26 11:38:00 [scrapy.core.scraper] DEBUG: Scraped from <200 file:///C:%5Cprojects%5Cspinbot%5Cspinbot%5Cspiders%5Cdummy1>
{'item_type': 'TaskC'}
2017-06-26 11:38:00 [spinning] INFO: >>> TaskD - start
2017-06-26 11:38:02 [spinning] INFO: >>> TaskD - end
2017-06-26 11:38:02 [scrapy.core.engine] INFO: Closing spider (finished)
2017-06-26 11:38:02 [spinning] INFO: >>> tearDown
2017-06-26 11:38:02 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 1750,
 'downloader/request_count': 7,
 'downloader/request_method_count/GET': 7,
 'downloader/response_bytes': 133,
 'downloader/response_count': 7,
 'downloader/response_status_count/200': 7,
 'dupefilter/filtered': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2017, 6, 26, 3, 38, 2, 429398),
 'item_scraped_count': 8,
 'log_count/DEBUG': 17,
 'log_count/INFO': 21,
 'response_received_count': 7,
 'scheduler/dequeued': 7,
 'scheduler/dequeued/memory': 7,
 'scheduler/enqueued': 7,
 'scheduler/enqueued/memory': 7,
 'start_time': datetime.datetime(2017, 6, 26, 3, 37, 49, 799386)}
2017-06-26 11:38:02 [scrapy.core.engine] INFO: Spider closed (finished)
