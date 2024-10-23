
## Quick Start
pending




## Developer Notes
### Folder structure
- `public/index.html`: HTML template. Points to `public/scripts/app.js`.
- `public/scripts/app.js`: auto-translated code by `babel` compiled from `src/app.js`. No manual edit.
- `src/app.js`: source code in JSX format. Editable.

To setup the auto-translation:
```sh
babel src/app.js --out-file public/scripts/app.js
```