/* YES site behaviour: menu, reveal on scroll, ambient video (poster first). No dependencies. */
(function(){
  var d=document;
  // mobile menu
  var btn=d.querySelector('.menu-btn'), nav=d.getElementById('nav');
  if(btn&&nav){ btn.addEventListener('click',function(){ var o=nav.classList.toggle('open'); btn.setAttribute('aria-expanded',o?'true':'false'); btn.textContent=o?'CLOSE':'MENU'; }); }

  // reveal
  var rv=[].slice.call(d.querySelectorAll('.reveal'));
  if('IntersectionObserver' in window && rv.length){
    var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }); },{rootMargin:'0px 0px -8% 0px'});
    rv.forEach(function(el){ io.observe(el); });
  } else rv.forEach(function(el){ el.classList.add('in'); });

  // count-up for [data-count]
  var rm=window.matchMedia?window.matchMedia('(prefers-reduced-motion: reduce)'):{matches:false};
  function fmt(n,dp){ return Number(n).toLocaleString('en-AU',{minimumFractionDigits:dp,maximumFractionDigits:dp}); }
  var cs=[].slice.call(d.querySelectorAll('[data-count]'));
  function run(el){ var to=+el.getAttribute('data-count'), dp=+(el.getAttribute('data-dec')||0), pre=el.getAttribute('data-prefix')||'', suf=el.getAttribute('data-suffix')||'';
    if(rm.matches){ el.textContent=pre+fmt(to,dp)+suf; return; }
    var t0=null, dur=1100; function step(ts){ if(!t0) t0=ts; var p=Math.min(1,(ts-t0)/dur); var e=1-Math.pow(1-p,3); el.textContent=pre+fmt(to*e,dp)+suf; if(p<1) requestAnimationFrame(step); } requestAnimationFrame(step); }
  if('IntersectionObserver' in window && cs.length){ var io2=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ run(e.target); io2.unobserve(e.target); } }); },{rootMargin:'0px 0px -10% 0px'}); cs.forEach(function(el){ io2.observe(el); }); }
  else cs.forEach(run);

  // ambient video: loads only on wider screens, without reduced motion or data saver, and only while on screen
  var vids=[].slice.call(d.querySelectorAll('video[data-bgv]'));
  if(vids.length){
    var conn=navigator.connection||{};
    var allowed=function(){ return !rm.matches && !conn.saveData && window.innerWidth>=720; };
    var play=function(v){ var p=v.play(); if(p&&p.catch) p.catch(function(){}); };
    var start=function(v){ if(!v.getAttribute('data-on')){ v.setAttribute('data-on','1'); [].forEach.call(v.querySelectorAll('source[data-src]'),function(s){ s.src=s.getAttribute('data-src'); }); v.load(); } play(v); };
    vids.forEach(function(v){ v.muted=true; v.defaultMuted=true; v.playsInline=true; });
    if('IntersectionObserver' in window){
      var io3=new IntersectionObserver(function(es){ es.forEach(function(e){ var v=e.target; v._in=e.isIntersecting; if(e.isIntersecting){ if(allowed()) start(v); } else if(!v.paused) v.pause(); }); },{rootMargin:'160px 0px'});
      vids.forEach(function(v){ io3.observe(v); });
    } else if(allowed()) vids.forEach(start);
    d.addEventListener('visibilitychange',function(){ vids.forEach(function(v){ if(d.hidden){ if(!v.paused) v.pause(); } else if(v._in&&allowed()) start(v); }); });
    if(rm.addEventListener) rm.addEventListener('change',function(){ if(rm.matches) vids.forEach(function(v){ v.pause(); }); });
  }
})();
