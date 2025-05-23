# Sub-Grid Pixel Sorcery

This project demonstrates an interactive p5.js sketch that generates
a grid of colorful squares and applies several visual effects:

1. **Pixel Sorting** - Sorts pixel rows by brightness for a distorted look.
2. **Noise Displacement** - Warps pixels using Perlin noise.
3. **Optional Bayer Dithering** - Applies a 4×4 dithering matrix for a retro effect.

The sketch runs entirely in the browser and lets you save the result as a
PNG image by clicking the **save** button.

## Running Locally

Simply open `index.html` in a web browser. No additional dependencies are required because it loads the p5.js library from a CDN.

```bash
# If you have Python installed, you can serve it locally
python3 -m http.server
```
Then navigate to `http://localhost:8000` in your browser.

## Parameters

Some constants at the top of the script let you tweak the effect:

- `GRID_SIZE` - base subdivision for the grid
- `SORT_CHANCE` - probability that each row will be pixel-sorted
- `NOISE_MAG` - strength of the noise displacement
- `DITHER_PROB` - chance to apply Bayer dithering at the end

Experiment with different values to see how they change the image.

## License

This project is provided as-is under the MIT license.

