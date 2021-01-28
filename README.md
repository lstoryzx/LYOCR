# 落叶OCR（LYOCR）

平时一直都有文字识别的需求，也用过天若ocr、pandaocr、妙手ocr等等（有个关于ocr的聚合页，介绍了好多ocr及各自的特点，[请点击这里](https://adzhp.cn/wen-zi-shi-bie.html)），有的ocr功能不全，比如在我读英文文献的时候识别之后又有翻译的需求（之前读文献的时候一直在用这个小工具，觉得很不错，[请点击这里](https://copytranslator.github.io/)），也有的ocr集很多功能于一身，比如pandaocr（我以前也用过，功能很强大，在此也感谢pandaocr的作者开发了这么好用的工具）。因为有这方面的需求，所以很早之前就有想过，可以自己开发一个ocr，毕竟自己的需求自己才是最清楚的，于是假期自学了python后，就开始动手去写一个ocr。

落叶ocr使用tkinter开发，一个是因为自己刚自学python没多久，还没有学pyqt，另一个是因为只是做一个小工具，觉得tkinter也够用（虽然界面可能没那么好看）。

落叶ocr目前仅支持windows平台（要开发mac版首先我得先有台mac   ╮（╯＿╰）╭）。

[<u>**落叶ocr使用技巧及相关问题见文档**</u>](https://lstoryzx.github.io/LYOCR/)

项目地址：

- [GitHub](https://github.com/lstoryzx/LYOCR)
- [Gitee](https://gitee.com/lstoryzx/lyocr)

在GitHub或者Gitee上可以直接下载压缩包解压即可使用。如果GitHub上下载太慢，可以安装**Tampermonkey** 脚本[GitHub增强-高速下载](https://greasyfork.org/zh-CN/scripts/412245-github-%E5%A2%9E%E5%BC%BA-%E9%AB%98%E9%80%9F%E4%B8%8B%E8%BD%BD)，或者使用百度网盘：[链接请点击这里](https://pan.baidu.com/s/1tPn4qjFJYFTUQXqxMmPqZQ)，提取码为h9x3

落叶ocr使用python开发， 项目的LYOCR文件夹包含所有源码，用的pyinstaller打包。不含恶意代码，如果杀软报毒请加入白名单，不放心的话也可自行查看源代码。

软件没有离线识别引擎，要使用软件需自行申请百度、腾讯等平台的api接口（申请方法见文档），落叶ocr只是调用这写接口去实现文字识别，理论上来说用户使用的时候，所上传到相关平台服务器上的数据都是暂时的，但毕竟是别人家的，如果要识别的内容为商业或机密信息，请选用其他文字识别产品，且由此造成的损失与本人无关。

落叶OCR的截图功能并非我自己造的轮子，而是借鉴了csdn上的一篇博文（[请点击这里](https://blog.csdn.net/frostime/article/details/104798861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161182293516780262512266%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=161182293516780262512266&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-27-104798861.pc_search_result_cache&utm_term=python%E6%88%AA%E5%9B%BE)）。落叶ocr的源码可自行下载修改以便交流学习，但转载引用等行为请标明出处。

如果你有一些文档中没有说明的问题，欢迎提lssues或者联系我（邮箱：lstoryzx@126.com），我自学python没多久，而且也是第一次自己去做一个小工具，很期待与你交流。