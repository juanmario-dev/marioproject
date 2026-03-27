"use strict";

function ownKeys(e, r) { var t = Object.keys(e); if (Object.getOwnPropertySymbols) { var o = Object.getOwnPropertySymbols(e); r && (o = o.filter(function (r) { return Object.getOwnPropertyDescriptor(e, r).enumerable; })), t.push.apply(t, o); } return t; }
function _objectSpread(e) { for (var r = 1; r < arguments.length; r++) { var t = null != arguments[r] ? arguments[r] : {}; r % 2 ? ownKeys(Object(t), !0).forEach(function (r) { _defineProperty(e, r, t[r]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : ownKeys(Object(t)).forEach(function (r) { Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r)); }); } return e; }
function _defineProperty(obj, key, value) { key = _toPropertyKey(key); if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
function _regeneratorRuntime() { "use strict"; /*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/facebook/regenerator/blob/main/LICENSE */ _regeneratorRuntime = function _regeneratorRuntime() { return e; }; var t, e = {}, r = Object.prototype, n = r.hasOwnProperty, o = Object.defineProperty || function (t, e, r) { t[e] = r.value; }, i = "function" == typeof Symbol ? Symbol : {}, a = i.iterator || "@@iterator", c = i.asyncIterator || "@@asyncIterator", u = i.toStringTag || "@@toStringTag"; function define(t, e, r) { return Object.defineProperty(t, e, { value: r, enumerable: !0, configurable: !0, writable: !0 }), t[e]; } try { define({}, ""); } catch (t) { define = function define(t, e, r) { return t[e] = r; }; } function wrap(t, e, r, n) { var i = e && e.prototype instanceof Generator ? e : Generator, a = Object.create(i.prototype), c = new Context(n || []); return o(a, "_invoke", { value: makeInvokeMethod(t, r, c) }), a; } function tryCatch(t, e, r) { try { return { type: "normal", arg: t.call(e, r) }; } catch (t) { return { type: "throw", arg: t }; } } e.wrap = wrap; var h = "suspendedStart", l = "suspendedYield", f = "executing", s = "completed", y = {}; function Generator() {} function GeneratorFunction() {} function GeneratorFunctionPrototype() {} var p = {}; define(p, a, function () { return this; }); var d = Object.getPrototypeOf, v = d && d(d(values([]))); v && v !== r && n.call(v, a) && (p = v); var g = GeneratorFunctionPrototype.prototype = Generator.prototype = Object.create(p); function defineIteratorMethods(t) { ["next", "throw", "return"].forEach(function (e) { define(t, e, function (t) { return this._invoke(e, t); }); }); } function AsyncIterator(t, e) { function invoke(r, o, i, a) { var c = tryCatch(t[r], t, o); if ("throw" !== c.type) { var u = c.arg, h = u.value; return h && "object" == _typeof(h) && n.call(h, "__await") ? e.resolve(h.__await).then(function (t) { invoke("next", t, i, a); }, function (t) { invoke("throw", t, i, a); }) : e.resolve(h).then(function (t) { u.value = t, i(u); }, function (t) { return invoke("throw", t, i, a); }); } a(c.arg); } var r; o(this, "_invoke", { value: function value(t, n) { function callInvokeWithMethodAndArg() { return new e(function (e, r) { invoke(t, n, e, r); }); } return r = r ? r.then(callInvokeWithMethodAndArg, callInvokeWithMethodAndArg) : callInvokeWithMethodAndArg(); } }); } function makeInvokeMethod(e, r, n) { var o = h; return function (i, a) { if (o === f) throw new Error("Generator is already running"); if (o === s) { if ("throw" === i) throw a; return { value: t, done: !0 }; } for (n.method = i, n.arg = a;;) { var c = n.delegate; if (c) { var u = maybeInvokeDelegate(c, n); if (u) { if (u === y) continue; return u; } } if ("next" === n.method) n.sent = n._sent = n.arg;else if ("throw" === n.method) { if (o === h) throw o = s, n.arg; n.dispatchException(n.arg); } else "return" === n.method && n.abrupt("return", n.arg); o = f; var p = tryCatch(e, r, n); if ("normal" === p.type) { if (o = n.done ? s : l, p.arg === y) continue; return { value: p.arg, done: n.done }; } "throw" === p.type && (o = s, n.method = "throw", n.arg = p.arg); } }; } function maybeInvokeDelegate(e, r) { var n = r.method, o = e.iterator[n]; if (o === t) return r.delegate = null, "throw" === n && e.iterator["return"] && (r.method = "return", r.arg = t, maybeInvokeDelegate(e, r), "throw" === r.method) || "return" !== n && (r.method = "throw", r.arg = new TypeError("The iterator does not provide a '" + n + "' method")), y; var i = tryCatch(o, e.iterator, r.arg); if ("throw" === i.type) return r.method = "throw", r.arg = i.arg, r.delegate = null, y; var a = i.arg; return a ? a.done ? (r[e.resultName] = a.value, r.next = e.nextLoc, "return" !== r.method && (r.method = "next", r.arg = t), r.delegate = null, y) : a : (r.method = "throw", r.arg = new TypeError("iterator result is not an object"), r.delegate = null, y); } function pushTryEntry(t) { var e = { tryLoc: t[0] }; 1 in t && (e.catchLoc = t[1]), 2 in t && (e.finallyLoc = t[2], e.afterLoc = t[3]), this.tryEntries.push(e); } function resetTryEntry(t) { var e = t.completion || {}; e.type = "normal", delete e.arg, t.completion = e; } function Context(t) { this.tryEntries = [{ tryLoc: "root" }], t.forEach(pushTryEntry, this), this.reset(!0); } function values(e) { if (e || "" === e) { var r = e[a]; if (r) return r.call(e); if ("function" == typeof e.next) return e; if (!isNaN(e.length)) { var o = -1, i = function next() { for (; ++o < e.length;) if (n.call(e, o)) return next.value = e[o], next.done = !1, next; return next.value = t, next.done = !0, next; }; return i.next = i; } } throw new TypeError(_typeof(e) + " is not iterable"); } return GeneratorFunction.prototype = GeneratorFunctionPrototype, o(g, "constructor", { value: GeneratorFunctionPrototype, configurable: !0 }), o(GeneratorFunctionPrototype, "constructor", { value: GeneratorFunction, configurable: !0 }), GeneratorFunction.displayName = define(GeneratorFunctionPrototype, u, "GeneratorFunction"), e.isGeneratorFunction = function (t) { var e = "function" == typeof t && t.constructor; return !!e && (e === GeneratorFunction || "GeneratorFunction" === (e.displayName || e.name)); }, e.mark = function (t) { return Object.setPrototypeOf ? Object.setPrototypeOf(t, GeneratorFunctionPrototype) : (t.__proto__ = GeneratorFunctionPrototype, define(t, u, "GeneratorFunction")), t.prototype = Object.create(g), t; }, e.awrap = function (t) { return { __await: t }; }, defineIteratorMethods(AsyncIterator.prototype), define(AsyncIterator.prototype, c, function () { return this; }), e.AsyncIterator = AsyncIterator, e.async = function (t, r, n, o, i) { void 0 === i && (i = Promise); var a = new AsyncIterator(wrap(t, r, n, o), i); return e.isGeneratorFunction(r) ? a : a.next().then(function (t) { return t.done ? t.value : a.next(); }); }, defineIteratorMethods(g), define(g, u, "Generator"), define(g, a, function () { return this; }), define(g, "toString", function () { return "[object Generator]"; }), e.keys = function (t) { var e = Object(t), r = []; for (var n in e) r.push(n); return r.reverse(), function next() { for (; r.length;) { var t = r.pop(); if (t in e) return next.value = t, next.done = !1, next; } return next.done = !0, next; }; }, e.values = values, Context.prototype = { constructor: Context, reset: function reset(e) { if (this.prev = 0, this.next = 0, this.sent = this._sent = t, this.done = !1, this.delegate = null, this.method = "next", this.arg = t, this.tryEntries.forEach(resetTryEntry), !e) for (var r in this) "t" === r.charAt(0) && n.call(this, r) && !isNaN(+r.slice(1)) && (this[r] = t); }, stop: function stop() { this.done = !0; var t = this.tryEntries[0].completion; if ("throw" === t.type) throw t.arg; return this.rval; }, dispatchException: function dispatchException(e) { if (this.done) throw e; var r = this; function handle(n, o) { return a.type = "throw", a.arg = e, r.next = n, o && (r.method = "next", r.arg = t), !!o; } for (var o = this.tryEntries.length - 1; o >= 0; --o) { var i = this.tryEntries[o], a = i.completion; if ("root" === i.tryLoc) return handle("end"); if (i.tryLoc <= this.prev) { var c = n.call(i, "catchLoc"), u = n.call(i, "finallyLoc"); if (c && u) { if (this.prev < i.catchLoc) return handle(i.catchLoc, !0); if (this.prev < i.finallyLoc) return handle(i.finallyLoc); } else if (c) { if (this.prev < i.catchLoc) return handle(i.catchLoc, !0); } else { if (!u) throw new Error("try statement without catch or finally"); if (this.prev < i.finallyLoc) return handle(i.finallyLoc); } } } }, abrupt: function abrupt(t, e) { for (var r = this.tryEntries.length - 1; r >= 0; --r) { var o = this.tryEntries[r]; if (o.tryLoc <= this.prev && n.call(o, "finallyLoc") && this.prev < o.finallyLoc) { var i = o; break; } } i && ("break" === t || "continue" === t) && i.tryLoc <= e && e <= i.finallyLoc && (i = null); var a = i ? i.completion : {}; return a.type = t, a.arg = e, i ? (this.method = "next", this.next = i.finallyLoc, y) : this.complete(a); }, complete: function complete(t, e) { if ("throw" === t.type) throw t.arg; return "break" === t.type || "continue" === t.type ? this.next = t.arg : "return" === t.type ? (this.rval = this.arg = t.arg, this.method = "return", this.next = "end") : "normal" === t.type && e && (this.next = e), y; }, finish: function finish(t) { for (var e = this.tryEntries.length - 1; e >= 0; --e) { var r = this.tryEntries[e]; if (r.finallyLoc === t) return this.complete(r.completion, r.afterLoc), resetTryEntry(r), y; } }, "catch": function _catch(t) { for (var e = this.tryEntries.length - 1; e >= 0; --e) { var r = this.tryEntries[e]; if (r.tryLoc === t) { var n = r.completion; if ("throw" === n.type) { var o = n.arg; resetTryEntry(r); } return o; } } throw new Error("illegal catch attempt"); }, delegateYield: function delegateYield(e, r, n) { return this.delegate = { iterator: values(e), resultName: r, nextLoc: n }, "next" === this.method && (this.arg = t), y; } }, e; }
function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }
function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }
function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : String(i); }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
/* -------------------------------------------------------------------------- */
/*                                    Utils                                   */
/* -------------------------------------------------------------------------- */
var docReady = function docReady(fn) {
  // see if DOM is already available
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fn);
  } else {
    setTimeout(fn, 1);
  }
};
var isRTL = function isRTL() {
  return document.querySelector('html').getAttribute('dir') === 'rtl';
};
var resize = function resize(fn) {
  return window.addEventListener('resize', fn);
};
var isIterableArray = function isIterableArray(array) {
  return Array.isArray(array) && !!array.length;
};
var camelize = function camelize(str) {
  var text = str.replace(/[-_\s.]+(.)?/g, function (match, capture) {
    if (capture) {
      return capture.toUpperCase();
    }
    return '';
  });
  return "".concat(text.substr(0, 1).toLowerCase()).concat(text.substr(1));
};
var getData = function getData(el, data) {
  try {
    return JSON.parse(el.dataset[camelize(data)]);
  } catch (e) {
    return el.dataset[camelize(data)];
  }
};

