# 泰国服饰定价计算器 PWA

随时随地用手机算泰铢成本 → 人民币售价 + 利润。

## 文件清单

- `index.html` — 完整版（含 PWA 安装支持）
- `offline_calculator.html` — 单文件离线版（无需 PWA 即可独立使用）
- `manifest.json` — PWA 配置文件
- `sw.js` — Service Worker（离线缓存）
- `icon-192.png` / `icon-512.png` — PWA 图标
- `.nojekyll` — 告诉 GitHub Pages 跳过 Jekyll 处理

## GitHub Pages 部署步骤

1. 上传所有文件到 GitHub 仓库 `pricing-calculator` 根目录
2. 仓库 → **Settings** → **Pages**
3. **Source**: `Deploy from a branch`
4. **Branch**: `main` / `(root)` → **Save**
5. 等待 1-3 分钟，访问 `https://<用户名>.github.io/pricing-calculator/`

## 手机安装为 App

- **iPhone**: Safari 打开 → 分享 → 添加到主屏幕
- **Android**: Chrome 打开 → 菜单 → 添加到主屏幕

## 使用

主入口用 `index.html`（带 PWA），备用入口 `offline_calculator.html`（单文件无依赖）。
