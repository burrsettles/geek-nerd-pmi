geek-nerd-pmi
=============

Python scripts from my Geek/Nerd Twitter analysis. First read the surprisingly viral blog post [On "Geek" Versus "Nerd"](http://slackprop.wordpress.com/2013/06/03/on-geek-versus-nerd/) at *Slackpropagation*.

You'll need:

  1. A "background corpus" from the [Twitter streaming API](https://dev.twitter.com/docs/api/1.1/get/statuses/sample). These are assumed to be in gzipped files of JSON-encoded objects that are one line per tweet.
  2. A "search corpus" of interest from the [Twitter search API](https://dev.twitter.com/docs/api/1.1/get/search/tweets). In my case these were collected from a cron job that queried "geek," "nerd," "dork," and "dweeb" periodically and wrote the output to log files. These are also JSON tweet objects, one-per-line (but not gzipped).

Compute the PMIs by running Python 2.7 scripts in the order numbered:

    $ python 1_rfmt_queries.py geek.search.1.log geek.search.2.log ... > geek.search.corpus.txt
    $ python 2_log_pxy.py geek.search.corpus.txt > geek.log_pxy.txt
	[... repeat 1 & 2 for other query terms, like "nerd" ...]
	$ python 3_log_px.py background.log.1.gz background.log.2.gz ... > background.log_px.txt
	$ python 4_final_scores.py background.log_px.txt geek.log_pxy.txt ... > pmis.txt

You'll need to edit ```4_final_scores.py``` to accomodate whatever words you are analyzing.

**Note that I offer absolutely zero support for these scripts**, and I'm kind of embarrassed by them, but a lot of people have asked, and I don't care to clean them up, so here's how the sausage was made. I hacked the pipeline together over about an hour for a weekend project, so yes, it's sloppy. And I'd only really been using Python for a few of months at this point. Also, I didn't do any smoothing on the probabilities. The Rev. Bayes would be so disappointed.