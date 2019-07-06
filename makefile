
post:
	python _python_utils/make_post.py

tags:
	mkdir tags
	touch tags/index.html
	python _python_utils/tag_gen.py

clean:
	rm -rf tags