/* ----------------------------- Colors function ---------------------------- */

var hexToRgb = function hexToRgb(hexValue) {
  var hex;
  hexValue.indexOf('#') === 0 ? hex = hexValue.substring(1) : hex = hexValue;
  // Expand shorthand form (e.g. "03F") to full form (e.g. "0033FF")
  var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex.replace(shorthandRegex, function (m, r, g, b) {
    return r + r + g + g + b + b;
  }));
  return result ? [parseInt(result[1], 16), parseInt(result[2], 16), parseInt(result[3], 16)] : null;
};
var rgbaColor = function rgbaColor() {
  var color = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '#fff';
  var alpha = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 0.5;
  return "rgba(".concat(hexToRgb(color), ", ").concat(alpha, ")");
};

/* --------------------------------- Colors --------------------------------- */

var getColor = function getColor(name) {
  var dom = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : document.documentElement;
  return getComputedStyle(dom).getPropertyValue("--hideaway-".concat(name)).trim();
};
var getColors = function getColors(dom) {
  return {
    primary: getColor('primary', dom),
    secondary: getColor('secondary', dom),
    success: getColor('success', dom),
    info: getColor('info', dom),
    warning: getColor('warning', dom),
    danger: getColor('danger', dom),
    light: getColor('light', dom),
    dark: getColor('dark', dom),
    white: getColor('white', dom),
    black: getColor('black', dom),
    emphasis: getColor('emphasis-color', dom)
  };
};
var getGrays = function getGrays(dom) {
  return {
    100: getColor('gray-100', dom),
    200: getColor('gray-200', dom),
    300: getColor('gray-300', dom),
    400: getColor('gray-400', dom),
    500: getColor('gray-500', dom),
    600: getColor('gray-600', dom),
    700: getColor('gray-700', dom),
    800: getColor('gray-800', dom),
    900: getColor('gray-900', dom),
    1000: getColor('gray-1000', dom),
    1100: getColor('gray-1100', dom)
  };
};
var hasClass = function hasClass(el, className) {
  !el && false;
  return el.classList.value.includes(className);
};
var addClass = function addClass(el, className) {
  el.classList.add(className);
};
var removeClass = function removeClass(el, className) {
  el.classList.remove(className);
};
var breakpoints = {
  xs: 0,
  sm: 576,
  md: 768,
  lg: 992,
  xl: 1200,
  xxl: 1540
};
var getOffset = function getOffset(el) {
  var rect = el.getBoundingClientRect();
  var scrollLeft = window.pageXOffset || document.documentElement.scrollLeft;
  var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  return {
    top: rect.top + scrollTop,
    left: rect.left + scrollLeft
  };
};
var isScrolledIntoView = function isScrolledIntoView(el) {
  var top = el.offsetTop;
  var left = el.offsetLeft;
  var width = el.offsetWidth;
  var height = el.offsetHeight;
  while (el.offsetParent) {
    // eslint-disable-next-line no-param-reassign
    el = el.offsetParent;
    top += el.offsetTop;
    left += el.offsetLeft;
  }
  return {
    all: top >= window.pageYOffset && left >= window.pageXOffset && top + height <= window.pageYOffset + window.innerHeight && left + width <= window.pageXOffset + window.innerWidth,
    partial: top < window.pageYOffset + window.innerHeight && left < window.pageXOffset + window.innerWidth && top + height > window.pageYOffset && left + width > window.pageXOffset
  };
};
var isElementIntoView = function isElementIntoView(el) {
  var position = el.getBoundingClientRect();
  // checking whether fully visible
  if (position.top >= 0 && position.bottom <= window.innerHeight) {
    return true;
  }

  // checking for partial visibility
  if (position.top < window.innerHeight && position.bottom >= 0) {
    return true;
  }
  return null;
};
var getBreakpoint = function getBreakpoint(el) {
  var classes = el && el.classList.value;
  var breakpoint;
  if (classes) {
    breakpoint = breakpoints[classes.split(' ').filter(function (cls) {
      return cls.includes('navbar-expand-');
    }).pop().split('-').pop()];
  }
  return breakpoint;
};
var getCurrentScreenBreakpoint = function getCurrentScreenBreakpoint() {
  var currentBreakpoint = '';
  if (window.innerWidth >= breakpoints.xl) {
    currentBreakpoint = 'xl';
  } else if (window.innerWidth >= breakpoints.lg) {
    currentBreakpoint = 'lg';
  } else if (window.innerWidth >= breakpoints.md) {
    currentBreakpoint = 'md';
  } else {
    currentBreakpoint = 'sm';
  }
  var breakpointStartVal = breakpoints[currentBreakpoint];
  return {
    currentBreakpoint: currentBreakpoint,
    breakpointStartVal: breakpointStartVal
  };
};
/* --------------------------------- Cookie --------------------------------- */

