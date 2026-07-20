# AI时代的哲学思维

> 在答案越来越快的时代，重新练习提出问题、辨认边界，并为自己的判断负责。

这是一个持续增量的课程与思考资料库，收录关于 AI、知识、意识、判断与人的课件、案例和阅读材料。

这里不急着给“人类的未来”下结论，而是把那些经常被跳过的中间问题重新摆回桌面：什么问题值得被提出？什么答案值得被相信？什么判断必须由人完成？我们希望成为什么样的人？

## 直接进入

- [打开项目云端主页](https://2023anita.github.io/ai-era-philosophical-thinking/)
- [课程目录](./courses/catalog.json)
- [增量添加说明](./CONTRIBUTING.md)

## 三个课件

| 课程 | 主题 | 云端入口 |
| --- | --- | --- |
| 01 | 问题先于答案 | [打开课件](./courses/01-question-before-answer/) |
| 02 | 人与模型之间 | [打开课件](./courses/02-human-and-model/) |
| 03 | 判断与责任 | [打开课件](./courses/03-judgement-and-responsibility/) |

当前三个课程入口已建立，原始课件文件待从项目来源目录接入。接入后会保留原始文件，并为 HTML、PDF 或其他格式提供可直接在线打开的版本。

## 项目结构

```text
assets/illustrations/       主页面解释图
courses/                    每个课件的独立目录
courses/catalog.json        主页课程目录
scripts/                    资源和链接检查
index.html                  GitHub Pages 主页
```

## 设计原则

- 先问清楚，再使用工具。
- 把模型输出和现实判断分开。
- 让抽象概念回到具体的人与行动。
- 新增内容沿着目录增量接入，不破坏已有入口。

## 本地检查

```bash
python3 scripts/validate_courses.py
```

## License

课程内容与配图的授权方式将在原始课件接入后补充说明。未经注明，不默认授予再发布权限。
