(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{18:function(e,t,a){e.exports=a.p+"static/media/logo.5d5d9eef.svg"},21:function(e,t,a){e.exports=a(47)},44:function(e,t,a){},46:function(e,t,a){},47:function(e,t,a){"use strict";a.r(t);var n=a(1),o=a.n(n),r=a(13),s=a.n(r),c=a(2),i=a.n(c),l=(a(44),a(3)),u=a.n(l),p=a(14),d=a(15),h=a(16),f=a(19),m=a(17),v=a(20),g=a(18),w=a.n(g),k=(a(46),function(e){function t(){var e,a;Object(d.a)(this,t);for(var n=arguments.length,o=new Array(n),r=0;r<n;r++)o[r]=arguments[r];return(a=Object(f.a)(this,(e=Object(m.a)(t)).call.apply(e,[this].concat(o)))).state={},a}return Object(v.a)(t,e),Object(h.a)(t,[{key:"componentDidMount",value:function(){var e=Object(p.a)(u.a.mark(function e(){var t;return u.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,i()({url:"http://localhost:8000/api/polls/questions/",method:"get"});case 3:t=e.sent,this.setState({data:t.data}),e.next=10;break;case 7:e.prev=7,e.t0=e.catch(0),console.log(e.t0);case 10:case"end":return e.stop()}},e,this,[[0,7]])}));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){return console.log(this.state),o.a.createElement("div",{className:"App"},o.a.createElement("header",{className:"App-header"},o.a.createElement("img",{src:w.a,className:"App-logo",alt:"logo"}),o.a.createElement("br",null),this.state.data?this.state.data[0].question_text:null))}}]),t}(o.a.Component));Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));i.a.defaults.xsrfCookieName="csrftoken",i.a.defaults.xsrfHeaderName="X-CSRFToken",i.a.defaults.baseURL="http://localhost:8000",i.a.interceptors.request.use(function(e){var t=localStorage.getItem("_kAZ%U0.token");return t&&(e.headers.Authorization="Bearer ".concat(t)),e},function(e){return Promise.reject(e)}),s.a.render(o.a.createElement(k,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[21,1,2]]]);
//# sourceMappingURL=main.312ed0c7.chunk.js.map