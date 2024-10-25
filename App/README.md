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
#### Components
A component in React is simply a function that return renderable content - typically JSX code. The JSX code leads to a tree-like code structure that informs React how different componsnents are related and how the UI should look like. It then executes appropriate commands to manipulate the real DOM to reflect that target structure.


## Reference
Set up React: https://krasimirtsonev.com/blog/article/The-bare-minimum-to-work-with-React
