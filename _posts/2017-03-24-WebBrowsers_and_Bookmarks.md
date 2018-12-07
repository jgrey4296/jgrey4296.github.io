---
layout: post
title : "Webrowsers and Bookmarks"
date: 2017-03-24
tags: bookmarks ui criticism
---
I have over 5000 bookmarks. I amass them as I wander the web.  
For a long time it felt like an unrelenting mass of unorganised
information that held great promise.  I eventually got to the point
where I wanted my bookmarks in an easier to manage state.  I collected
the various "backup.html", "backup_1.html", and
"bookmarks_thursday_24th.html", with the intention of simplifying and
sorting. So I wrote a couple of little tools that have helped
dramatically.

## The Trie
A python script to slice up all urls into their component pieces
("www.google.co.uk" => ["www", "google", "co","uk"]) and build a trie
out of them.
Its not fancy, but it very easily removes duplicates.   
  
Why do browsers not provide the ability to flatten bookmarks, and
remove duplicates?


## The Twitterer
A Large number of bookmarks I had tweeted, as shortened urls. So,
armed with my downloaded twitter archive, I set a program going to
search for the title of the article, and load the shortened url, to be
able to rebookmark them outside of twitter. This created a wonderfully
meditational practice, repetitively bookmarking and switching back to
trigger the next load.
