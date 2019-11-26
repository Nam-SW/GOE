package com.example.goe;

import android.graphics.Color;
import android.os.Bundle;

import com.github.mikephil.charting.animation.Easing;
import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.components.Description;
import com.github.mikephil.charting.components.XAxis;
import com.github.mikephil.charting.components.YAxis;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;

import java.util.ArrayList;
import java.util.List;

import androidx.appcompat.app.AppCompatActivity;

public class Graph_Activity extends AppCompatActivity {

    private LineChart lineChart2;
    private LineChart lineChart;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_graph_);

        lineChart2 = (LineChart)findViewById(R.id.chart);
        lineChart = findViewById(R.id.chart2);

        List<Entry> Electry_Data = new ArrayList<>();
        Electry_Data.add(new Entry(1, Bill(40)));
        Electry_Data.add(new Entry(2, Bill(100)));
        Electry_Data.add(new Entry(3, Bill(150)));
        Electry_Data.add(new Entry(4, Bill(180)));
        Electry_Data.add(new Entry(5, Bill(210)));
        Electry_Data.add(new Entry(6, Bill(250)));
        Electry_Data.add(new Entry(7, Bill(300)));
        Electry_Data.add(new Entry(8, Bill(345)));
        Electry_Data.add(new Entry(9, Bill(370)));
        Electry_Data.add(new Entry(10, Bill(390)));
        Electry_Data.add(new Entry(11, Bill(430)));
        Electry_Data.add(new Entry(12, Bill(500)));
        Electry_Data.add(new Entry(13, Bill(560)));
        Electry_Data.add(new Entry(14, Bill(590)));
        Electry_Data.add(new Entry(15, Bill(630)));
        Electry_Data.add(new Entry(16, Bill(700)));
        Electry_Data.add(new Entry(17, Bill(730)));
        Electry_Data.add(new Entry(18, Bill(760)));
        Electry_Data.add(new Entry(19, Bill(800)));
        Electry_Data.add(new Entry(20, Bill(850)));
        Electry_Data.add(new Entry(21, Bill(920)));
        Electry_Data.add(new Entry(22, Bill(960)));
        Electry_Data.add(new Entry(23, Bill(1000)));
        Electry_Data.add(new Entry(24,Bill(1100) ));
        Electry_Data.add(new Entry(25, Bill(1150)));
        Electry_Data.add(new Entry(26, Bill(1220)));

        List<Entry> entries = new ArrayList<>();
        entries.add(new Entry(1, Bill(45)));
        entries.add(new Entry(2, Bill(90)));
        entries.add(new Entry(3, Bill(140)));
        entries.add(new Entry(4, Bill(160)));
        entries.add(new Entry(5, Bill(200)));
        entries.add(new Entry(6, Bill(270)));
        entries.add(new Entry(7, Bill(320)));
        entries.add(new Entry(8, Bill(365)));
        entries.add(new Entry(9, Bill(390)));
        entries.add(new Entry(10, Bill(420)));
        entries.add(new Entry(11, Bill(440)));
        entries.add(new Entry(12, Bill(490)));
        entries.add(new Entry(13, Bill(530)));
        entries.add(new Entry(14, Bill(570)));
        entries.add(new Entry(15, Bill(620)));
        entries.add(new Entry(16, Bill(690)));
        entries.add(new Entry(17, Bill(750)));
        entries.add(new Entry(18, Bill(860)));
        entries.add(new Entry(19, Bill(900)));
        entries.add(new Entry(20, Bill(925)));
        entries.add(new Entry(21, Bill(950)));
        entries.add(new Entry(22, Bill(970)));
        entries.add(new Entry(23, Bill(990)));
        entries.add(new Entry(24,Bill(1060) ));
        entries.add(new Entry(25, Bill(1100)));
        entries.add(new Entry(26, Bill(1248)));
        entries.add(new Entry(27, Bill(1296)));
        entries.add(new Entry(28, Bill(1344)));
        entries.add(new Entry(29, Bill(1392)));
        entries.add(new Entry(30, Bill(1440)));


        LineDataSet lineDataSet = new LineDataSet(Electry_Data, "실제 요금");
        LineDataSet lineDataSet2 = new LineDataSet(entries, "예측된 요금");
        lineDataSet2.setLineWidth(2);
        lineDataSet2.setCircleRadius(6);
        lineDataSet2.setCircleColor(Color.parseColor("#FFA1B4DC"));
        lineDataSet2.setCircleColorHole(Color.BLUE);
        lineDataSet2.setColor(Color.parseColor("#FFA1B4DC"));
        lineDataSet2.setDrawCircleHole(true);
        lineDataSet2.setDrawCircles(true);
        lineDataSet2.setDrawHorizontalHighlightIndicator(false);
        lineDataSet2.setDrawHighlightIndicators(false);
        lineDataSet2.setDrawValues(true);

        lineDataSet.setLineWidth(2);
        lineDataSet.setCircleRadius(6);
        lineDataSet.setCircleColor(Color.parseColor("#FFA1B4DC"));
        lineDataSet.setCircleColorHole(Color.BLUE);
        lineDataSet.setColor(Color.parseColor("#FFA1B4DC"));
        lineDataSet.setDrawCircleHole(true);
        lineDataSet.setDrawCircles(true);
        lineDataSet.setDrawHorizontalHighlightIndicator(false);
        lineDataSet.setDrawHighlightIndicators(false);
        lineDataSet.setDrawValues(true);

        LineData lineData = new LineData(lineDataSet);
        lineChart2.setData(lineData);

        LineData lineData2 = new LineData(lineDataSet2);
        lineChart.setData(lineData2);

        XAxis xAxis = lineChart2.getXAxis();
        xAxis.setPosition(XAxis.XAxisPosition.BOTTOM);
        xAxis.setTextColor(Color.BLACK);
        xAxis.enableGridDashedLine(8, 24, 0);

        YAxis yLAxis = lineChart2.getAxisLeft();
        yLAxis.setTextColor(Color.BLACK);

        YAxis yRAxis = lineChart2.getAxisRight();
        yRAxis.setDrawLabels(false);
        yRAxis.setDrawAxisLine(false);
        yRAxis.setDrawGridLines(false);

        Description description = new Description();
        description.setText("");

        lineChart2.setDoubleTapToZoomEnabled(false);
        lineChart2.setDrawGridBackground(false);
        lineChart2.setDescription(description);
        lineChart2.animateY(2000, Easing.EasingOption.EaseInCubic);
        lineChart2.invalidate();

        XAxis xAxis2 = lineChart.getXAxis();
        xAxis2.setPosition(XAxis.XAxisPosition.BOTTOM);
        xAxis2.setTextColor(Color.BLACK);
        xAxis2.enableGridDashedLine(8, 24, 0);

        YAxis yLAxis2 = lineChart.getAxisLeft();
        yLAxis2.setTextColor(Color.BLACK);

        YAxis yRAxis2 = lineChart.getAxisRight();
        yRAxis2.setDrawLabels(false);
        yRAxis2.setDrawAxisLine(false);
        yRAxis2.setDrawGridLines(false);

        Description description2 = new Description();
        description2.setText("");

        lineChart.setDoubleTapToZoomEnabled(false);
        lineChart.setDrawGridBackground(false);
        lineChart.setDescription(description2);
        lineChart.animateY(2000, Easing.EasingOption.EaseInCubic);
        lineChart.invalidate();

    }
    public static int Bill(int UsedElectry){
        double bill;
        if(UsedElectry<=200)
        {
            bill=UsedElectry*93.3+910;
        }else if (UsedElectry<=400)
        {
            bill= 200*93.3+((UsedElectry-200)*187.9)+1600;
        }else
        {
            bill= 200*93.3+200*187.9+((UsedElectry-400)*280.6)+7300;
        }
        bill = bill+(bill/10)+(bill/1000*37);
        final int Electry_Bill = (int) (bill);
        return Electry_Bill;
    }

}
