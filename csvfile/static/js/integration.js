
var DbDetails = {};

function validate() {
    var input = document.getElementsByClassName('datainput__input');

    var flag = 1;
    Array.prototype.forEach.call(input, (elem) => {
        if (elem.tagName === "select") {
            DbDetails[elem.name] = elem.options[elem.selectedIndex].value;
            return;
        }
        console.log("hi");
        if (elem.value === '') {

            elem.nextElementSibling.classList.remove('h-hide');
            flag = 0;
        }
        DbDetails[elem.name] = elem.value;
    });
    if (flag == 1)
        ConnectDb(DbDetails);
}


function funct() {
    alert("File uploaded Sucessfully !");
}


function ConnectDb(DbDetails) {

    // POST request using fetch() 
    const proxyurl = "https://cors-anywhere.herokuapp.com/";
    const url = "http://localhost:8080/CRM/ConnectDB";
    fetch(url, {

        // Adding method type 
        method: "POST",


        // Adding body or contents to send 
        body: JSON.stringify(DbDetails),

        // Adding headers to the request 
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "Content-type": "application/json; charset=UTF-8",
            "Retry-After": 3600
        }
    })

        // Converting to JSON 
        .then(response => response.json())

        // Displaying results to console 
        .then(json => {
            console.log(json);
            setTable(json);
        });
};



function setTable(tableData) {
    var tabledata = [
        { id: 1, name: "Oli Bob", progress: 12, gender: "male", rating: 1, col: "red", dob: "19/02/1984", car: 1 },
        { id: 2, name: "Mary May", progress: 1, gender: "female", rating: 2, col: "blue", dob: "14/05/1982", car: true },
        { id: 3, name: "Christine Lobowski", progress: 42, gender: "female", rating: 0, col: "green", dob: "22/05/1982", car: "true" },
        { id: 4, name: "Brendon Philips", progress: 100, gender: "male", rating: 1, col: "orange", dob: "01/08/1980" },
        { id: 5, name: "Margret Marmajuke", progress: 16, gender: "female", rating: 5, col: "yellow", dob: "31/01/1999" },
        { id: 6, name: "Frank Harbours", progress: 38, gender: "male", rating: 4, col: "red", dob: "12/05/1966", car: 1 },
        { id: 1, name: "Oli Bob", progress: 12, gender: "male", rating: 1, col: "red", dob: "19/02/1984", car: 1 },
        { id: 2, name: "Mary May", progress: 1, gender: "female", rating: 2, col: "blue", dob: "14/05/1982", car: true },
        { id: 3, name: "Christine Lobowski", progress: 42, gender: "female", rating: 0, col: "green", dob: "22/05/1982", car: "true" },
        { id: 4, name: "Brendon Philips", progress: 100, gender: "male", rating: 1, col: "orange", dob: "01/08/1980" },
        { id: 5, name: "Margret Marmajuke", progress: 16, gender: "female", rating: 5, col: "yellow", dob: "31/01/1999" },
        { id: 6, name: "Frank Harbours", progress: 38, gender: "male", rating: 4, col: "red", dob: "12/05/1966", car: 1 },
        { id: 1, name: "Oli Bob", progress: 12, gender: "male", rating: 1, col: "red", dob: "19/02/1984", car: 1 },
        { id: 2, name: "Mary May", progress: 1, gender: "female", rating: 2, col: "blue", dob: "14/05/1982", car: true },
        { id: 3, name: "Christine Lobowski", progress: 42, gender: "female", rating: 0, col: "green", dob: "22/05/1982", car: "true" },
        { id: 4, name: "Brendon Philips", progress: 100, gender: "male", rating: 1, col: "orange", dob: "01/08/1980" },
        { id: 5, name: "Margret Marmajuke", progress: 16, gender: "female", rating: 5, col: "yellow", dob: "31/01/1999" },
        { id: 6, name: "Frank Harbours", progress: 38, gender: "male", rating: 4, col: "red", dob: "12/05/1966", car: 1 },
        { id: 1, name: "Oli Bob", progress: 12, gender: "male", rating: 1, col: "red", dob: "19/02/1984", car: 1 },
        { id: 2, name: "Mary May", progress: 1, gender: "female", rating: 2, col: "blue", dob: "14/05/1982", car: true },
        { id: 3, name: "Christine Lobowski", progress: 42, gender: "female", rating: 0, col: "green", dob: "22/05/1982", car: "true" },
        { id: 4, name: "Brendon Philips", progress: 100, gender: "male", rating: 1, col: "orange", dob: "01/08/1980" },
        { id: 5, name: "Margret Marmajuke", progress: 16, gender: "female", rating: 5, col: "yellow", dob: "31/01/1999" },
        { id: 6, name: "Frank Harbours", progress: 38, gender: "male", rating: 4, col: "red", dob: "12/05/1966", car: 1 },
    ];

    //initialize table
    var elem = document.getElementById("tableData");
    elem.parentNode.classList.add("c-card--height");
    elem.classList.remove("c-card__logo");
    elem.classList.add("c-card__table");

    document.getElementById("tableButton").classList.add("h-hide");


    var table = new Tabulator("#tableData", {
        data: tabledata,           //load row data from array
        layout: "fitColumns",      //fit columns to width of table
        responsiveLayout: "hide",  //hide columns that dont fit on the table
        tooltips: true,            //show tool tips on cells
        addRowPos: "top",          //when adding a new row, add it to the top of the table
        history: true,             //allow undo and redo actions on the table
        pagination: "local",       //paginate the data
        paginationSize: 20,         //allow 7 rows per page of data
        movableColumns: true,      //allow column order to be changed
        resizableRows: true,       //allow row order to be changed
        initialSort: [             //set the initial sort order of the data
            { column: "name", dir: "asc" },
        ],
        columns: [                 //define the table columns
            { title: "Name", field: "name" },
            { title: "Task Progress", field: "progress" },
            { title: "Gender", field: "gender", width: 95 },
            { title: "Rating", field: "rating", hozAlign: "center", width: 100 },
            { title: "Color", field: "col", width: 130 },
            { title: "Date Of Birth", field: "dob", width: 130, sorter: "date", hozAlign: "center" },
            { title: "Driver", field: "car", width: 90, hozAlign: "center", formatter: "tickCross", sorter: "boolean", editor: true },
        ],
    });
}