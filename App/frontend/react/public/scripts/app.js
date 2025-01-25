(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
"use strict";

console.log("App.js is running");
var app = {
  title: "React App",
  subtitle: "Put your life in the hands of a computer"
};

// JSX - JavaScript with XML
var template = /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h1", null, app.title), app.subtitle && /*#__PURE__*/React.createElement("p", null, app.subtitle), /*#__PURE__*/React.createElement("ol", null, /*#__PURE__*/React.createElement("li", null, "Item one"), /*#__PURE__*/React.createElement("li", null, "Item two"), /*#__PURE__*/React.createElement("li", null, "Item three"), /*#__PURE__*/React.createElement("li", null, "Item four")));

// mutable variable
var user = {
  name: "Andrew",
  age: 26,
  eligible: "no",
  location: "Philadelphia"
};

// immutable constant (cannot be re-defined)
var user2 = {
  name: "Lucy",
  age: 13,
  eligible: "yes"
};

// immutable constant that (cannot be re-defined nor re-assigned)
var user3 = {
  name: "Joe",
  age: 13,
  eligible: "yes"
};

// Conditional render: only render the Location if location is provided
function getLocation(location) {
  if (location) {
    return /*#__PURE__*/React.createElement("p", null, "Location: ", location);
  }
}
var templateTwo = /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h1", null, user.name ? user.name : "Anonymous"), user.age && user.age >= 18 && /*#__PURE__*/React.createElement("p", null, "Age: ", user.age), user.eligible && user.eligible == "yes" && /*#__PURE__*/React.createElement("p", null, "Eligible: ", user.eligible), getLocation(user.location), /*#__PURE__*/React.createElement("h1", null, user2.name ? user2.name : "Anonymous"), user2.age && user2.age >= 18 && /*#__PURE__*/React.createElement("p", null, "Age: ", user2.age), user2.eligible && user2.eligible == "yes" && /*#__PURE__*/React.createElement("p", null, "Eligible: ", user2.eligible), getLocation(user2.location));
var appRoot = document.getElementById("app");
ReactDOM.render(templateTwo, appRoot);

},{}]},{},[1]);
