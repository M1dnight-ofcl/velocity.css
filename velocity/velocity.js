const init = () => {
    const sass = require('sass');
    const result = sass.compile('style.scss');
    css = result.css;
}