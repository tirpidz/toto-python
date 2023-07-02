# Documentation

Documentation is simple, see those `.md` text file in the repo? Those are our documentation!

To build this documentation, we use :

* [mkdocs.org](https://www.mkdocs.org) to produces this documentation from plain markdown `md` files

Everything is stored in `docs` folder.

## Generate and Serve

```bash
mkdocs serve
```

## Build the static site

```bash
mkdocs build
```

## Documentation tricks

### Tables

| Field | Type     | Required | Description |
| ---   | ---      | ---      | ---         |
| `f`   | `string` |          | Something   |

Is generated from using:

```md
| Field | Type     | Required | Description |
| ---   | ---      | ---      | ---         |
| `f`   | `string` |          | Something   |
```

### Panel

> This **quote** panel is created with `>`

```md
> This **quote** panel is created with `>`
```

!!! info

     This **info** panel is created with `!!! info`

```md
!!! info

    This **info** panel is created with `!!! info`
```

!!! tip

    This **tip** panel is created with `!!! tip`

```md

!!! tip

    This **tip** panel is created with `!!! tip`
```

!!! warning

    This **warning** panel is created with `!!! warning`

```md

!!! warning

    This **warning** panel is created with `!!! warning`
```

Other [types](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types) are available.

### Diagrams

To do nice diagram, use [this](https://app.diagrams.net/) then use default soft colors, and then `sketch` line mode.
Once done export then as `SVG` and add then to the `docs` folder. Make sure when we click on it from the documentation
the zoom in works, and the diagram is perfectly readable.

### Link to a header

Somewhere in `page.md` there is a header like:

```md
### My Header Title
```

To link to it (from any page even `page.md` itself):

```md
[link display](docs/page?id=my-header-title)
```