var setCookie = function setCookie(name, value, expire) {
  var expires = new Date();
  expires.setTime(expires.getTime() + expire);
  document.cookie = "".concat(name, "=").concat(value, ";expires=").concat(expires.toUTCString());
};
var getCookie = function getCookie(name) {
  var keyValue = document.cookie.match("(^|;) ?".concat(name, "=([^;]*)(;|$)"));
  return keyValue ? keyValue[2] : keyValue;
};

/* ---------------------------------- Store --------------------------------- */

var getItemFromStore = function getItemFromStore(key, defaultValue) {
  var store = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : localStorage;
  try {
    return JSON.parse(store.getItem(key)) || defaultValue;
  } catch (_unused) {
    return store.getItem(key) || defaultValue;
  }
};
var setItemToStore = function setItemToStore(key, payload) {
  var store = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : localStorage;
  return store.setItem(key, payload);
};
var getStoreSpace = function getStoreSpace() {
  var store = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : localStorage;
  return parseFloat((escape(encodeURIComponent(JSON.stringify(store))).length / (1024 * 1024)).toFixed(2));
};

/* get Dates between */

var getDates = function getDates(startDate, endDate) {
  var interval = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : 1000 * 60 * 60 * 24;
  var duration = endDate - startDate;
  var steps = duration / interval;
  return Array.from({
    length: steps + 1
  }, function (v, i) {
    return new Date(startDate.valueOf() + interval * i);
  });
};

/* Get Random Number */
var getRandomNumber = function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
};
var utils = {
  docReady: docReady,
  breakpoints: breakpoints,
  resize: resize,
  isIterableArray: isIterableArray,
  camelize: camelize,
  getData: getData,
  hasClass: hasClass,
  addClass: addClass,
  hexToRgb: hexToRgb,
  rgbaColor: rgbaColor,
  getColor: getColor,
  getColors: getColors,
  getGrays: getGrays,
  getOffset: getOffset,
  isScrolledIntoView: isScrolledIntoView,
  getBreakpoint: getBreakpoint,
  setCookie: setCookie,
  getCookie: getCookie,
  getItemFromStore: getItemFromStore,
  setItemToStore: setItemToStore,
  getStoreSpace: getStoreSpace,
  getDates: getDates,
  getRandomNumber: getRandomNumber,
  removeClass: removeClass,
  isElementIntoView: isElementIntoView,
  getCurrentScreenBreakpoint: getCurrentScreenBreakpoint,
  isRTL: isRTL
};

