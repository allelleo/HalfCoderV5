import codestyle_test
import login_test
import registrations_test
import pydocs_test
import redis_test
import smtp_test
codestyle_test.test_conformance()
pydocs_test.test_conformance()
registrations_test.test_first()
registrations_test.test_second()
registrations_test.test_thrid()
login_test.test_first()
login_test.test_second()
login_test.test_thrid()

redis_test.test()
smtp_test.test()