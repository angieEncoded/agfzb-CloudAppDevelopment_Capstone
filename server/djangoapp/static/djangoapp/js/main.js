// alert('linked')

// <a href="{% url 'djangoapp:get_dealer_details' dealer.id %}"></a>
// Open the link programatically to make the entire table row nicely clickable
const open_dealer_details = (url) => {
    // console.log(url)
    // console.log("clicked")
    document.location.href = url
}