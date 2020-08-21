let rows = 0;

const AddJobbtn = document.getElementById("AddJob");
AddJobbtn.onclick = () => {
    let tab = document.querySelector("#Inputs").insertRow(++rows);
    tab.innerHTML +=
        `
        <tr>
            <td><input type="text" value="Job-${rows}" id="J${rows}" size="5" disabled></td>
            <td><input type="number" id="AT${rows}" value="0" min="0" required></td>
            <td><input type="number" id="BT${rows}" value="0" min="0" required></td>
            <td><input type="text" id="CT${rows}" size="5" disabled></td>
            <td><input type="text" id="TAT${rows}" size="5" disabled></td>
            <td><input type="text" id="WT${rows}" size="5" disabled></td>
            <td><input type="text" id="RT${rows}" size="5" disabled></td>
        </tr>
    `
}

const RemoveJobbtn = document.getElementById("RemoveJob");
RemoveJobbtn.onclick = () => {
    if (rows == 0)
        return;
    document.querySelector("#Inputs").deleteRow(rows--);
    if (rows == 0) {
        let r = 3;
        while (r--) {
            document.querySelector("#CalcAvg").deleteRow(r);
        }
    }
}

const Solvebtn = document.getElementById("Solve");
Solvebtn.onclick = () => {

    // if there are no jobs
    if (rows == 0)
        return;

    // check if any input box is empty or not
    for (let i = 1; i < rows + 1; ++i) {

        if (document.getElementById(`AT${i}`).value == '' || document.getElementById(`BT${i}`).value == '') {
            alert("Error! Some imputs are empty.");
            return;
        }
    }

    let table = [];
    // adding all the jobs data into an array
    for (let i = 1; i < rows + 1; ++i)
        table.push([Number(i), Number(document.getElementById(`AT${i}`).value), Number(document.getElementById(`BT${i}`).value), Number(0), Number(0), Number(0), Number(0)]);

    // sorting according to AT and if AT is same then BT
    for (let i = 0; i < rows; ++i) {
        for (let j = i + 1; j < rows; ++j) {
            if (table[j][1] < table[i][1]) {
                for (let k = 0; k < 3; ++k)
                    [table[j][k], table[i][k]] = [table[i][k], table[j][k]];
            }
            if (table[j][1] == table[i][1] && table[j][2] < table[i][2]) {
                for (let k = 0; k < 3; ++k)
                    [table[j][k], table[i][k]] = [table[i][k], table[j][k]];
            }
        }
    }

    // saving BT for further reference
    let originalBT = [];
    for (let i = 0; i < rows; ++i)
        originalBT.push(table[i][2]);

    // algorithm
    let curr = 0;
    let finished = 0;
    let cameonce = 0;
    let completed = [];

    for (let i = 0; i < rows; ++i)
        completed.push(false);

    while (cameonce != rows) {

        let isthere = false;

        //check if any process is availabe or not
        for (let i = 0; i < rows; ++i) {
            if (!completed[i] && table[i][1] <= curr) {
                isthere = true;
                break;
            }
        }

        // if not available make the current timer to the next closest Job
        if (!isthere) {
            curr = table[0][1];
            for (let i = 0; i < rows; ++i) {
                if (!completed[i]) {
                    curr = Math.min(curr, table[i][1]);
                }
            }
        }

        // get the list of all available Jobs
        let available = [];
        for (let i = 0; i < rows; ++i) {
            if (!completed[i] && table[i][1] <= curr)
                available.push(Number(i));
        }

        // now get the Job with lowest BT and run it for 1 unit time
        let present = available[0];
        for (let i = 0; i < available.length; ++i) {
            if (table[available[i]][2] < table[present][2])
                present = available[i];
        }

        // check if it came for the first time
        if (table[present][2] == originalBT[present]) {
            ++cameonce;
            table[present][6] = curr - table[present][1];
        }
        --table[present][2];
        ++curr

        // check if the job is finished or not
        if (table[present][2] == 0) {
            completed[present] = true;
            ++finished;
            table[present][3] = curr;
            table[present][4] = table[present][3] - table[present][1];
            table[present][5] = table[present][4] - originalBT[present];
        }
    }

    // after every job has been once into running state, continue with the algorithm of SJF
    while (finished != rows) {

        let isthere = false;

        //check if any process is availabe or not
        for (let i = 0; i < rows; ++i) {
            if (!completed[i] && table[i][1] <= curr) {
                isthere = true;
                break;
            }
        }

        // if not available make the current timer to the next closest Job
        if (!isthere) {
            curr = table[0][1];
            for (let i = 0; i < rows; ++i) {
                if (!completed[i]) {
                    curr = Math.min(curr, table[i][1]);
                }
            }
        }

        // get the list of all available Jobs
        let available = [];
        for (let i = 0; i < rows; ++i) {
            if (!completed[i] && table[i][1] <= curr)
                available.push(Number(i));
        }

        // now get the Job with lowest BT
        let present = available[0];
        let BT = table[available[0]][2];
        for (let i = 0; i < available.length; ++i) {
            if (table[available[i]][2] < BT) {
                BT = table[available[i]][2];
                present = available[i];
            }
        }

        // we got the process in present, complete it
        ++finished;
        completed[present] = true;
        curr += table[present][2];
        table[present][3] = curr;
        table[present][4] = table[present][3] - table[present][1];
        table[present][5] = table[present][4] - originalBT[present];
    }

    let avgTAT = 0;
    let avgWT = 0;
    let avgRT = 0;

    // setting the values to textbox
    for (let i = 0; i < rows; ++i) {
        avgTAT += table[i][4];
        avgWT += table[i][5];
        avgRT += table[i][6];
        document.getElementById(`CT${table[i][0]}`).value = `${table[i][3]}`;
        document.getElementById(`TAT${table[i][0]}`).value = `${table[i][4]}`;
        document.getElementById(`WT${table[i][0]}`).value = `${table[i][5]}`;
        document.getElementById(`RT${table[i][0]}`).value = `${table[i][6]}`;
    }

    // calculating the average
    avgTAT /= rows;
    avgWT /= rows;
    avgRT /= rows;

    // displaying the average
    let avgg = document.querySelector("#average");
    avgg.innerHTML =
        `
        <table id="CalcAvg" cellspacing="5px">
            <tr>
                <th><input type="text" id="avggTAT" size="9" value="Average TAT :" disabled></th>
                <td><input type="text" name="avgTAT" id="avgTAT" value="${avgTAT}" disabled></td>
            </tr>
            <tr>
                <th><input type="text" id="avggWT" size="9" value="Average WT  :" disabled></th>
                <td><input type="text" name="avgWT" id="avgWT" value="${avgWT}" disabled></td>
            </tr>
            <tr>
                <th><input type="text" id="avggRT" size="9" value="Average RT  : " disabled></th>
                <td><input type="text" name="avgRT" id="avgRT" value="${avgRT}" disabled></td>
            </tr>
        </table>
    `
}