    var updateBtns = document.getElementsByClassName('update-cart')

    for(var i = 0; i < updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
            var itemID = this.dataset.item
            var action = this.dataset.action
            console.log('itemID:', itemID, 'action:', action )

            console.log('USER:', user)
            if(user === 'AnonymousUser'){
                console.log('you are not logged in')
            }else{
                console.log('user is logged in, sending requested data')
            }
        })
    }