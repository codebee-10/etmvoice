#1.Client 模式 （version:1.0）
###语音合成服务
1. 运行 bin/etmvoice_client_v1.0.exe
2. 查看api文档,发送请求
3. 正常的语音输出

#2.B-S 模式 （version:1.2）
###语音合成服务B-S
1. windows 上运行 bin/etmvoice_server_v1.2.exe
2. linux上 进入项目目录 ，然后运行 nohup python server.py 1>/dev/null  2>/var/log/etmvoice/etmvoice.log &
2. 打开浏览器运行 http://ip:10010
3. 查看bin/api文档发送请求
4. 请求过程中如果文字过长程序会自动将音频切割，会标注为语音1,语音2 ...
5. 浏览器需要支持 h5
6.0