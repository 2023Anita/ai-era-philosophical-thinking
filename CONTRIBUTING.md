# 如何继续添加课程

这个项目使用“一个课程目录 + 一条目录登记”的增量方式。

## 添加步骤

1. 在 `courses/` 下建立新的英文 slug 文件夹。
2. 将在线入口命名为 `index.html`。
3. 原始 HTML、PPTX、PDF 或其他文件放进该课程目录下的 `original/`；如果是自包含 HTML，也要保留其可直接打开的 `index.html`。
4. 在 `courses/catalog.json` 的 `courses` 数组里增加一条记录。
5. 从课件中提取可公开使用的代表性图片，放入 `assets/course-previews/` 或课程自己的资源目录。
6. 运行 `python3 scripts/validate_courses.py`。
7. 确认首页课程卡片、真实图片和云端入口都能打开。

## 目录记录模板

```json
{
  "id": "new-course-slug",
  "title": "新课件标题",
  "description": "一句话说明这份课件要带读者看见什么。",
  "tags": ["主题一", "主题二"],
  "path": "./courses/new-course-slug/",
  "status": "ready",
  "statusLabel": "在线阅读"
}
```

## 保持稳定的约定

- 不删除旧课程入口；如果课件更新，保留清晰的版本说明。
- 课程资源使用相对路径，确保 GitHub Pages 和仓库内链接一致。
- 大图放入课程自己的资源目录，不把所有资源堆在主页目录。
- 主页图片优先来自真实课件，保留来源关系，不用泛化配图代替课程内容。
- 课程标题和简介先写清楚“读者会看见什么”，再写技术格式。
