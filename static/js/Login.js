window.onload = () =>
    {
        const form = document.querySelector('.box-form')
    
        document.querySelector('.box-form h2').onclick = () => form.classList.add('box-form-open')
    
        document.querySelector('.close').onclick = () => form.classList.remove('box-form-open')
        
    }