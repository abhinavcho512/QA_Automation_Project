// Test 1: Check Response Status and Content-Type
pm.test("Response status is OK", function () {
    pm.response.to.have.status(200);
});

pm.test("Content-Type is JSON", function () {
    pm.response.to.have.header("Content-Type", "application/json");
});

// Test 2: Verify Shipment Details
pm.test("Verify Shipment Details", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('shipment');
    pm.expect(jsonData.shipment).to.have.property('id', 'shp_e0b570fd1d7d4b62bd206917eae5881a');
});

// Test 3: Verify selected_rate and compare retail_rate and list_rate
pm.test("Verify selected_rate retail_rate is 12", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.shipment.selected_rate.retail_rate).to.eql(12);
});

pm.test("Verify retail_rate is greater than list_rate", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.shipment.selected_rate.retail_rate).to.be.greaterThan(jsonData.shipment.selected_rate.list_rate);
});