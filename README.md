# Hack A Thing - Setlist Visualizer

## Alexander Danilowicz, Weiling Huang

## What we attempted to build

We both had zero experience with Python web frameworks. Over the summer, I (Alex) wrote a simple, crummy Python script that creates a graph of the frequency of songs played at concerts. We thought it'd be fun to try and hook that script up to the Internet, so anyone can use it. (Please see citations below for script.)

Again, we knew nothing about Django/Flask. In fact, we knew so little about Django we thought it was a front-end only framework at first and Flask was back-end only... 


## Who did what

1. Alex - did the initial Django tutorial and set everything up, put website on pythonanywhere.com, prepared initial script for web, wrote this README worth apparently worth 30% of this assignment grade

1. Weiling - added a form for Django, discovered how to run script, cleaned up form, cleaned up code. Overall baller.

1. We both (paired-programming) worked on getting everything working. We had no idea if you could even run pandas/matplotlib on a web framework. So, that was cool to figure out.

## What we  learned

Django is really powerful. Flask is mini. Flask and Django are different. You either have Flask or Django, not both.

Learned a lot about Django and where things go. Don't put dynamic images in the `static` folder, for example.

## What didn’t work

Hosting it on pythonanywhere didn't really work. First, I had to pay $5 in order for it to scrape setlistfm. Second, we realized with a lot of users these graphs need to stored somewhere. If we continued working on it, we'd add a chron job or dynamically render the graphs and not actually save them as images.

# Other:

## Issues/Problems:

There are many. But we learned a lot about Django and Python web frameworks.

- We don't do error handling yet because we maxed out on our 10+ hours. So, if you choose your own artist and you get an error, try a different artist or ensure that the fields are correct.

## Running it locally

```python3 manage.py runserver```

Then go to: `http://127.0.0.1:8000/`

## Deployed:

[setlistvisualizer.pythonanywhere.com](http://setlistvisualizer.pythonanywhere.com)

## Example:

### Example Data Fields:

Arist Unique: 

`radiohead-bd6bd12.html`

Start URL:

`wells-fargo-center-philadelphia-pa-13eb054d.html`

End URL: 

`td-garden-boston-ma-73eb2ad9.html`


## How do I choose my own concert?

### Arist Unique

This is the unique URL that setlist.fm uses for that artist. For example, if you were to Google search: "Dave Matthews Band setlist fm", you'd probably land here.

```
https://www.setlist.fm/setlists/dave-matthews-band-43d6e713.html
```
**This is what you want:**

```
dave-matthews-band-43d6e713.html
```

That's your Artist Unique.

### Start URL:

What setlist do you want to start at? Say I have a particular timeframe in mind. Then, I would go to the first setlistfm URL I want. Let's start with Dave Matthew's concert at the Gorge:

```
dave-matthews-band/2018/the-gorge-amphitheatre-george-wa-7be87614.html
```

Just take the last half of it. Exclude https.

### Stop URL:

What setlist do you want to end at? If you don't care, then just type:

```
''''
```

Or provide a URL where the tour ended, or any concert you want to stop at.

For example:

```
dave-matthews-band/2018/les-schwab-amphitheater-bend-or-7be82af4.html
```