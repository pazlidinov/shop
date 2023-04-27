// Product Quantity
function minus() {
    let count = document.getElementById(id = 'count')
    num = Number(count.value)
    if (num > 1) {
        count.value = (num - 1).toString()
    }
}
function plus() {
    let count = document.getElementById(id = 'count')
    num = Number(count.value)
    count.value = (num + 1).toString()
}