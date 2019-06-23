run-example:
	find examples/microservices-demo-master/ -iname *.yaml | xargs ./yaml-complexity-index.py
