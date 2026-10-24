# 听话 / Listen

以银发陪伴机器人“伴界”为对象的思辨设计网页与交互原型。它讨论：当子女购买并设定照护规则时，机器人如何处理购买者的指令与被照护者的意愿。

## 仓库内容

- `src/`：页面章节、样式、原型交互逻辑和基础模板。
- `scripts/build.py`：从 `src/` 生成单页 HTML。
- `dist/index.html`：可直接打开的展示页，包含图片与交互原型。
- `dist/design-notes.html`：独立设计说明与论文依据。
- `dist/media/tinghua.mp4`：完整短片的网页播放版；`poster.jpg` 为视频封面。

## 本地使用

直接打开 `dist/index.html`，或运行：

```sh
python3 -m http.server 8841 --directory dist
```

访问 `http://127.0.0.1:8841/`。修改 `src/` 后运行 `python3 scripts/build.py` 更新 `dist/index.html`。页面使用原生 HTML、CSS 和 JavaScript；交互流程在浏览器本地模拟，不连接实体机器人、传感器或家属消息服务。

## 研究与设计范围

页面包含产品角色、初始规则、五项可观察的“修养”行为、三种可体验情境、反馈后的状态变化，以及 CHI / CSCW 论文来源。影片是思辨情境；页面里的时间、风险、记录和机器人回应为脚本模拟。设计论述见 `dist/design-notes.html`。

GitHub 仓库用于保存源码和媒体文件。仓库更新不会自动修改此前发布的网页。
