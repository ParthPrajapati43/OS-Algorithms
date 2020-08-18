let rows = 0;

/*
This works well but not getting why entered values are getting reset/erased
on adding a new joob by clicking the ADD JOB button
:: FIXED ::
ISSUE Was: this was adding new tbody rather than tr
    let tab = document.querySelector("#Inputs");
*/
function AddJob() {
    let tab = document.querySelector("#Inputs").insertRow(++rows);
    tab.innerHTML +=
        `
        <tr>
            <td><input type="text" value="Job-${rows}" id="J${rows}" size="5" disabled></td>
            <td><input type="number" id="AT${rows}"></td>
            <td><input type="number" id="BT${rows}"></td>
            <td><input type="text" id="CT${rows}" size="5" disabled></td>
            <td><input type="text" id="TAT${rows}" size="5" disabled></td>
            <td><input type="text" id="WT${rows}" size="5" disabled></td>
            <td><input type="text" id="RT${rows}" size="5" disabled></td>
        </tr>
    `
}

/*
function AddJob() {
    let Row = document.querySelector("#Inputs").insertRow(++rows);
    let col = -1;
    let cell = Row.insertCell(++col);
    cell.innerHTML += `<input type="text" value="Job-${rows}" id="J${rows }" size="5" disabled>`;
    cell = Row.insertCell(++col);
    cell.innerHTML += `<input type="number" id="AT${rows}">`;
    cell = Row.insertCell(++col);
    cell.innerHTML += `<input type="number" id="BT${rows}">`;
    cell = Row.insertCell(++col);
    cell.innerHTML += `<input type="text" id="CT${rows}" size="5" disabled>`;
    cell = Row.insertCell(++col);
    cell.innerHTML += `<input type="text" id="TAT${rows}" size="5" disabled>`;
    cell = Row.insertCell(++col);
    cell.innerHTML += `<input type="text" id="WT${rows}" size="5" disabled>`;
    cell = Row.insertCell(++col);
    cell.innerHTML += `<input type="text" id="RT${rows}" size="5" disabled>`;
}
*/
function RemoveJob() {
    if (rows > 0)
        document.querySelector("#Inputs").deleteRow(rows--);
}

function Solve() {
    // incomplete
}