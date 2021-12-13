using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Data.SqlClient;
namespace AzureAPP.Models
{
    public class Chart
    {
        public int measurementId { get; set; }
        public string sensorName { get; set; }
        public float measurementValue { get; set; }

        public string measurementDateTime { get; set; }

        public List<Chart> GetChartData(string connectionString)
        {
            List<Chart> chartDataList = new List<Chart>();
            SqlConnection con = new SqlConnection(connectionString);
            string selectSQL = "Select MeasurementId, SensorName, ReferenceValue, MeasurementValue, Unit, MeasurementDateTime from MeasurementDatabase";//
            con.Open();
            SqlCommand cmd = new SqlCommand(selectSQL, con);
            SqlDataReader dr = cmd.ExecuteReader();
            if (dr != null)
            {
                while (dr.Read())
                {
                    Chart chartData = new Chart();
                    chartData.measurementId = Convert.ToInt32(dr["MeasurementId"]);
                    chartData.measurementDateTime = dr["MeasurementDateTime"].ToString();
                    chartData.measurementValue = Convert.ToSingle(dr["MeasurementValue"]);
                    //chartData.measurementValue = Convert.ToSingle(dr["ReferenceValue"]); //
                    chartDataList.Add(chartData);
                }
            }
            return chartDataList;
        }
    }
}
