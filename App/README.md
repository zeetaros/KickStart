## Quick Start
Installing dependencies:
```sh
npm install
```

Start development server:
```sh
npm run dev
```

While on project root:
```sh
live-server public
```


## Developer Notes
### Folder structure
- `public/index.html`: HTML template. Points to `public/scripts/app.js`.
- `public/scripts/app.js`: auto-translated code by `babel` compiled from `src/app.js`. No manual edit.
- `src/app.js`: source code in JSX format. Editable.

To do a one-off translate using `babel`:
```sh
babel src/app.js --out-file public/scripts/app.js
```

To setup the auto-translation and with preset babel modules, add the `--watch` & `--presets` flags:
```sh
babel src/app.js --out-file public/scripts/app.js --presets=@babel/preset-env,@babel/preset-react --watch
```

### Local per-project packages
Generally avoid installing node packages globally i.e. `npm install -g`. Package versions should be per-project. The detail of required packages is stored in `package.json` or `yarn.lock` on the project level.  

### Use of `package.json`
This file can contain information about the project, project dependencies, and some custom scripts.
Since node packages are installed locally per-project, it might not be added to the Path, meaning that some CLI commands might not be recognisable. To run commands installed on project level, one trick is to define the commands in `package.json`. e.g.

```js
"scripts": {
    "babel-version": "babel --version",
    "babel-sync": "babel src/app.js --out-file public/scripts/app.js --presets=@babel/preset-env,@babel/preset-react"
  }
```
Then these commands will be callable in terminal while in the project directory. 
```sh
npm run babel-version
npm run babel-sync
```

## React
Core concepts:
- Components
- Props
- Events
- State

### Components
A component in React is simply a function that return renderable content - typically JSX code. The JSX code leads to a tree-like code structure that informs React how different componsnents are related and how the UI should look like. It then executes appropriate commands to manipulate the real DOM to reflect that target structure.  
To use custom components, their name must be capitalised. That's how React tells them apart from built-in HTML elements.  

**N.B.** By default, React components execute **Only Once**. It is executed when the components are encountered at the first time when the App is loaded. The components have to be informed if it should be executed again.

### Props
Props are the way to pass data to components. There are two ways to pass props:
1. Pass props using **attributes**. This approach is for *multiple smaller pieces of information* that must be passed to a component.  
    a. Pass props as attributes.
    ```js
    <Component name="John" age="30" />
    ```  
    b. Pass props as attribute (with an object). Only if the attributes are namded the same in components (the function definition).
    ```js
    const user = {
      name: "John",
      age: 30
    }
      <Component {...user} />
      // the Component function must be using props.name and props.age
    ```
    On component definition side:  
    ```js
    function  Component({user}) {
      return (
        <li>
            <p>{user.name}</p>
            <p>{user.age}</p>
        </li>
      )
    }
    ```  

2. Pass props using **children**. This takes a *single piece of renderable content*, this approach is closer to "normal HTML usage". It is conventient when passing JSX code as a value to another component.
    ```js
    <Component>"John"</Component>
    ```
   On component definition side:
    ```js
    function  Component({children}) {
      return (
        <li>
            <p>{children}</p>
        </li>
      )
    }
    ```
    The "children" prop will receive whichever content passed between the opening and closing tags of the component.  


### Events : `onXYZ`
To handle events (e.g. mouse clicking), the built-in `onXYZ` props (e.g. `onClick`, `onSelect`) allow defining functions that should be triggered when the specified event occurs. This is handled by React and is different from vanilla JavaScript where developers use `addEventListener()` (e.g. `addEventListener('click')`).  
  
To execute code upon events, a pointer to the function that should be executed must be passed to the event props like `onClick`:
```js
function handleClick() {
  return ()
}
<Component onClick={handleClick} />
// pass only {handleClick} and let React take care of execution but not explicitly calling the function i.e. {handleClick()}
```
  
Event-dependent function can also accept arguments by wrapping the function with another function:
```js
function handleClick(integer) {
  return ();
};
<Component onClick={() => handleClick(5)} />
```

**Creating annoymous event handling functions**  
Two syntax styles:
```js
// Event function
function selectHandler() {
    console.log("Event triggered");
};
// (1)
<TabButton onSelect={() => selectHandler()}>some_labels</TabButton>
// (2)
<TabButton onSelect={function() {selectHandler}}>some_labels</TabButton>
```

