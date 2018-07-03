/**
 * Created by tcz on 18-7-2.
 */
/**
 * Created by tcz on 18-7-3.
 */
function get_id() {
    var username = {"name":document.getElementById("Username-log").value};
    //alert(document.getElementById("Username-log").value);
    //alert(2);
     $.ajax(
        {
            url: '/Shrimp_hust/getid/',
            type: "POST",
            data: username,
            async: false,
            success: function (data) {
                rname = data;

            }
        }
    );
     //alert(rname);
    //alert(username);
    sessionStorage.setItem("username", document.getElementById("Username-log").value);
    sessionStorage.setItem("rname", rname);
    //window.open("http://127.0.0.1:8000/Shrimp_hust/movie/");
}