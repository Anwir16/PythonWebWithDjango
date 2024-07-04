document.addEventListener('DOMContentLoaded', function() {
    const table = document.getElementById('datatable');
    const headers = table.querySelectorAll('thead th');
    const rows = table.querySelectorAll('tbody tr');
  
    // Create columns array from table headers
    const columns = Array.from(headers).map(header => ({
      label: header.innerText,
      field: header.innerText.toLowerCase().replace(/ /g, '_') // Convert header text to field name
    }));
  
    // Create rows array from table body
    const dataRows = Array.from(rows).map(row => {
      const cells = row.querySelectorAll('td');
      return Array.from(cells).map(cell => cell.innerText);
    });
  
    const data = {
      columns: columns,
      rows: dataRows,
    };
  
    const instance = new mdb.Datatable(document.getElementById('datatable'), data);
  
    document.getElementById('datatable-search-input').addEventListener('input', (e) => {
      instance.search(e.target.value);
    });
  });
  