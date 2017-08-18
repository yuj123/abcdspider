The flow of the spider:
1. "start_requests" request Task A
2. At the end of Task A, request Task B
3. At the end of Task B, request Task C
4. Task C, request Task C1, C2, C3
5. At the end of Task C1, C2, C3, request Task D

Playing around, Deferred, Async/Await and Twisted Thread. Have Fun.

```
scrapy runspider abcd.py

2017-06-26 11:37:49 [scrapy.utils.log] INFO: Scrapy 1.4.0 started (bot: spinbot)
...
2017-06-26 11:37:49 [scrapy.core.engine] INFO: Spider opened
...
2017-06-26 11:37:49 [spinning] INFO: >>> TaskA - start
2017-06-26 11:37:51 [spinning] INFO: >>> TaskA - end
2017-06-26 11:37:52 [spinning] INFO: >>> TaskB - start
2017-06-26 11:37:54 [spinning] INFO: >>> TaskB - end
2017-06-26 11:37:54 [spinning] INFO: >>> TaskC - start
2017-06-26 11:37:54 [spinning] INFO: >>> TaskC - start
2017-06-26 11:37:54 [spinning] INFO: >>> TaskC - start
2017-06-26 11:38:00 [spinning] INFO: >>> TaskC - end
2017-06-26 11:38:00 [spinning] INFO: >>> TaskC - end
2017-06-26 11:38:00 [spinning] INFO: >>> TaskC - end
2017-06-26 11:38:00 [spinning] INFO: >>> TaskD - start
2017-06-26 11:38:02 [spinning] INFO: >>> TaskD - end
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
```
