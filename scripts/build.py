from pathlib import Path
root=Path(__file__).resolve().parent.parent
w=root/'src';dest=root/'dist'
s=(w/'base.html').read_text()
s=s.replace('</style>',(w/'extra.css').read_text()+'\n</style>',1)
s=s.replace('<a href="#film">观看短片 ↗</a>','<a href="#principles">修养设计</a><a href="#prototype">交互体验</a><a href="#film">观看短片</a><a href="#sources">设计依据</a>')
s=s.replace('陪伴与提醒，遇到规则外的请求寻求确认。','陪伴、递物与提醒；初始设定中还会阻拦外出、扣住蛋糕罩，并把例外决定交给家属。')
s=s.replace('无法确定或风险较高时，暂停并寻求帮助。','无法确定或超出能力时，暂停对应协助、解释原因并提供替代；不以笼统风险为由锁门。')
s=s.replace('<section class="section wrap anchor" id="concept"',(w/'academic_context.html').read_text()+'\n<section class="section wrap anchor" id="concept"',1)
point=s.index('<section class="tension anchor"')
close=s.rfind('</section>',0,point)
s=s[:close]+(w/'product_depth.html').read_text()+s[close:]
s=s.replace('<section class="film wrap anchor"',(w/'additions.html').read_text()+'\n<section class="film wrap anchor"',1)
s=s.replace('03 / 把问题交还给生活','05 / 把问题交还给生活').replace('04 / 影片之后，继续追问','影片之后 / 继续追问')
s=s.replace('<input type="file" id="video-input"','<p class="video-check" id="video-duration-check" role="status">可选择本地短片进行观看。视频仅在当前浏览器中读取，不会上传。</p><input type="file" id="video-input"')
s=s.replace('<section class="closing"',(w/'afterfilm.html').read_text()+'\n<section class="closing"',1)
s=s.replace('</body>', '<script>\n'+(w/'prototype.js').read_text()+'\n</script></body>')
from video_transform import embed_video
s=embed_video(s)
dest.mkdir(exist_ok=True)
(dest/'index.html').write_text(s)
print('Built dist/index.html:',len(s),'characters')
