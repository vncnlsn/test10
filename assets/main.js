(function(){var b=document.querySelector('.burger'),n=document.querySelector('.nav');
if(b)b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
var f=document.querySelectorAll('.fade');
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});f.forEach(function(x){io.observe(x)})}else f.forEach(function(x){x.classList.add('in')})})();
