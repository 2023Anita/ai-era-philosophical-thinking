# AI时代的哲学思维

> 在答案越来越快的时代，重新练习提出问题、辨认边界，并为自己的判断负责。

这是一个持续增量的公开课资料库，当前收录三堂真实 HTML 公开课：Pace Layers 与个人 AI 系统、从兴趣进入 AI 学习、以及行动与环境设计。

三堂课看似分别谈技术、兴趣和意志力，底层却在处理同一个现实：当变化太快、目标太大、入口太难时，人如何把一次尝试变成下一次仍然可以复用的路径。

## 直接进入

- [打开项目云端主页](https://2023anita.github.io/ai-era-philosophical-thinking/)
- [课程目录](./courses/catalog.json)
- [增量添加说明](./CONTRIBUTING.md)

## 三个课件

| 课程 | 主题 | 云端入口 |
| --- | --- | --- |
| 01 | AI时代的 Pace Layers | [打开课件](./courses/01-question-before-answer/) |
| 02 | AI时代的兴趣 | [打开课件](./courses/02-human-and-model/) |
| 03 | 你不是缺少意志力 | [打开课件](./courses/03-judgement-and-responsibility/) |

三个课程入口已经接入真实 HTML 课件。第一堂课保留了课程方案与素材目录，第二堂课把 HTML 内嵌图片提取到课程资源目录，第三堂课保留了原始课件中的插图资源。

主页课程卡片与正文插图均来自这三堂课，不再使用独立生成的占位配图。

## 项目结构

```text
assets/course-previews/     从真实课件提取的主页预览图
courses/                    每个课件的独立目录
courses/catalog.json        主页课程目录
scripts/                    资源和链接检查
index.html                  GitHub Pages 主页
```

## 设计原则

- 让工具在快层竞争，把证据、标准和责任留在慢层。
- 从玩到做，在做中学，让真实问题为理论提供位置。
- 让进步尽快被看见，把行动设计成可以继续的循环。
- 新增内容沿着目录增量接入，不破坏已有入口。

## 本地检查

```bash
python3 scripts/validate_courses.py
```

## License

课程内容与配图的授权方式将在原始课件接入后补充说明。未经注明，不默认授予再发布权限。
