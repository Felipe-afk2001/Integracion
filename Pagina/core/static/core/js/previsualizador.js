const inputimg =document.querySelector('input[name=imagen]')
inputimg.addEventListener('change',function(){
    const preview = document.getElementById('file-preview-zone')
    preview.innerHTML=`<img src='${inputimg.value}' style='width:20%'>`
})
