using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Data.SqlClient;

namespace AzureAPP.Models
{
    public class Measurement
    {
        public int measurementId { get; set; }
        public string sensorName { get; set; }
        public float measurementValue { get; set; }
        public float referenceValue { get; set; }

        public string unit { get; set; }
        public string measurementDateTime { get; set; }
        

        public List<Measurement> GetMeasurementParameters(string connectionString)
        {
            List<Measurement> measurementParameterList = new List<Measurement>();

            
            SqlConnection con = new SqlConnection(connectionString);
            string sqlQuery = "Select MeasurementId, SensorName, ReferenceValue, MeasurementValue, Unit, MeasurementDateTime from MeasurementDatabase";//
            con.Open();

            SqlCommand cmd = new SqlCommand(sqlQuery, con);
            SqlDataReader dr = cmd.ExecuteReader();


            if (dr != null)
            {
                while (dr.Read())
                {
                    Measurement measurementParameter = new Measurement();
                    measurementParameter.measurementId = Convert.ToInt32(dr["MeasurementId"]);
                    measurementParameter.sensorName = dr["SensorName"].ToString(); //
                    measurementParameter.referenceValue = Convert.ToSingle(dr["ReferenceValue"]);
                    measurementParameter.measurementValue = Convert.ToSingle(dr["MeasurementValue"]);
                    measurementParameter.unit = dr["Unit"].ToString(); //
                    measurementParameter.measurementDateTime = dr["MeasurementDateTime"].ToString();
                    measurementParameterList.Add(measurementParameter);
                }

            }
            return measurementParameterList;


        }
    }
}