/* -------------------------------------------------------------------------- */
/*                                  Detector                                  */
/* -------------------------------------------------------------------------- */

var detectorInit = function detectorInit() {
  var _window = window,
    is = _window.is;
  var html = document.querySelector('html');
  is.opera() && addClass(html, 'opera');
  is.mobile() && addClass(html, 'mobile');
  is.firefox() && addClass(html, 'firefox');
  is.safari() && addClass(html, 'safari');
  is.ios() && addClass(html, 'ios');
  is.iphone() && addClass(html, 'iphone');
  is.ipad() && addClass(html, 'ipad');
  is.ie() && addClass(html, 'ie');
  is.edge() && addClass(html, 'edge');
  is.chrome() && addClass(html, 'chrome');
  is.mac() && addClass(html, 'osx');
  is.windows() && addClass(html, 'windows');
  navigator.userAgent.match('CriOS') && addClass(html, 'chrome');
};

/*-----------------------------------------------
|   DomNode
-----------------------------------------------*/
var DomNode = /*#__PURE__*/function () {
  function DomNode(node) {
    _classCallCheck(this, DomNode);
    this.node = node;
  }
  _createClass(DomNode, [{
    key: "addClass",
    value: function addClass(className) {
      this.isValidNode() && this.node.classList.add(className);
    }
  }, {
    key: "removeClass",
    value: function removeClass(className) {
      this.isValidNode() && this.node.classList.remove(className);
    }
  }, {
    key: "toggleClass",
    value: function toggleClass(className) {
      this.isValidNode() && this.node.classList.toggle(className);
    }
  }, {
    key: "hasClass",
    value: function hasClass(className) {
      this.isValidNode() && this.node.classList.contains(className);
    }
  }, {
    key: "data",
    value: function data(key) {
      if (this.isValidNode()) {
        try {
          return JSON.parse(this.node.dataset[this.camelize(key)]);
        } catch (e) {
          return this.node.dataset[this.camelize(key)];
        }
      }
      return null;
    }
  }, {
    key: "attr",
    value: function attr(name) {
      return this.isValidNode() && this.node[name];
    }
  }, {
    key: "setAttribute",
    value: function setAttribute(name, value) {
      this.isValidNode() && this.node.setAttribute(name, value);
    }
  }, {
    key: "removeAttribute",
    value: function removeAttribute(name) {
      this.isValidNode() && this.node.removeAttribute(name);
    }
  }, {
    key: "setProp",
    value: function setProp(name, value) {
      this.isValidNode() && (this.node[name] = value);
    }
  }, {
    key: "on",
    value: function on(event, cb) {
      this.isValidNode() && this.node.addEventListener(event, cb);
    }
  }, {
    key: "isValidNode",
    value: function isValidNode() {
      return !!this.node;
    }

    // eslint-disable-next-line class-methods-use-this
  }, {
    key: "camelize",
    value: function camelize(str) {
      var text = str.replace(/[-_\s.]+(.)?/g, function (_, c) {
        return c ? c.toUpperCase() : '';
      });
      return "".concat(text.substr(0, 1).toLowerCase()).concat(text.substr(1));
    }
  }]);
  return DomNode;
}();
/* --------------------------------------------------------------------------
|                                 bg player                                  |
--------------------------------------------------------------------------- */
var bgPlayerInit = function bgPlayerInit() {
  var Selector = {
    DATA_YOUTUBE_EMBED: '[data-youtube-embed]',
    YT_VIDEO: '.bg-youtube'
  };
  var DATA_KEY = {
    YOUTUBE_EMBED: 'youtube-embed'
  };
  var ClassName = {
    LOADED: 'loaded'
  };
  var Events = {
    SCROLL: 'scroll',
    LOADING: 'loading',
    DOM_CONTENT_LOADED: 'DOMContentLoaded'
  };
  var youtubeEmbedElements = document.querySelectorAll(Selector.DATA_YOUTUBE_EMBED);
  var loadVideo = function loadVideo() {
    function setupPlayer() {
      window.YT.ready(function () {
        youtubeEmbedElements.forEach(function (youtubeEmbedElement) {
          var userOptions = utils.getData(youtubeEmbedElement, DATA_KEY.YOUTUBE_EMBED);
          var defaultOptions = {
            videoId: 'hLpy-DRuiz0',
            startSeconds: 1,
            endSeconds: 50
          };
          var options = window._.merge(defaultOptions, userOptions);
          var youTubePlayer = function youTubePlayer() {
            // eslint-disable-next-line
            new YT.Player(youtubeEmbedElement, {
              videoId: options.videoId,
              playerVars: {
                autoplay: 1,
                disablekb: 1,
                controls: 0,
                modestbranding: 1,
                // Hide the Youtube Logo
                loop: 1,
                fs: 0,
                enablejsapi: 0,
                start: options === null || options === void 0 ? void 0 : options.startSeconds,
                end: options === null || options === void 0 ? void 0 : options.endSeconds
              },
              events: {
                onReady: function onReady(e) {
                  e.target.mute();
                  e.target.playVideo();
                },
                onStateChange: function onStateChange(e) {
                  if (e.data === window.YT.PlayerState.PLAYING) {
                    // eslint-disable-next-line max-len
                    document.querySelectorAll(Selector.DATA_YOUTUBE_EMBED).forEach(function (embedElement) {
                      embedElement.classList.add(ClassName.LOADED);
                    });
                  }
                  if (e.data === window.YT.PlayerState.PAUSED) {
                    e.target.playVideo();
                  }
                  if (e.data === window.YT.PlayerState.ENDED) {
                    // Loop from starting point
                    e.target.seekTo(options.startSeconds);
                  }
                }
              }
            });
          };
          youTubePlayer();
        });
      });
    }
    var tag = document.createElement('script');
    tag.src = 'https://www.youtube.com/iframe_api';
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    tag.onload = setupPlayer;
  };
  if (document.readyState !== Events.LOADING) {
    loadVideo();
  } else {
    document.addEventListener(Events.DOM_CONTENT_LOADED, function () {
      return loadVideo();
    });
  }

  /* --------------------------------------------------------------------------
  |                                 Adjust BG Ratio                           |
  --------------------------------------------------------------------------- */

  var adjustBackgroundRatio = function adjustBackgroundRatio() {
    var ytElements = document.querySelectorAll(Selector.YT_VIDEO);
    ytElements.forEach(function (ytEl) {
      var ytElement = ytEl;
      var width = ytElement.parentElement.offsetWidth + 200;
      var height = width * 9 / 16;
      var minHeight = ytElement.parentElement.offsetHeight + 112;
      var minWidth = minHeight * 16 / 9;
      ytElement.style.width = "".concat(width, "px");
      ytElement.style.height = "".concat(height, "px");
      ytElement.style.minHeight = "".concat(minHeight, "px");
      ytElement.style.minWidth = "".concat(minWidth, "px");
    });
  };
  adjustBackgroundRatio();
  document.addEventListener(Events.SCROLL, function () {
    return adjustBackgroundRatio();
  });
};

