/**
 * Created by tcz on 18-6-30.
 */
function search_movie(target) {
    var movie_type = {"type":$(target).text()};
    //alert(movie_type);

    $.ajax(
        {
            url: '/Shrimp_hust/type/',
            type: "POST",
            data: movie_type,
            //dataType: 'json',
            success: function (data){
                data = JSON.parse(data);
                // alert(data["src0"]);
                for(i=0;i<6;i++){
                    var src = "src"+i;
                    //alert(src);
                    var type = "type"+i;
                    var name = "name"+i;
                    document.getElementById(src).src = data[src];
                    document.getElementById(type).textContent = data[type];
                    document.getElementById(name).textContent = data[name];

    }
            }
        }
    )

    //location.reload()
}

function test(data) {
    alert(data)
}

function show_movie(data) {
    data = JSON.parse(data);
    for(i=0;i<6;i++){
        var src = "src"+str(i);
        var type = "type"+str(i);
        var name = "name"+str(i);
        document.getElementById(src).src = data[src];
        document.getElementById(type).src = data[type];
        document.getElementById(name).src = data[name];

    }
}