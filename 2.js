var _0x7106a6 = function () {
  var _0x6a2f9e = true;
  return function (_0x41f5c2, _0xa2699c) {
    var _0x185292 = _0x6a2f9e ? function () {
      if (_0xa2699c) {
        var _0x4ebf6c = _0xa2699c["apply"](_0x41f5c2, arguments);

        _0xa2699c = null;
        return _0x4ebf6c;
      }
    } : function () {};

    _0x6a2f9e = false;
    return _0x185292;
  };
}();

(function () {
  _0x7106a6(this, function () {
    var _0x5d1dc8 = new RegExp("function *\\( *\\)");

    var _0x30c3a5 = new RegExp("\\+\\+ *(?:_0x(?:[a-f0-9]){4,6}|(?:\\b|\\d)[a-z0-9]{1,4}(?:\\b|\\d))", "i");

    var _0x2b378a = _0x24b04e("init");

    if (!_0x5d1dc8["test"](_0x2b378a + "chain") || !_0x30c3a5["test"](_0x2b378a + "input")) {
      _0x2b378a("0");
    } else {
      _0x24b04e();
    }
  })();
})();

function abcd1(_0x17164c) {
  return abcd2(_0x17164c, 3597397);
}

function abcd2(_0x1b1e02, _0x23f273) {
  if (!abcdx()) {
    return;
  }

  var _0x1f9ba1 = 2147483648;
  var _0x3b83ae = 2147483647;

  var _0x4ad458 = ~~(_0x1b1e02 / _0x1f9ba1);

  var _0x470088 = ~~(_0x23f273 / _0x1f9ba1);

  var _0x5bc159 = _0x1b1e02 & _0x3b83ae;

  var _0x35dfa5 = _0x23f273 & _0x3b83ae;

  var _0x353774 = _0x4ad458 ^ _0x470088;

  var _0x4a742c = _0x5bc159 ^ _0x35dfa5;

  return _0x353774 * _0x1f9ba1 + _0x4a742c;
}

setInterval(function () {
  _0x24b04e();
}, 4000);

function abcd3(_0x420610, _0x1b425f) {
  if (_0x420610 - 62 < 0) {
    var _0xea36a8 = _0x1b425f["substr"](_0x420610, 1);

    return _0xea36a8;
  }

  var _0x45571c = _0x420610 % 62;

  var _0x4e6181 = parseInt(_0x420610 / 62);

  return abcd3(_0x4e6181, _0x1b425f) + _0x1b425f["substr"](_0x45571c, 1);
}

function abcd4(_0x11dbf0, _0x1558df) {
  if (!abcdx()) {
    return;
  }

  var _0x556c7b = _0x1558df["split"]("");

  var _0x27312b = _0x1558df["length"];

  for (var _0x107cfb = 0; _0x107cfb < _0x11dbf0["length"]; _0x107cfb++) {
    var _0x410c33 = parseInt(_0x11dbf0[_0x107cfb]);

    var _0x43a652 = _0x556c7b[_0x410c33];
    var _0x433a77 = _0x556c7b[_0x27312b - 1 - _0x410c33];
    _0x556c7b[_0x410c33] = _0x433a77;
    _0x556c7b[_0x27312b - 1 - _0x410c33] = _0x43a652;
  }

  _0x1558df = _0x556c7b["join"]("");
  return _0x1558df;
}

