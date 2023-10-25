const Velocity = class {
    constructor(defaultThemePath = './themes/default.json') {
        fetch("./themes/default.json")
            .then(response => response.json())
            .then(json => console.log(json));
    }
};

const v = Velocity()