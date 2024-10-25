console.log("App.js is running");

var app = {
    title: "React App",
    subtitle: "Put your life in the hands of a computer"
};

// JSX - JavaScript with XML
var template = (
    <div>
        <h1>{app.title}</h1>
        {app.subtitle && <p>{app.subtitle}</p>}
        <ol>
            <li>Item one</li>
            <li>Item two</li>
            <li>Item three</li>
            <li>Item four</li>
        </ol>
    </div>
);

// mutable variable
var user = {
    name: "Andrew",
    age: 26,
    eligible: "no",
    location: "Philadelphia"
};

// immutable constant (cannot be re-defined)
let user2 = {
    name: "Lucy",
    age: 13,
    eligible: "yes"
};

// immutable constant that (cannot be re-defined nor re-assigned)
const user3 = {
    name: "Joe",
    age: 13,
    eligible: "yes"
};


// Conditional render: only render the Location if location is provided
function getLocation(location) {
    if (location) {
        return <p>Location: {location}</p>;
    }
}
var templateTwo = (
    <div>
        <h1>{user.name ? user.name : "Anonymous"}</h1>
        {/* Conditional render */}
        {(user.age && user.age >= 18) && <p>Age: {user.age}</p>}
        {(user.eligible && user.eligible == "yes") && <p>Eligible: {user.eligible}</p>}
        {getLocation(user.location)}
        <h1>{user2.name ? user2.name : "Anonymous"}</h1>
        {(user2.age && user2.age >= 18) && <p>Age: {user2.age}</p>}
        {(user2.eligible && user2.eligible == "yes") && <p>Eligible: {user2.eligible}</p>}
        {getLocation(user2.location)}
    </div>
);

var appRoot = document.getElementById("app");

ReactDOM.render(templateTwo, appRoot);
