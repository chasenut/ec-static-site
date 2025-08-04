# ec-static-site

Static site generator tool. It generates site recursively based on 
documents in `./content` directory and resources in `./static` directory.

## Under the hood

Program scans `./content` directory and converts all `markdown` files to 
their `html` representatives, which are later inserted into `template.html` and 
transfered to `./public` alongside resources from `./static` directory.

## Features

Supported **block** syntax conversion:

### Plain text
`index.md`:
```
This is some nice text
```
to `index.html`:
```
<p>This is some nice text</p>
```

### Heading
`index.md`:
```
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
``` 
to `index.html`:
```
<h1>Header 1</h1>
<h2>Header 2</h2>
<h3>Header 3</h3>
<h4>Header 4</h4>
<h5>Header 5</h5>
<h6>Header 6</h6>
```

### Code
`index.md`:
```` 
```
def be_amazing():
    repo.star()
```
````
to `index.html`:
```
<pre><code>def be_amazing():
    repo.star()
</code></pre>
```

### Quote
`index.md`:
```
> "An idiot admires complexity, a genius admires simplicity."
> 
> -- Terry A. Davis
``` 
to `index.html`:
```
<blockquote>"An idiot admires complexity, a genius admires simplicity"  -- Terry A. Davis</blockquote>
```

### Unordered list
`index.md`:
```
- vim
- arch
- split keyboard
```
to `index.html`:
```
<ul><li>vim</li><li>arch</li><li>split keyboard</li></ul>
```

### Ordered list
`index.md`:
```
1. vim
2. arch
3. split keyboard
```
to `index.html`:
```
<ol><li>vim</li><li>arch</li><li>split keyboard</li></ol>
```

Supported **inline** syntax conversion:

### Bold
`index.md`:
```
This is **bold** text
```
to `index.html`:
```
This is <b>bold</b> text
```

### Italic
`index.md`:
```
This is _italic_ text
```
to `index.html`:
``` 
This is <i>italic</i> text
```
 
### Code
`index.md`:
```
This is `code` text
```
to `index.html`:
```
This is <code>code</code> text
```

### Link
`index.md`:
```
This is [link](https://your.link.here) element
```
to `index.html`:
```
This is <a href="https://your.link.here">link</a> element
```

### Image
`index.md`:
```
This is ![image](./path/to/img.png) element
```
to `index.html`:
```
This is <img src="./path/to/img.png"> element
```

## Syntax

Markdown has some rules when writting page, some of which are:

- Document must have at least one `<h1>` header (`# Header lvl 1`) which will 
be used as page title
- All blocks must be separated by one empty line
- No inline formatting will be rendered in the `code` block

# Run

Once you have created your desired pages in markdown, run:

```
./main.sh
```

This will overwrite `./public` directory with new content and host it on 
`http://localhost:8888/`.


## Credit

Project made as a part of [boot.dev](https://www.boot.dev) course.
