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

}

function show_movie(target) {
    var movie_name = {"name":$(target).text()};
    // window.open("http://www.baidu.com");
    //alert(1);

    //
     $.ajax(
        {
            url: '/Shrimp_hust/show/',
            type: "POST",
            data: movie_name,
            async: false,
            success: function (data) {
                //data1 = data;
                //movie_data = JSON.parse(data);
                movie_data = data;
                //alert(2);
                //movie_data = data;
                //document.getElementById("show").textContent = "TCZ";

            }
        }
    );
    // alert(3);
    //alert(movie_data);
    sessionStorage.setItem("key", movie_data);
    //alert(data1);
    window.open("detail/");
}

//$(".button-collapse").sideNav();

// $('.button-collapse').sideNav({
//       menuWidth: 300, // Default is 240
//       edge: 'right', // Choose the horizontal origin
//       closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
//       draggable: true // Choose whether you can drag to open on touch screens
//     }
//   );
