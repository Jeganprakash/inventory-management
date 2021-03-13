


function loadData() {
    const url = "/mobileTable";

    fetch(url)
        .then(response => response.json())

        .then(json => {
            console.log(json);
            setTable(json);
        }
        );
}



function setTable(tabledata) {

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
        autoResize: true,
        initialSort: [             //set the initial sort order of the data
            { column: "name", dir: "asc" },
        ],
        columns: [                 //define the table columns
            { title: "id", field: "id" },
            { title: "Statistics_Model", field: "Statistics_Model" },
            { title: "All_Stock", field: "All_Stock" },
            { title: "Sales_Proportion", field: "Sales_Proportion", hozAlign: "center" },
            { title: "Sales_Volume", field: "Sales_Volume", hozAlign: "center" },
            { title: "Stock_Proportion", field: "Stock_Proportion", hozAlign: "center" },
            { title: "Turnover_Days", field: "Turnover_Days" },
        ],
    });

    window.addEventListener('resize', function () {
        table.redraw();
    });
}


function warhouseData() {
    const url = "/warehouseTable";

    fetch(url)
        .then(response => response.json())

        .then(json => {
            console.log(json);
            setTable2(json);
        }
        );
}


function setTable2(tabledata) {

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
        autoResize: true,
        initialSort: [             //set the initial sort order of the data
            { column: "name", dir: "asc" },
        ],
        columns: [                 //define the table columns
            { title: "Warehouse_ID", field: "id" },
            { title: "All_Stock", field: "All_Stock" },
            { title: "Sales_Proportion", field: "Sales_Proportion", hozAlign: "center" },
            { title: "Sales_Volume", field: "Sales_Volume", hozAlign: "center" },
            { title: "Stock_Proportion", field: "Stock_Proportion", hozAlign: "center" },
            { title: "Turnover_Days", field: "Turnover_Days" },
        ],
    });

    window.addEventListener('resize', function () {
        table.redraw();
    });
}
