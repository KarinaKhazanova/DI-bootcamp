function calculateTip() {
    const bill = Number(prompt("Type amount of the bill:"))
    let tip = 0

    if (bill < 50) tip = 20
    if (bill >= 50 && bill < 200) tip = 15
    if (bill >= 200) tip = 10
    const finalBill = bill + (tip/100) * bill

    console.log(tip + "%", finalBill)
}

calculateTip()