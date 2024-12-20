<div align="center">
  <img src="https://github.com/xj63/TickTime/raw/main/docs.assets/ticktime.jpg" width="40%">
</div>

<h1 align="center">TickTime</h1>

<div align="center">

[![Web](https://img.shields.io/badge/Website-ticktime.xj63.fun-blue?style=flat-square&color=purple)](https://ticktime.xj63.fun)
[![License](https://img.shields.io/github/license/xj63/TickTime?style=flat-square&label=License)](./LICENSE)
![Language](https://img.shields.io/badge/Language-vue-lightgreen?style=flat-square)
![Repo Stars](https://img.shields.io/github/stars/xj63/TickTime?style=flat-square&label=%E2%9C%A8%20Stars)
[![Last Commit](https://img.shields.io/github/last-commit/xj63/TickTime?style=flat-square&label=%F0%9F%94%A5%20Last%20commit&color=orange)](https://github.com/xj63/TickTime/activity)

</div>

一个优雅显示当前**时间**和励志**名言**的应用，设计适配任何屏幕尺寸。

## 预览

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

## 功能

- 显示当前时间和励志名言。
- 从 public/quotes.txt 随机生成名言。
- 完全响应式设计，适配任何屏幕尺寸。
- 轻松自定义名言并与他人分享。
- 一切数据存储在 URL 中。通过 URL 记录时间和名言。

## API 描述

### URL 参数

- `quote:` 要显示的名言。此参数允许用户自定义底部显示的名言。

- `records:` 记录时间戳数据和相应笔记。存储在 URL 中，可以分享给他人重现相同页面。

格式：`YYYY-MM-DDThh.mm.ssZ{\_note}` Z 表示 UTC 时区，用 | 分隔快照。

### 示例 URL

```url
https://ticktime.xj63.fun/?quote=Click+here+to+edit+quote.&records=2024-12-18T15.51.22Z|2024-12-18T15.51.24Z_hello
```

```
quote=Click+here+to+edit+quote. # 底部显示名言：'Click here to edit quote.'
records=2024-12-18T15.51.22Z|2024-12-18T15.51.24Z_hello # 时间快照数据
```

| 时间                 | 笔记  |
| -------------------- | ----- |
| 2024-12-18T15.51.22Z |       |
| 2024-12-18T15.51.24Z | hello |

## 部署

你可以 fork 这个项目，并在 GitHub Pages 上部署。

**注意：**请确保正确设置URL。

```js
// file ./vite.config.js
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueDevTools from "vite-plugin-vue-devtools";

// https://vite.dev/config/
export default defineConfig({
  base: "/your-base-url/", // set your base url in here, example is your project name.
  plugins: [vue(), vueDevTools()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
```

`./.github/workflows/deploy.yml` 是运行 `bun run build` 构建到 gh-pages 分支的工作流。

将 GitHub 项目的 gh-pages 分支配置为 GitHub Pages。

## 贡献名言

欢迎为我们的名言集合贡献力量！请将你喜欢的名言添加到 public/quotes.txt 文件中。非常欢迎 PR/Issue