/*-----------------------------------------------
|   Dashboard Table dropdown
-----------------------------------------------*/
var dropdownMenuInit = function dropdownMenuInit() {
  // Only for ios
  if (window.is.ios()) {
    var Event = {
      SHOWN_BS_DROPDOWN: 'shown.bs.dropdown',
      HIDDEN_BS_DROPDOWN: 'hidden.bs.dropdown'
    };
    var Selector = {
      TABLE_RESPONSIVE: '.table-responsive',
      DROPDOWN_MENU: '.dropdown-menu'
    };
    document.querySelectorAll(Selector.TABLE_RESPONSIVE).forEach(function (table) {
      table.addEventListener(Event.SHOWN_BS_DROPDOWN, function (e) {
        var t = e.currentTarget;
        if (t.scrollWidth > t.clientWidth) {
          t.style.paddingBottom = "".concat(e.target.nextElementSibling.clientHeight, "px");
        }
      });
      table.addEventListener(Event.HIDDEN_BS_DROPDOWN, function (e) {
        e.currentTarget.style.paddingBottom = '';
      });
    });
  }
};

/* -------------------------------------------------------------------------- */
/*                           Open dropdown on hover                           */
/* -------------------------------------------------------------------------- */

var dropdownOnHover = function dropdownOnHover() {
  var navbarArea = document.querySelector('[data-top-nav-dropdowns]');
  if (navbarArea) {
    navbarArea.addEventListener('mouseover', function (e) {
      if (e.target.className.includes !== undefined) {
        if (e.target.className.includes('dropdown-toggle') && window.innerWidth > 992) {
          var dropdownInstance = new window.bootstrap.Dropdown(e.target);
          dropdownInstance._element.classList.add('show');
          dropdownInstance._menu.classList.add('show');
          dropdownInstance._menu.setAttribute('data-bs-popper', 'none');
          e.target.parentNode.addEventListener('mouseleave', function () {
            dropdownInstance.hide();
          });
        }
      }
    });
  }
};

/* -------------------------------------------------------------------------- */
/*                               Form-Processor                               */
/* -------------------------------------------------------------------------- */

var formInit = function formInit() {
  var zforms = document.querySelectorAll('[data-form]');
  if (zforms.length) {
    zforms.forEach(function (form) {
      form.addEventListener('submit', /*#__PURE__*/function () {
        var _ref = _asyncToGenerator( /*#__PURE__*/_regeneratorRuntime().mark(function _callee(e) {
          var feedbackEl, formData, response, result;
          return _regeneratorRuntime().wrap(function _callee$(_context) {
            while (1) switch (_context.prev = _context.next) {
              case 0:
                e.preventDefault();
                feedbackEl = form.querySelector('.feedback');
                formData = new FormData(form);
                _context.prev = 3;
                _context.next = 6;
                return fetch("https://formspree.io/f/".concat('YOUR_FORM_ID'), {
                  method: 'POST',
                  body: formData,
                  headers: {
                    Accept: 'application/json'
                  }
                });
              case 6:
                response = _context.sent;
                _context.next = 9;
                return response.json();
              case 9:
                result = _context.sent;
                if (response.ok) {
                  feedbackEl.innerHTML = "\n            <div class=\"alert alert-success\">\n              Your message has been sent successfully.\n            </div>";
                  form.reset();
                } else {
                  feedbackEl.innerHTML = "\n            <div class=\"alert alert-danger\">\n              ".concat(result.error || 'Something went wrong', "\n            </div>");
                }
                _context.next = 16;
                break;
              case 13:
                _context.prev = 13;
                _context.t0 = _context["catch"](3);
                feedbackEl.innerHTML = "\n          <div class=\"alert alert-danger\">\n            Network error. Please try again.\n          </div>";
              case 16:
                _context.prev = 16;
                setTimeout(function () {
                  feedbackEl.innerHTML = null;
                }, 3000);
                return _context.finish(16);
              case 19:
              case "end":
                return _context.stop();
            }
          }, _callee, null, [[3, 13, 16, 19]]);
        }));
        return function (_x) {
          return _ref.apply(this, arguments);
        };
      }());
    });
  }
};

/*-----------------------------------------------
|   Gooogle Map
-----------------------------------------------*/

