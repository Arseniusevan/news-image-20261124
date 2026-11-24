// news-image-20261124 entry program.
// Copies the pre-drawn front-page image (entry.png, 1024x1024, drawn by
// generate_image.py from the world news of Tuesday 24 November 2026)
// into the output directory. Deterministic: the same bytes every run.
// Standard library only; no network.
import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const MAX_BYTES = 1048576; // 1 MiB

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const src = join(here, "entry.png");
const dst = join(outDir, "entry.png");

const size = statSync(src).size;
if (size > MAX_BYTES) {
  throw new Error(`entry.png is ${size} bytes, over the 1 MiB limit`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(src, dst);
console.log(`wrote ${dst} (${size} bytes)`);
