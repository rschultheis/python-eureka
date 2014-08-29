from eureka.client import EurekaClient
import logging

logging.basicConfig()

print "hello"
ec = EurekaClient(app_name="irrelevant", eureka_url="http://localhost:13350/v2/", use_dns=False, data_center="NotAmazon")
"initialized"

print ec.get_eureka_urls()
print ec.get_app("USER_THRIFT_DEV")
