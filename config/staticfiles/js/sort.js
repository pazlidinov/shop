function check_fun(id) {
    let chek = document.getElementById(id)
    if (chek.ariaChecked == 'true') {
        chek.ariaChecked = 'false'
    }
    else {
        chek.ariaChecked = 'true'
    }

}

function key_word() {
    let key_category = ''
    console.log('00000')
    let a_link = document.getElementById('filter')
    let name_input = document.getElementById('search')
    let category_slug = document.getElementsByClassName('category');
    let color_slug = document.getElementsByClassName('color');
    let size_slug = document.getElementsByClassName('size');

    key_category += name_input.value + '*'

    for (let i = 0; i < category_slug.length; i++) {
        if (category_slug[i].ariaChecked == 'true') {

            key_category += category_slug[i].id[2] + '+'

        }
    }
    console.log(category_slug[-1])
    key_category += '*'

    for (let i = 0; i < color_slug.length; i++) {
        if (color_slug[i].ariaChecked == 'true') {

            key_category += color_slug[i].id[2] + '+'
        }
    }

    key_category += '*'

    for (let i = 0; i < size_slug.length; i++) {
        if (size_slug[i].ariaChecked == 'true') {
            key_category += size_slug[i].id[1] + '+'
        }
    }


    // a_link.href = "{% url 'main_app:sort_products' " + key_category + " %}"
    a_link.href = key_category
}
function cart_update(id) {
    let update_value = document.getElementById('quantity')
    let a_link = document.getElementById('update')
    key_update = String(id + '+' + update_value.value)
    
    a_link.href = "update/" + key_update
}