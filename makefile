
serve:
	jekyll serve

post:
	python _python_utils/make_post.py

tags:
	mkdir tags
	python _python_utils/tag_gen.py

clean:
	rm -rf tags


