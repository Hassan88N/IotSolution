using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using AzureAPP.Models;
using Microsoft.Extensions.Configuration;


namespace AzureAPP.Pages
{
    public class MeasurementModel : PageModel
    {
        public List<Chart> chartDataList = new List<Chart>();//

        readonly IConfiguration _configuration;
        public List<Measurement> measurementParameterList = new List<Measurement>();
        public string connectionString;
        public MeasurementModel(IConfiguration configuration)
        {
            _configuration = configuration;
        }

        public void OnGet()
        {
            Measurement measurement = new Measurement();
            connectionString = _configuration.GetConnectionString("ConnectionString");
            measurementParameterList = measurement.GetMeasurementParameters(connectionString);

            chartDataList = ChartData(); //

        }
        private List<Chart> ChartData() //
        {
            connectionString = _configuration.GetConnectionString("ConnectionString");
            List<Chart> chartDataList = new List<Chart>();
            Chart chartData = new Chart();
            chartDataList = chartData.GetChartData(connectionString);
            return chartDataList;
        }
    }
}