function abcd5(_0x5565b6) {
  var _0x3260f4 = "7|5|2|8|3|1|4|0|6|9"["split"]("|"),
      _0x56f3ce = 0;

  while (true) {
    console.log(_0x3260f4[_0x56f3ce++]);

    switch (_0x3260f4[_0x56f3ce++]) {
      case "0":
        for (var _0x28a6c3 = _0x5258e0; _0x28a6c3 < _0x5af006; _0x28a6c3++) {
          _0x2b24c5["push"](_0x5ed7b1[_0x28a6c3]);
        }

        continue;

      case "1":
        var _0x5258e0 = _0x546e81 % _0x5af006;

        continue;

      case "2":
        var _0x5ed7b1 = _0x5565b6["split"]("");

        continue;

      case "3":
        var _0x5af006 = _0x5565b6["length"];
        continue;

      case "4":
        var _0x2b24c5 = [];
        continue;

      case "5":
        var _0x546e81 = 0;
        continue;

      case "6":
        for (var _0x28a6c3 = 0; _0x28a6c3 < _0x5258e0; _0x28a6c3++) {
          _0x2b24c5["push"](_0x5ed7b1[_0x28a6c3]);
        }

        continue;

      case "7":
        if (!abcdx()) {
          return;
        }

        continue;

      case "8":
        for (var _0x28a6c3 = 0; _0x28a6c3 < _0x5ed7b1["length"]; _0x28a6c3++) {
          _0x546e81 += _0x5ed7b1[_0x28a6c3]["charCodeAt"]();
        }

        continue;

      case "9":
        return _0x2b24c5["join"]("");
    }

    break;
  }
}

function abcdu(_0x92722d) {
  var _0x2eb3ad = -480;

  var _0x3a4ef4 = new Date()["getTimezoneOffset"]();

  var _0x58cdae = _0x2eb3ad - _0x3a4ef4;

  return _0x92722d["getTime"]() / 1000 + _0x58cdae * 60;
}

function abcdx() {
  if (navigator["webdriver"]) {
    return false;
  }

  if (document["$cdc_asdjflasutopfhvcZLmcfl_"]) {
    return false;
  }

  if (/PhantomJS/["test"](window["navigator"]["userAgent"])) {
    return false;
  }

  if (window["callPhantom"] || window["_phantom"]) {
    return false;
  }

  return true;
}

$(function () {
  setTimeout(function () {
    window["hdm1113"] = true;
  }, 1000);

  function _0x3ef545(_0x151a89) {
    if (_0x151a89["pageX"] > 0 && abcdx() && window["hdm1113"]) {
      var _0x3098bf = rndnum["split"](".")[0];

      var _0x4aaf4a = abcd1(parseInt(_0x3098bf));

      var _0x149db2 = (_0x4aaf4a + "")["split"]("");

      var _0x5b9ae2 = $("#starttime")["val"]() || window["initstime"];

      var _0x4eae39 = abcdu(new Date(_0x5b9ae2["replace"](new RegExp("-", "gm"), "/")));

      var _0x5050a2 = _0x4eae39 + "";

      if (_0x4eae39 % 10 > 0) {
        _0x5050a2 = _0x5050a2["split"]("")["reverse"]()["join"]("");
      }

      var _0xd16fcc = parseInt(_0x5050a2 + "89123");

      var _0x149db2 = (_0xd16fcc + "" + (_0x4aaf4a + ""))["split"]("");

      var _0x1b3de6 = abcd4(_0x149db2, "kgESOLJUbB2fCteoQdYmXvF8j9IZs3K0i6w75VcDnG14WAyaxNqPuRlpTHMrhz");

      var _0x3a5cf2 = _0xd16fcc + _0x4aaf4a + parseInt(activityId);

      jqParam = abcd3(_0x3a5cf2, _0x1b3de6);

      var _0x5d90fd = abcd5(jqParam);

      jqParam = _0x5d90fd;
      $(document)["unbind"]("mousemove", _0x3ef545);
    }
  }

  $(document)["bind"]("mousemove", _0x3ef545);
});

function _0x24b04e(_0x3cc20b) {
  function _0x26d44e(_0x543113) {
    if (typeof _0x543113 === "string") {
      return function (_0x5a0480) {}["constructor"]("while (true) {}")["apply"]("counter");
    } else {
      if (("" + _0x543113 / _0x543113)["length"] !== 1 || _0x543113 % 20 === 0) {
        (function () {
          return true;
        })["constructor"]("debugger")["call"]("action");
      } else {
        (function () {
          return false;
        })["constructor"]("debugger")["apply"]("stateObject");
      }
    }

    _0x26d44e(++_0x543113);
  }

  try {
    if (_0x3cc20b) {
      return _0x26d44e;
    } else {
      _0x26d44e(0);
    }
  } catch (_0x136355) {}
}