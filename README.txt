About:
------------------
Small demon for testing jade and tenjin templates.

Dependencies:
------------------
 - python-gevent
 - python-flask
 - python-flaskext.wtf
 - python-werkzeug
 - python-six

Running:
------------------
./server

Runs on port 8001, available routes:
 /
 /tenjin/<tpl_name>
 /jade/<tpl_name>

View Paths:
------------------
Tenjin renders from views/tenjin/<tpl_name>.pyhtml
Jade renders from views/jade/<tpl_name>.jade


--

 devel@lorea.org
