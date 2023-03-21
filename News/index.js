<script>
    const searchFrom = document.querySelector('.search');
    const input = document.querySelector('.input');
    const newList = document.querySelector('.news-list');

    searchFrom.addEventListener('submit', retrieve)

    function retrieve(e) 
        e.preventDefault()
        const apiKey = '54e54e937b0e414c991dfe8f46517ca6'
        let topic = input.value;
        let url =`https://newsapi.org/v2/everything?q=${topic}&apiKey=${apiKey}`
        fetch(url).then((res)={">"}
            return res.json()
    ).then((data)={">"}{
        console.log(data)
    })
    
</script>