function destroyMap(map) {
  if (map) {
    window.google.maps.event.clearInstanceListeners(map);
  }
}
function initMap() {
  var themeController = document.body;
  var $googlemaps = document.querySelectorAll('[data-gmap]');
  if ($googlemaps.length && window.google) {
    $googlemaps.forEach( /*#__PURE__*/function () {
      var _ref2 = _asyncToGenerator( /*#__PURE__*/_regeneratorRuntime().mark(function _callee2(itm) {
        var _yield$window$google$, Map, InfoWindow, _yield$window$google$2, AdvancedMarkerElement, _yield$window$google$3, ColorScheme, latLng, markerPopup, zoom, mapElement, mapId, lightIconUrl, darkIconUrl, pov, _mapOptions, mapOptions, map, infowindow, iconImage, marker;
        return _regeneratorRuntime().wrap(function _callee2$(_context2) {
          while (1) switch (_context2.prev = _context2.next) {
            case 0:
              _context2.next = 2;
              return window.google.maps.importLibrary('maps');
            case 2:
              _yield$window$google$ = _context2.sent;
              Map = _yield$window$google$.Map;
              InfoWindow = _yield$window$google$.InfoWindow;
              _context2.next = 7;
              return window.google.maps.importLibrary('marker');
            case 7:
              _yield$window$google$2 = _context2.sent;
              AdvancedMarkerElement = _yield$window$google$2.AdvancedMarkerElement;
              _context2.next = 11;
              return window.google.maps.importLibrary('core');
            case 11:
              _yield$window$google$3 = _context2.sent;
              ColorScheme = _yield$window$google$3.ColorScheme;
              latLng = utils.getData(itm, 'latlng').split(',');
              markerPopup = itm.innerHTML;
              zoom = utils.getData(itm, 'zoom');
              mapElement = itm;
              mapId = utils.getData(itm, 'mapid');
              lightIconUrl = utils.getData(itm, 'icon') ? utils.getData(itm, 'icon') : 'https://maps.gstatic.com/mapfiles/api-3/images/spotlight-poi.png';
              darkIconUrl = utils.getData(itm, 'dark-icon') ? utils.getData(itm, 'dark-icon') : lightIconUrl;
              if (!(utils.getData(itm, 'theme') === 'streetview')) {
                _context2.next = 24;
                break;
              }
              pov = utils.getData(itm, 'pov');
              _mapOptions = {
                position: {
                  lat: Number(latLng[0]),
                  lng: Number(latLng[1])
                },
                pov: pov,
                zoom: zoom,
                gestureHandling: 'none',
                scrollwheel: false,
                linksControl: true,
                panControl: true,
                motionTracking: false,
                visible: true
              };
              return _context2.abrupt("return", new window.google.maps.StreetViewPanorama(mapElement, _mapOptions));
            case 24:
              mapOptions = {
                mapId: mapId,
                zoom: zoom,
                scrollwheel: utils.getData(itm, 'scrollwheel'),
                center: {
                  lat: Number(latLng[0]),
                  lng: Number(latLng[1])
                },
                colorSchema: ColorScheme.LIGHT
              };
              map = new Map(mapElement, mapOptions);
              infowindow = new InfoWindow({
                content: markerPopup
              });
              iconImage = document.createElement('img');
              iconImage.src = localStorage.getItem('theme') === 'dark' ? darkIconUrl : lightIconUrl;
              marker = new AdvancedMarkerElement({
                position: {
                  lat: Number(latLng[0]),
                  lng: Number(latLng[1])
                },
                content: iconImage,
                map: map
              });
              marker.addListener('click', function () {
                infowindow.open(map, marker);
              });
              themeController && themeController.addEventListener('clickControl', function (_ref3) {
                var control = _ref3.detail.control;
                if (control === 'theme') {
                  destroyMap(map);
                  initMap();
                }
              });
              return _context2.abrupt("return", null);
            case 33:
            case "end":
              return _context2.stop();
          }
        }, _callee2);
      }));
      return function (_x2) {
        return _ref2.apply(this, arguments);
      };
    }());
  }
}

/* -------------------------------------------------------------------------- */
/*                               Hamburger icon                               */
/* -------------------------------------------------------------------------- */

var hamburgerInit = function hamburgerInit() {
  var hamburgerButton = document.querySelectorAll('[data-hamburger-icon]');
  if (hamburgerButton.length) {
    hamburgerButton.forEach(function (hamburger) {
      var hamburgerIcon = hamburger.querySelector('.hamburger');
      hamburger.addEventListener('click', function () {
        hamburgerIcon.classList.toggle('is-active');
        if (hamburgerIcon.classList.contains('is-active')) {
          var computedStyle = window.getComputedStyle(hamburgerIcon);
          if (computedStyle.animationName !== 'none') {
            var clone = hamburger.cloneNode(true);
            hamburger.parentNode.replaceChild(clone, hamburger);
          }
        }
      });
    });
  }
};

/* -------------------------------------------------------------------------- */
/*                                  Inertia                                   */
/* -------------------------------------------------------------------------- */

var inertiaInit = function inertiaInit() {
  var inertia = function inertia(element, controller) {
    var offset = element.getBoundingClientRect().top + window.scrollY;
    var winHeight = window.innerHeight;
    var currentPosition = window.scrollY;
    var previousPosition = 0;
    var y = 0;
    if (!controller) {
      controller = {};
    }
    if (!controller.weight) {
      controller.weight = 2;
    }
    if (!controller.duration) {
      controller.duration = 0.7;
    }
    if (!controller.ease) {
      controller.ease = 'Power3.easeOut';
    }

    // eslint-disable-next-line no-mixed-operators
    element.style.transform = "translateY(".concat((offset - window.screenY) * 100 / winHeight, "px)");
    function onScrollOrResize() {
      currentPosition = window.scrollY;
      // eslint-disable-next-line no-mixed-operators
      y = controller.weight * (offset - currentPosition) * 100 / winHeight;
      if (currentPosition !== previousPosition) {
        window.TweenMax.to(element, controller.duration, {
          y: y,
          ease: controller.ease
        });
      }
      previousPosition = currentPosition;
    }
    window.addEventListener('resize', onScrollOrResize);
    window.addEventListener('scroll', onScrollOrResize);
  };
  var inertiaElement = document.querySelectorAll('[data-inertia]');
  inertiaElement.forEach(function (elem) {
    var options = utils.getData(elem, 'inertia');
    inertia(elem, options || undefined);
  });
};

/* -------------------------------------------------------------------------- */
/*                                 bigPicture                                 */
/* -------------------------------------------------------------------------- */

var lightboxInit = function lightboxInit() {
  if (window.BigPicture) {
    var bpItems = document.querySelectorAll('[data-bigpicture]');
    bpItems.forEach(function (bpItem) {
      var userOptions = utils.getData(bpItem, 'bigpicture');
      var defaultOptions = {
        el: bpItem
      };
      var options = window._.merge(defaultOptions, userOptions);
      bpItem.addEventListener('click', function () {
        window.BigPicture(options);
      });
    });
  }
};

/* -------------------------------------------------------------------------- */
/*                               Video Modal                                  */
/* -------------------------------------------------------------------------- */

var parallaxInit = function parallaxInit() {
  var parallax = document.querySelectorAll('[data-parallax]');
  if (parallax.length && window.Rellax) {
    parallax.forEach(function (item) {
      var options = utils.getData(item, 'rellax');
      var centered = utils.getData(item, 'center');
      // eslint-disable-next-line no-new
      new window.Rellax(item, _objectSpread(_objectSpread({}, options), {}, {
        center: centered
      }));
    });
  }
};

