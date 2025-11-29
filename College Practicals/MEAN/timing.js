
console.log("h")
setInterval(function () {
    console.log("time out")
}, 3000)
setTimeout(function () {
    console.log("interval")
}, 3000)
setImmediate(function () {
    console.log("immediate")
}, 3000)

async function name(params) {
    console.log(params);
}

await name("test")

console.log("ii")
process.nextTick(() => {
    console.log("nextTick1");
});