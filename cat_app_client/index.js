const newForm = document.getElementById('new-cat-form');
const cats = document.getElementById('cats');
const info = document.getElementById('info-banner')

newForm.onsubmit = addCat

const setBannerText = e => info.innerHTML = e.target.alt
const clearBannerText = e => info.innerHTML = "Kitties!"

const addAllCats = ({cats}) => cats.forEach(cat => appendCat(JSON.parse(cat)))

fetch('http://localhost:5000/cats')
    .then(resp => resp.json())
    .then(addAllCats)

async function addCat(e){
    e.preventDefault();
    const { name, age, image } = e.target
    catData = { name: name.value, age: age.value, image: image.value}
    console.log(catData)
    fetch('http://localhost:5000/cats', {
        method: 'POST',
        body: JSON.stringify(catData),
        headers: { "Content-Type": "application/json"}
    })
        .then(resp => resp.json())
        .then(appendCat)
}

function appendCat(cat){
    const catCard = document.createElement('img')
    catCard.src = cat.img_url
    catCard.className = 'cat-card'
    catCard.alt = `${cat.name} - ${cat.age} years young`
    catCard.onmouseover = setBannerText
    catCard.onmouseout = clearBannerText
    console.log(catCard)
    cats.append(catCard)
}
