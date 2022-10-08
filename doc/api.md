# 微博API说明
LastEdit Date: 2022-10-08


## 接口列表
### 搜索接口
返回格式：Web Html，文章数据存放在页面的JavaScript变量当中<br>
https://s.weibo.com/weibo?q={keyword}&page={page_number}<br>
&emsp;示例：https://s.weibo.com/weibo?q=中国大学生&page=5

### 评论接口
返回格式：Json<br>
https://m.weibo.cn/comments/hotflow?mid={mid} <br>
&emsp;示例：https://m.weibo.cn/comments/hotflow?mid=4820791684237361
