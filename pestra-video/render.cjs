const { chromium } = require('playwright'); const { spawn } = require('child_process');
(async()=>{const FPS=30; const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/anim.html'); await p.evaluate(()=>document.fonts.ready);
const total=await p.evaluate(()=>TL.total); const N=Math.ceil(total*FPS);
const ff=spawn('ffmpeg',['-loglevel','error','-y','-f','image2pipe','-framerate',''+FPS,'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','silent.mp4'],{stdio:['pipe','inherit','inherit']});
for(let i=0;i<N;i++){await p.evaluate(t=>render(t),i/FPS); const buf=await p.screenshot({type:'jpeg',quality:92}); if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r)); if(i%300==0) console.log(i,'/',N);}
ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close();})();
