<div align="center">
  <img src="https://github.com/xj63/TickTime/raw/main/public/ticktime.jpg" width="40%">
</div>

<h1 align="center">TickTime</h1>

<div align="center">

[![Web](https://img.shields.io/badge/Website-ticktime.xj63.fun-blue?style=flat-square&color=purple)](https://ticktime.xj63.fun)
[![License](https://img.shields.io/github/license/xj63/TickTime?style=flat-square&label=License)](./LICENSE)
![Language](https://img.shields.io/badge/Language-vue-lightgreen?style=flat-square)
![Repo Stars](https://img.shields.io/github/stars/xj63/TickTime?style=flat-square&label=%E2%9C%A8%20Stars)
[![Last Commit](https://img.shields.io/github/last-commit/xj63/TickTime?style=flat-square&label=%F0%9F%94%A5%20Last%20commit&color=orange)](https://github.com/xj63/TickTime/activity)

</div>

A application that _elegantly_ displays the current **time** and an inspirational **quote**, designed to fit perfectly within any screen size.

## Preview

Just feel it.
[website.complex](https://ticktime.xj63.fun/?quote=Click+here+to+edit+quote.&records=2024-12-18T13.41.50Z_Click+here+to+edit+notes.|2024-12-18T13.43.26Z_All+the+data+is+stored+in+the+URL+link.|2024-12-18T13.44.49Z_You+can+share+this+link+to+your+friends+to+get+the+same+page.|2024-12-18T13.46.02Z|2024-12-18T13.46.03Z_Click+right+time+to+add+snap.)
[website.simple](https://ticktime.xj63.fun)

<table>
  <tr>
    <td><img src="https://github.com/xj63/TickTime/raw/main/docs.assets/complex.png" style="max-width: 100%; height: auto;" alt="complex"></td>
    <td><img src="https://github.com/xj63/TickTime/raw/main/docs.assets/complex-mobile.png" style="max-width: 100%; height: auto;" alt="complex mobile"></td>
  </tr>
</table>
<table>
  <tr>
    <td><img src="https://github.com/xj63/TickTime/raw/main/docs.assets/simple.png" style="max-width: 100%; height: auto;" alt="simple"></td>
    <td><img src="https://github.com/xj63/TickTime/raw/main/docs.assets/simple-mobile.png" style="max-width: 100%; height: auto;" alt="simple mobile"></td>
  </tr>
</table>

## Features

- Displays current time and an inspirational quote.
- Fully responsive design for any screen size.
- Easy to customize the quote and share it with others.
- URL is all. Records the time and quote in the URL link.

## API Description

### URL Parameters

- `quote`: The quote to display. This parameter allows users to customize the quote shown on the bottom.
- `records`: Encoded data containing notes and timestamps. This data is stored in the URL and can be shared with others to reproduce the same page.

format: `YYYY-MM-DDThh.mm.ssZ{_note}` Z is UTC time zone. use `|` to split snapshots.

### Example URL

```url
https://ticktime.xj63.fun/?quote=Click+here+to+edit+quote.&records=2024-12-18T15.51.22Z|2024-12-18T15.51.24Z_hello
```

```
quote=Click+here+to+edit+quote. # bottom show quote: 'Click here to edit quote.'
records=2024-12-18T15.51.22Z|2024-12-18T15.51.24Z_hello # timesnap data
```

| time                 | note  |
| -------------------- | ----- |
| 2024-12-18T15.51.22Z |       |
| 2024-12-18T15.51.24Z | hello |

## Deploy

You can fork this project and deploy it on [GitHub Pages](https://pages.github.com/).

**Notice**: ensure that the base url is right.
```js
// file ./vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  base: '/your-base-url/', // set your base url in here, example is your project name.
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
```

`./.github/workflows/deploy.yml` is the workflow to run `bun run build` to branch gh-pages.

Set github project config gh-pages to github pages.

# Contributing Quotes

We welcome contributions to our quotes collection! Please add your favorite quotes to the public/quotes.txt file. PR/Issue are most welcome.
