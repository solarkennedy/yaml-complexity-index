run-example:
	find examples/microservices-demo-master/ -iname *.yaml | xargs ./yaml_complexity_index.py