/* -------------------------------------------------------------------------- */
/*                                  Preloader                                 */
/* -------------------------------------------------------------------------- */

var preloaderInit = function preloaderInit() {
  var bodyElement = document.querySelector('body');
  window.imagesLoaded(bodyElement, function () {
    var preloader = document.querySelector('#preloader');
    preloader === null || preloader === void 0 || preloader.classList.add('loaded');
    setTimeout(function () {
      preloader === null || preloader === void 0 || preloader.remove();
    }, 800);
  });
};

/* -------------------------------------------------------------------------- */
/*                                 Scrollbars                                 */
/* -------------------------------------------------------------------------- */

var scrollInit = function scrollInit() {
  var dropdownElements = Array.from(document.querySelectorAll('[data-hide-on-body-scroll]'));
  if (window.innerWidth < 1200) {
    window.addEventListener('scroll', function () {
      dropdownElements.forEach(function (dropdownElement) {
        var instanceEl = window.bootstrap.Dropdown.getInstance(dropdownElement);
        instanceEl && instanceEl.hide();
      });
    });
  }
};

/*-----------------------------------------------
|  Swiper
-----------------------------------------------*/
var swiperInit = function swiperInit() {
  var themeContainers = document.querySelectorAll('[data-swiper-theme-container]');
  themeContainers.forEach(function (themeContainer) {
    var swiper = themeContainer.querySelector('[data-swiper]');
    var options = utils.getData(swiper, 'swiper');
    var thumbsOptions = options.thumb;
    var thumbsInit;
    if (thumbsOptions) {
      var thumbImages = swiper.querySelectorAll('img');
      var slides = '';
      thumbImages.forEach(function (img) {
        slides += "\n          <div class='swiper-slide'\">\n            <img class='img-fluid mt-1' src=".concat(img.src, " alt=''/>\n          </div>\n        ");
      });
      var thumbs = document.createElement('div');
      thumbs.setAttribute('class', 'swiper thumb');
      thumbs.innerHTML = "<div class='swiper-wrapper overflow-hidden'>".concat(slides, "</div>");
      if (thumbsOptions.parent) {
        var parent = document.querySelector(thumbsOptions.parent);
        parent.parentNode.appendChild(thumbs);
      } else {
        swiper.parentNode.appendChild(thumbs);
      }
      thumbsInit = new window.Swiper(thumbs, thumbsOptions);
    }
    var swiperNav = themeContainer.querySelector('.swiper-nav');
    // eslint-disable-next-line no-new
    var newSwiper = new window.Swiper(swiper, _objectSpread(_objectSpread({}, options), {}, {
      navigation: {
        nextEl: swiperNav === null || swiperNav === void 0 ? void 0 : swiperNav.querySelector('.swiper-button-next'),
        prevEl: swiperNav === null || swiperNav === void 0 ? void 0 : swiperNav.querySelector('.swiper-button-prev'),
        addIcons: false
      },
      pagination: {
        el: themeContainer === null || themeContainer === void 0 ? void 0 : themeContainer.querySelector('.swiper-pagination'),
        clickable: true
      },
      thumbs: {
        swiper: thumbsInit
      }
    }));
    if (swiper) {
      newSwiper.on('slideChange', function () {
        var timelineElements = swiper.querySelectorAll('[data-zanim-timeline]');
        timelineElements.forEach(function (el) {
          window.zanimation(el, function (animation) {
            setTimeout(function () {
              animation.play();
            }, 800);
          });
        });
      });
    }
  });
};

/*-----------------------------------------------
|                 Zanimation
-----------------------------------------------*/

/*
global CustomEase, gsap
*/
CustomEase.create('CubicBezier', '.77,0,.18,1');

