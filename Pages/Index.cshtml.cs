
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;
using Microsoft.Data.SqlClient;

namespace AzureAPP.Pages
{
    public class IndexModel : PageModel
    {
        public string sensorName;
        public string measurementValue;
        private readonly ILogger<IndexModel> _logger;

        public IndexModel(ILogger<IndexModel> logger)
        {
            _logger = logger;
        }

        public void OnGet()
        {
            ///string connectionString = "Data Source=NAWHASW10\\MSSQLSERVER1; Initial Catalog=DATA;Integrated Security=True;TrustServerCertificate=True";
            //SqlConnection con = new SqlConnection(connectionString);
            //con.Open();

            //string sqlQuery = "Select SensorName, MeasurementValue from MeasurementD where MeasurementId=80 ";
            //SqlCommand cmd = new SqlCommand(sqlQuery, con);
            //SqlDataReader dr = cmd.ExecuteReader();
            //if (dr.Read())
            {
            //    sensorName = dr["SensorName"].ToString();
            //    measurementValue = dr["MeasurementValue"].ToString();
            }
            //con.Close();
        }
    }
}