var img = document.getElementById('product_img_id');
//or however you get a handle to the IMG
var width = img.clientWidth;
var height = img.clientHeight;

var options = {
    width: width, // required
    // more options here
    zoomWidth: width,
    scale: .7,

};
new ImageZoom(document.getElementById("img-container"), options);

var options = {
    width: 400,
    height: 400
};

var options = {
    width: 400,
    zoomWidth: 500
};

var options = {
    width: 400,
    img: '/path/to/1.jpg'
};

var options = {
    width: 400,
    offset: {
        vertical: 0,
        horizontal: 10
    }
};

var options = {
    width: 400,
    scale: 2.5
};

var options = {
    width: 400,
    zoomContainer: domNode
};

c

var options = {
    width: 400,
    zoomPosition: 'left'
}