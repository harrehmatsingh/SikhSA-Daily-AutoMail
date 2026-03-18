
const input = process.argv[2];  // second argument after 'node convert.js <input>'

if (!input) {
    console.error("No input provided");
    process.exit(1);
}

const { toUnicode } = require("gurmukhi-utils");

const output = toUnicode(input);
console.log(output);