### States : `useXYZ`
Functions with format `useXYZ` are React hooks used to handle states. 
```js
import { useState } from 'react';
// Or
import React from 'react';
React.useState();
```
They can only be called either:
- inside a React Component directly on the top level;
- inside another React Hook.

It cannot be called:
- inside a nested inner function inside a React Component (even inside a if-statements);

```js
// Valid use cases:
// Example A1
function App() {
  useState();

  function inner() {
    // useState() cannot be used here
  }
}

// Example A2
function App() {
  const [val, setVal] = useState(0);
}

// Invalid use cases:
// Example B1
const [val, setVal] = useState(0);
function App() { ... }

// Example B2
function App() {
  if (someCondition)
    const [val, setVal] = useState(0);
}
```
<br>

`useState()` yields an array with exactly two elements. It can be used as
```js
const stateArray = useState("Please click a button");
// or use array destructuring
const [selectedTopic, setSelectedTopic] = useState("Please click a button");
```
Here the first element -- e.g. `selectedTopic`, is the current state value provided by React. It may change if the component function executed again. The string `"Please click a button"` is the defined initial state value stored by React. It can also store an integer e.g. `useState(0)`.   

The seconde element -- e.g. `setSelectedTopic`, will **always be a function**. It is called the "state updating function" that updates the stored value and informs React to re-execute the component function in which `useState()` was called.  

N.B. upon calling the state updating function `setSelectedTopic` execute **two things**:
1. re-execute the component in which the React Hook is used e.g. `App()`.
2. update the value of `selectedTopic`;

```js
function App() {  // 1. re-executing this component
  // 2. updating the selectedTopic constant
  const [selectedTopic, setSelectedTopic] = useState("Please click a button");
  console.log(selectedTopic);
}
```
The order of execution matters. The value in `selectedTopic` is **not updated until** the `App()` component is executed; because the new version of the constant only gets created when the component is re-run. Hence, in this above example, the log will show the old value right after calling `setSelectedTopic`.    


**Why use `const` here?**
* Because `selectedTopic` should be re-created everytime when the component function is executed. It shouldn't be a variable but a constant.  

The state updating function `setSelectedTopic` can be explicitly called within the React Component including within an inner function, e.g.
```js
function App() {
  const [selectedTopic, setSelectedTopic] = useState("Please click a button");
  function handleSelect(selectedButton) {
    setSelectedTopic(selectedButton);
  }
  return (
    <p>{selectedTopic}</p>
  )
}
```
Putting button event `onClick` and React Hook together:
```js
// Write a button to apply discount upon click e.g. $100 -> $75
function App() {
  const [price, setPrice] = useState(100);

  function handleClick(newPrice) {
    setPrice(newPrice);
  }

  return (
    <div>
      <p data-testid="price">{price}</p>
      <button onClick={() => handleClick(75)}>Apply Discount</button>
    </div>
  );
}
```

<br>

### Images
Image files loaded by 
```html
<img src="./asset/001.png" alt="imageAlt" />
```
might be ignored by the bundling process during build. Hence, a better way to load images is
```js
import reactImg from './asset/001.png';  // "reactImg" is a variable name; it could be anything else.å
```
This image `reactImg` is then a Javascript object/variable that can be used in JSX code.
```html
<img src={reactImg} alt="imageAlt" />
```

### How React checks if UI needs to be updated  
React compares the old JSX and new new JSX and applies any differences to the actual website UI.  
For example, when Web App got loaded initially with code:  
```js
<div>
    <h1>Hello World</h1>
</div>
```
And later on, the code is changed to:
```js
<div>
    <h1>Hello World</h1>
    <p>New paragraph</p>
</div>
```
React will detect the state change and apply the update to the real DOM, ensuring that the visible UI matches the expected output.  

### React Best Practices
- When storing component, split across multiple files - one component per file. Optionally store the corresponding css style along with the component JSX scripts. (However, bear in mind that css' are accessible globally regardless where the css style files are stored)

## Reference
Set up React: https://krasimirtsonev.com/blog/article/The-bare-minimum-to-work-with-React
