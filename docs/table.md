关于表格识别，落叶ocr支持调用百度和腾讯的表格识别接口，假设已经在百度智能云与腾讯云中开通了相关服务并已经将密钥填入落叶ocr当中。处理重要数据（商业数据、机密数据或其它不能泄露的数据）请不要使用落叶ocr！

## 百度表格识别：

落叶ocr调用的是百度异步表格识别，百度的这个表格识别分为两个接口，一个是提交请求接口另一个是获取结果接口，换句话说就是先把数据提交到服务器，但是服务器识别是需要时间的，在识别完成之后，需要再从服务器获取识别的结果，那么问题来了，我怎么知道服务器啥时候能识别完成，于是在开发过程中我用一些复杂的表格做了测试，并将这个识别过程的时间设定为7秒，也就是说给服务器提交数据之后，等待7秒再次向服务器发送获取结果的请求，所以在落叶ocr当中调用百度表格识别，至少需要等待7秒才能看到返回的结果（通常是10秒左右）。

在落叶ocr中使用百度表格识别返回的结果是识别后的表格下载地址。你需要复制这个链接到下载器或者浏览器当中，将表格下载到本地查看识别结果。如果你等了好久没有返回下载地址，那说明你的表格实在是太复杂了（假设你填入的api没问题），7秒不够服务器给出识别结果，这时候请你换用腾讯表格识别或者另寻其它方法。

下面给出调用百度表格识别的例子。

要识别的表格如下图所示。

![](https://s3.ax1x.com/2021/01/29/yPFjwd.png)

调用百度表格识别后得到的结果如下图所示。

![](https://s3.ax1x.com/2021/01/29/yPkYkR.png)

复制下载地址将识别后的结果保存到本地并打开，下图即为识别的结果。

![](https://s3.ax1x.com/2021/01/29/yPk7As.png)

## 腾讯表格识别：

落叶ocr调用腾讯表格识别v2，和百度接口不同的是这个不用等很久，腾讯表格识别返回的结果是<u>进过base64编码后的excel数据</u>（这真的是编码后的数据不是乱码┑(￣Д ￣)┍）。如果你有能力，那么可用对这些数据解码得到excel。但这显然不是一种比较大众的方法，落叶ocr调用腾讯表格识别接口后，根据得到结果中的json数据，对其整理保存为excel，文件名为当时的时间，生成的excel文件保存在落叶ocr软件目录下的Table文件夹内（所以说要记住在磁盘中存放软件的位置，好吧如果你真的忘了，那面右键桌面上的快捷方式，点击属性，然后打开文件所在位置也能找到。啥？你没有在桌面上放快捷方式？那我也没办法，还是努力回忆保存位置吧）

?> 简而言之，腾讯表格识别返回的结果是经过base64编码后的excel数据，而落叶ocr会自动根据返回的json数据生成一个excel，这个excel文件保存在落叶ocr软件目录下的Table文件夹内。文件名就是当时的时间。

还用上门百度表格识别示例中的表格，来试试腾讯表格识别。

选择腾讯表格识别，之后得到的结果如下图所示。

![](https://s3.ax1x.com/2021/01/29/yPZKUJ.png)

然后进入软件目录中的Table文件夹，就可以找到excel（文件名是调用的时间）。如下图所示。

![](https://s3.ax1x.com/2021/01/29/yPeZRI.png)

![](https://s3.ax1x.com/2021/01/29/yPesY9.png)









