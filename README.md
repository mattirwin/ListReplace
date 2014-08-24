ListReplace Sublime Text 2 Plugin
=================================
v.0.1.0

This is a port of a script I wrote back when I was coding in BBEdit.  It ended up being the most productive script I ever wrote myself for BBEdit.  Now here it is for Sublime Text.

##What it does

The plugin replaces a search term you choose in one window with lines or search terms from another window. Put in another way, it does a "find" in one window and pulls the "replace" from another.  This can be very useful. 

It requires at least 2 open tabs in a window to run. The number of search terms in each window must match as well

###Steps

The plugin will prompt for the following:

1. Choose the target tab(view): where your search and replacement will be run
2. Choose the source tab(view): where your replacements will be sourced from
3. Enter a search term (regex): your target window will be searched for this term
4. Enter a replacement term (regex): your source window will be searched for this term, matches will be used to replace matches in the target window

Once the above input is retrieved the plugin will check that the number of search and replacement terms match.  If they don't the plugin stops execution and will display a message informing you of the mismatch.  If they do, execution continues and each target search is replaced with each source replacement.

###Example

How this works or why it might be useful, might be a little hard to follow at this point, here is an example:

You have some html

Tab 1:

```
	<div>Content 1</div>
	<div><span>FOO 123</span></div>
	<div>Content 2</div>
	<div>Content 3</div>
	<div>FOO 234</div>
	<div>
		<ul>
			<li>stuff</li>
			<li>more stuff</li>
			<li>other stuff</li>
		</ul>
		<div>FOO 345</div>
	</div>
	<div>Content 4</div>
	<div>FOO 456</div>
```

You want to replace all the "FOO ..." content with new content, however a simple find and replace won't solve your problem because your replacements are all unique and you've listed them out in Tab 2.

Tab 2:

```
	BAR <strong>AAA111<strong>
	BAR <em>BBB222</em>
	BAR <em>CCC333</em>
	BAR <strong>DDD444</strong>
```

You could just copy and paste these in "by hand", but you're a high powered tech professional, with things to do and places to be. What would be great, would be if you do a find and replace where you could source all your replacements from Tab 2 instead, and with the ListReplace plugin you can.

Run the plugin, and start by choosing your target tab:

```
Choose the target view:
*Tab 1
Tab 2
```

next choose your source tab, in this case the only remaining choice:

```
Choose the source view:
*Tab 2
```

next enter your search term, in this case you can use the regular expression "FOO \d\d\d" to match all the "FOO ..." content you want replaced

```
Enter a search term (regex):
FOO \d\d\d
```

last enter your replacement term, since every line in Tab 2 represents a replacement you wish to capture you use the regular expression ".+$" to capture each line

```
Enter a replacement term (regex):
.+$
```

The plugin runs and Tab 1 now looks like this:

```
	<div>Content 1</div>
	<div><span>BAR <strong>AAA111<strong></span></div>
	<div>Content 2</div>
	<div>Content 3</div>
	<div>BAR <em>BBB222</em></div>
	<div>
		<ul>
			<li>stuff</li>
			<li>more stuff</li>
			<li>other stuff</li>
		</ul>
		<div>BAR <em>CCC333</em></div>
	</div>
	<div>Content 4</div>
	<div>BAR <strong>DDD444</strong></div>
```

What could have taken minutes took seconds! Yay! You take off work early and go drinking with movie stars. Win.

License
=======

ListReplace is released under the MIT license.

Copyright (c) 2014 Matt Irwin info@irwinone.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
