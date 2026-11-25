# README visual assets

The two scientific figures are raster exports of the maintainer-supplied technical
report sources in `FrontierDrugBench (2).zip`. Their data, labels and composition
are unchanged; no plot was redrawn. The source archive and LaTeX build artifacts
are not distributed here.

| Asset | Original source | Export |
| --- | --- | --- |
| `graphical-abstract.png` | `figure/graphical-abstract.pdf` | 2400 × 1350 pixels, RGB PNG |
| `benchmark-inventory.png` | `figure/benchmark-inventory.pdf` | 2200 × 933 pixels, RGB PNG |

The graphical abstract covers BindingGym and the report's five-domain evaluation;
its dashed lines are illustrative forecasts. The inventory figure describes the
full 1,196-task inventory, including 225 internal and 971 external tasks. Its
360-task modality panel is a subset, not an additional task inventory. These
figures do not present scores computed on the 971-task public release.

## Reproduce the figure exports

Extract the two source PDFs from the original archive, then run from the
repository root with Poppler installed:

```sh
pdftoppm -f 1 -l 1 -scale-to 2400 -png -singlefile figure/graphical-abstract.pdf docs/assets/graphical-abstract
pdftoppm -f 1 -l 1 -scale-to 2200 -png -singlefile figure/benchmark-inventory.pdf docs/assets/benchmark-inventory
```

The committed PNGs were converted to RGB and losslessly optimized with Pillow:

```python
from pathlib import Path
from PIL import Image

for name in ("graphical-abstract", "benchmark-inventory"):
    path = Path("docs/assets") / f"{name}.png"
    with Image.open(path) as source:
        image = source.convert("RGB")
    image.save(path, optimize=True)
```

## Source PDF SHA-256

- `figure/graphical-abstract.pdf`: `37d160197582eaf2d9acab81bb979f36f3e774cd99b85aaf3c5a51a105e0329b`
- `figure/benchmark-inventory.pdf`: `11bdfb7210a76cae87abba3e63dd62eb92339065a622e3eaeb87ffd529f50dea`

## Branding and resource links

`wordmark.svg` is an editable text wordmark using the report's blue-to-purple
palette. `homepage.svg`, `technical-report.svg`, `dataset.svg` and `citation.svg`
are local navigation labels. They contain no scripts, remote resources or embedded
fonts. Links live in the README so the images remain display-only. The SVG files
are their editable sources.
