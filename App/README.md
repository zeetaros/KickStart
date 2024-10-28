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

### React
Core concepts:
- Components
- Props
- State
- Events

#### Components
A component in React is simply a function that return renderable content - typically JSX code. The JSX code leads to a tree-like code structure that informs React how different componsnents are related and how the UI should look like. It then executes appropriate commands to manipulate the real DOM to reflect that target structure.  
To use custom components, their name must be capitalised. That's how React tells them apart from built-in HTML elements.  

**N.B.** By default, React components execute **Only Once**. It is executed when the components are encountered at the first time when the App is loaded. The components have to be informed if it should be executed again.

#### Props
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

**Creating annoymous event handling functions**  
Two syntax styles:
```js
// Event function
function selectHandler() {
    console.log("Event triggered");
}
// (1)
<TabButton onSelect={() => selectHandler()}>some_labels</TabButton>
// (2)
<TabButton onSelect={function() {selectHandler}}>some_labels</TabButton>
```

#### Images
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

#### How React checks if UI needs to be updated  
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

## Reference
Set up React: https://krasimirtsonev.com/blog/article/The-bare-minimum-to-work-with-React
