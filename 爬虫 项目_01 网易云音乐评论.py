# 1、找到加密的参数
# 2、将参数依据网易的方式进行加密
# 3、请求网易拿到i评论的数据


url  = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
#  请求方式是 post

data = {
"cursor": "-1",
"offset": "0",
"orderType": "1",
"pageNo":"1",
"pageSize": "20",
"rid": "R_SO_4_1325905146",
"threadId": "R_SO_4_1325905146",
}