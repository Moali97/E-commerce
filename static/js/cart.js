    var updateBtns = document.getElementsByClassName('update-cart')

    for(var i = 0; i < updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
            var itemID = this.dataset.item
            var action = this.dataset.action
            console.log('itemID:', itemID, 'action:', action )

            console.log('USER:', user)
        })
    }