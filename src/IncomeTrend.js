import React, { useState, useEffect } from "react";
import axios from "axios";
import { Line } from "react-chartjs-2";

const IncomeTrend = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios("/income");
      setData(result.data);
    };
    fetchData();
  }, []);

  const chartData = {
    labels: data.map((item) => item.date),
    datasets: [
      {
        label: "Income Trend",
        data: data.map((item) => item.income),
        fill: false,
        backgroundColor: "#0074D9",
        borderColor: "#0074D9",
        pointBackgroundColor: "#0074D9",
        pointBorderColor: "#0074D9",
        pointHoverBackgroundColor: "#0074D9",
        pointHoverBorderColor: "#0074D9",
      },
    ],
  };

  const options = {
    scales: {
      xAxes: [
        {
          type: "time",
          time: {
            unit: "month",
            displayFormats: {
              month: "MMM YYYY",
            },
          },
        },
      ],
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  };

  return <Line data={chartData} options={options} />;
};

export default IncomeTrend;