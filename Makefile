VENV = venv
ACTIVATE = $(VENV)/bin/activate
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip



build-AwsWafGstaticIpSet:
	pwd
	python3 -m venv $(VENV)
	source $(ACTIVATE); \
	$(PIP) install -r requirements.txt
	mkdir $(VENV)/lib/python3.9/site-packages/caQuery
	git init $(VENV)/lib/python3.9/site-packages/caQuery
	git -C $(VENV)/lib/python3.9/site-packages/caQuery pull https://github.com/chuckautomates/query.git
	cd $(VENV)/lib/python3.9/site-packages/caQuery && python setup.py bdist_egg
	cp -R $(VENV)/lib/python3.9/site-packages/ awsWafIpSet/


clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	rm -rf awsWafIpSet/*/
	rm -f awsWafIpSet/caQuery*
	rm -f awsWafIpSet/distutils*
	rm -f awsWafIpSet/easy-*
	rm -f awsWafIpSet/six.py
