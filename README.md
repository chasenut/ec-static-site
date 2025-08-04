# ec-static-site

Static site generator tool. It generates site recursively based on 
documents in `./content` directory and resources in `./static` directory.

## Under the hood

Program scans `./content` directory and converts all `markdown` files to 
their `html` representatives, which are later inserted into `template.html` and 
transfered to `./public` alongside resources from `./static` directory.

## Features

Supported syntax conversion:

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
