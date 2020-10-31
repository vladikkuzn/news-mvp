function getCookie(name)
 {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '')
     {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++)
         {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '='))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


document.addEventListener("DOMContentLoaded", buildNews)

function buildNews()
{
    let wrapper = document.getElementById('list-wrapper')
    wrapper.innerHTML = ''
    //let url = 'http://127.0.0.1:8000/api/posts/'
    let url = 'https://news-mvp.herokuapp.com/api/posts/'

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data)
    {
        console.log('Data:', data)

        let list = data
        for (let i in list)
        {
            let item = `<div id="data-row-${i}" class="news-wrapper flex-wrapper">
                    <a style="flex: 7" href=${list[i].link}>
                        <span class="title">${list[i].title}</span><br/>
                        <span class="amount_of_upvotes">${list[i].amount_of_upvotes}</span>
                        <span class="author-name">${list[i].author_name}</span><br/>
                        <span class="creation-date">${new Date(list[i].creation_date).toDateString()}</span>
                    </a>
                    <div style="flex: 1">
                        <button class="btn btn-sm btn-outline-info edit">Edit </button>
                    </div>
                    <div style="flex: 1">
                        <button class="btn btn-sm btn-outline-dark delete">Delete </button>
                    </div>
                </div>
            `
            wrapper.innerHTML += item
        }

        for (let i in list)
        {
            let editBtn = document.getElementsByClassName('edit')[i]
            editBtn.addEventListener('click', function(){
                editItem(list[i])
            })
        }
    })

}

document.addEventListener("DOMContentLoaded", submitForm)

function submitForm()
{
let form = document.getElementById('form-wrapper')
form.addEventListener('submit', (e) => {
    e.preventDefault()
    console.log('Form submited')
    //let url = 'http://127.0.0.1:8000/api/post-create/'
    let url = 'https://news-mvp.herokuapp.com/api/post-create/'

    if(activeItem != null)
    {
        url = `https://news-mvp.herokuapp.com/api/post-update/${activeItem.id}/`
        activeItem = null
    }

    let title = document.getElementById('title').value
    let link = document.getElementById('link').value
    let author = document.getElementById('author-name').value

    fetch(url, {
        method: "POST",
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'title': title,
            'link': link,
            'author_name': author
        })
    })
    .then(() => {
        buildNews()
        document.getElementById('form').reset()
        })
    })
}

var activeItem = null

function editItem(item)
{
    console.log('Item clicked: ', item)
    activeItem = item
    document.getElementById('title').value = activeItem.title
    document.getElementById('link').value = activeItem.link
    document.getElementById('author_name').value = activeItem.author_name
}
