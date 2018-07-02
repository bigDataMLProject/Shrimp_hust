/**
 * Created by tcz on 18-7-2.
 */
 function test(){
     alert(1)
 }
function new_movie(target) {
    var movie_name = {"name":$(target).text()};
    // window.open("http://www.baidu.com");
    //alert(2);

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
    // // alert(3);
    // //alert(movie_data);
    sessionStorage.setItem("key", movie_data);
    //alert(data1);
    //window.location.href("http://127.0.0.1:8000/Shrimp_hust/movie/detail/");
    window.open("http://127.0.0.1:8000/Shrimp_hust/movie/detail/");
    //location.reload();
}

