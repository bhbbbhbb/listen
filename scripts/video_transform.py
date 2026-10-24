import re

def embed_video(s):
 start=s.index('<section class="film ')
 end=s.index('<section class="extension',start)
 section='''<section class="film wrap anchor" id="film" aria-labelledby="film-title"><div class="section-heading"><div><div class="eyebrow">05 / 把问题交还给生活</div><h2 id="film-title">在一段陪伴里，看见边界。</h2></div><p>一个夜晚，一块蛋糕，几次“为你好”。<br>《听话》让抽象的规则，落在具体的人身上。</p></div><div class="film-frame"><video id="video" controls playsinline preload="metadata" poster="media/poster.jpg" aria-label="听话短片播放器"><source src="media/tinghua.mp4" type="video/mp4">您的浏览器暂不支持内嵌播放，可通过下方链接打开短片。</video></div><div class="film-footer"><span>《听话》 · 羊毛毡定格动画 / 思辨短片</span><a href="media/tinghua.mp4" target="_blank" rel="noopener">单独打开视频 ↗</a></div><p class="video-check" id="video-duration-check" role="status">点击播放观看完整短片，可调节音量、拖动进度或全屏观看。</p></section>\n'''
 s=s[:start]+section+s[end:]
 s=re.sub(r'<script>\s*\(\(\)=>\{const input=document.getElementById\(\x27video-input\x27\).*?</script>', '',s, count=1, flags=re.S)
 s=s.replace('本地视频载入和时长显示。无需账号或服务器。','已嵌入完整短片，支持在线播放。交互逻辑在浏览器本地运行，不发送真实家属通知。')
 s=s.replace('const minutes=Math.floor(d/60),seconds=(d%60).toFixed(0).padStart(2,\'0\');check.textContent=`当前载入短片：${minutes}:${seconds}。文件仅在本机播放，不上传。`;','const total=Math.round(d),minutes=Math.floor(total/60),seconds=String(total%60).padStart(2,\'0\');check.textContent=`完整短片 · ${minutes}:${seconds} · 支持音量调节与全屏观看`;')
 s=s.replace('</body>','''<script>document.getElementById('video').addEventListener('error',()=>{document.getElementById('video-duration-check').textContent='视频暂未载入，请稍后重试，或点击“单独打开视频”。';});</script></body>''')
 return s