/*-----------------------------------------------
|   Global Functions
-----------------------------------------------*/
var filterBlur = function filterBlur() {
  var blur = 'blur(5px)';
  var isIpadIphoneMacFirefox = (window.is.ios() || window.is.mac()) && window.is.firefox();
  if (isIpadIphoneMacFirefox) {
    blur = 'blur(0px)';
  }
  return blur;
};
var zanimationEffects = {
  "default": {
    from: {
      opacity: 0,
      y: 70
    },
    to: {
      opacity: 1,
      y: 0
    },
    ease: 'CubicBezier',
    duration: 0.8,
    delay: 0
  },
  'slide-down': {
    from: {
      opacity: 0,
      y: -70
    },
    to: {
      opacity: 1,
      y: 0
    },
    ease: 'CubicBezier',
    duration: 0.8,
    delay: 0
  },
  'slide-left': {
    from: {
      opacity: 0,
      x: 70
    },
    to: {
      opacity: 1,
      x: 0
    },
    ease: 'CubicBezier',
    duration: 0.8,
    delay: 0
  },
  'slide-right': {
    from: {
      opacity: 0,
      x: -70
    },
    to: {
      opacity: 1,
      x: 0
    },
    ease: 'CubicBezier',
    duration: 0.8,
    delay: 0
  },
  'zoom-in': {
    from: {
      scale: 0.9,
      opacity: 0,
      filter: filterBlur()
    },
    to: {
      scale: 1,
      opacity: 1,
      filter: 'blur(0px)'
    },
    delay: 0,
    ease: 'CubicBezier',
    duration: 0.8
  },
  'zoom-out': {
    from: {
      scale: 1.1,
      opacity: 1,
      filter: filterBlur()
    },
    to: {
      scale: 1,
      opacity: 1,
      filter: 'blur(0px)'
    },
    delay: 0,
    ease: 'CubicBezier',
    duration: 0.8
  },
  'zoom-out-slide-right': {
    from: {
      scale: 1.1,
      opacity: 1,
      x: -70,
      filter: filterBlur()
    },
    to: {
      scale: 1,
      opacity: 1,
      x: 0,
      filter: 'blur(0px)'
    },
    delay: 0,
    ease: 'CubicBezier',
    duration: 0.8
  },
  'zoom-out-slide-left': {
    from: {
      scale: 1.1,
      opacity: 1,
      x: 70,
      filter: filterBlur()
    },
    to: {
      scale: 1,
      opacity: 1,
      x: 0,
      filter: 'blur(0px)'
    },
    delay: 0,
    ease: 'CubicBezier',
    duration: 0.8
  },
  'blur-in': {
    from: {
      opacity: 0,
      filter: filterBlur()
    },
    to: {
      opacity: 1,
      filter: 'blur(0px)'
    },
    delay: 0,
    ease: 'CubicBezier',
    duration: 0.8
  }
};
if (utils.isRTL()) {
  Object.keys(zanimationEffects).forEach(function (key) {
    if (zanimationEffects[key].from.x) {
      zanimationEffects[key].from.x = -zanimationEffects[key].from.x;
    }
  });
}
var zanimation = function zanimation(el, callback) {
  var Selector = {
    DATA_ZANIM_TIMELINE: '[data-zanim-timeline]',
    DATA_KEYS: '[data-zanim-xs], [data-zanim-sm], [data-zanim-md],[data-zanim-lg], [data-zanim-xl]'
  };
  var DATA_KEY = {
    DATA_ZANIM_TRIGGER: 'data-zanim-trigger'
  };

  /*-----------------------------------------------
  |   Get Controller
  -----------------------------------------------*/
  var controllerZanim;
  var currentBreakpointName = utils.getCurrentScreenBreakpoint().currentBreakpoint;
  var currentBreakpointVal = utils.getCurrentScreenBreakpoint().breakpointStartVal;
  var getController = function getController(element) {
    var options = {};
    var controller = {};
    if (element.hasAttribute("data-zanim-".concat(currentBreakpointName))) {
      controllerZanim = "zanim-".concat(currentBreakpointName);
    } else {
      /*-----------------------------------------------
      |   Set the mobile first Animation
      -----------------------------------------------*/
      var animationBreakpoints = [];
      var attributes = element.getAttributeNames();
      attributes.forEach(function (attribute) {
        if (attribute !== DATA_KEY.DATA_ZANIM_TRIGGER && attribute.startsWith('data-zanim-')) {
          var breakPointName = attribute.split('data-zanim-')[1];
          if (utils.breakpoints[breakPointName] < currentBreakpointVal) {
            animationBreakpoints.push({
              name: breakPointName,
              size: utils.breakpoints[breakPointName]
            });
          }
        }
      });
      controllerZanim = undefined;
      if (animationBreakpoints.length !== 0) {
        animationBreakpoints = animationBreakpoints.sort(function (a, b) {
          return a.size - b.size;
        });
        var activeBreakpoint = animationBreakpoints.pop();
        controllerZanim = "zanim-".concat(activeBreakpoint.name);
      }
    }
    var userOptions = utils.getData(element, controllerZanim);
    controller = window._.merge(options, userOptions);
    if (!(controllerZanim === undefined)) {
      if (userOptions.animation) {
        options = zanimationEffects[userOptions.animation];
      } else {
        options = zanimationEffects["default"];
      }
    }
    if (controllerZanim === undefined) {
      options = {
        delay: 0,
        duration: 0,
        ease: 'Expo.easeOut',
        from: {},
        to: {}
      };
    }

    /*-----------------------------------------------
    |   populating the controller
    -----------------------------------------------*/
    controller.delay || (controller.delay = options.delay);
    controller.duration || (controller.duration = options.duration);
    controller.from || (controller.from = options.from);
    controller.to || (controller.to = options.to);
    if (controller.ease) {
      controller.to.ease = controller.ease;
    } else {
      controller.to.ease = options.ease;
    }
    return controller;
  };
  /*-----------------------------------------------
  |   End of Get Controller
  -----------------------------------------------*/

  /*-----------------------------------------------
  |   For Timeline
  -----------------------------------------------*/

  var zanimTimeline = el.hasAttribute('data-zanim-timeline');
  if (zanimTimeline) {
    var timelineOption = utils.getData(el, 'zanim-timeline');
    var timeline = gsap.timeline(timelineOption);
    var timelineElements = el.querySelectorAll(Selector.DATA_KEYS);
    timelineElements.forEach(function (timelineEl) {
      var controller = getController(timelineEl);
      timeline.fromTo(timelineEl, controller.duration, controller.from, controller.to, controller.delay).pause();
      window.imagesLoaded(timelineEl, callback(timeline));
    });
  } else if (!el.closest(Selector.DATA_ZANIM_TIMELINE)) {
    /*-----------------------------------------------
    |   For single elements outside timeline
    -----------------------------------------------*/
    var controller = getController(el);
    callback(gsap.fromTo(el, controller.duration, controller.from, controller.to).delay(controller.delay).pause());
  }
  callback(gsap.timeline());
};

/*-----------------------------------------------
|    Zanimation Init
-----------------------------------------------*/

var zanimationInit = function zanimationInit() {
  var Selector = {
    DATA_ZANIM_TRIGGER: '[data-zanim-trigger]',
    DATA_ZANIM_REPEAT: '[zanim-repeat]'
  };
  var DATA_KEY = {
    DATA_ZANIM_TRIGGER: 'data-zanim-trigger'
  };
  var Events = {
    SCROLL: 'scroll'
  };

  /*-----------------------------------------------
  |   Triggering zanimation when the element enters in the view
  -----------------------------------------------*/
  var triggerZanimation = function triggerZanimation() {
    var triggerElement = document.querySelectorAll(Selector.DATA_ZANIM_TRIGGER);
    triggerElement.forEach(function (el) {
      if (utils.isElementIntoView(el) && el.hasAttribute(DATA_KEY.DATA_ZANIM_TRIGGER)) {
        zanimation(el, function (animation) {
          return animation.play();
        });
        if (!document.querySelector(Selector.DATA_ZANIM_REPEAT)) {
          el.removeAttribute(DATA_KEY.DATA_ZANIM_TRIGGER);
        }
      }
    });
  };
  triggerZanimation();
  window.addEventListener(Events.SCROLL, function () {
    triggerZanimation();
  });
};
var gsapAnimation = {
  zanimationInit: zanimationInit,
  zanimation: zanimation
};

/* -------------------------------------------------------------------------- */
/*                            Theme Initialization                            */
/* -------------------------------------------------------------------------- */
docReady(detectorInit);
docReady(dropdownOnHover);
docReady(dropdownMenuInit);
docReady(scrollInit);
docReady(initMap);
docReady(parallaxInit);
docReady(swiperInit);
docReady(lightboxInit);
docReady(bgPlayerInit);
docReady(zanimationInit);
docReady(hamburgerInit);
docReady(formInit);
docReady(preloaderInit);
docReady(inertiaInit);
//# sourceMappingURL=theme.js.map
