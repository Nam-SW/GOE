package com.example.goe;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import androidx.appcompat.app.AppCompatActivity;

public class Billuse_Activity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_billuse_);

        final TextView bill_text = findViewById(R.id.textView9);

        Button btnGraph = findViewById(R.id.button2);


        ImageButton rotate = findViewById(R.id.imageButton);
        FloatingActionButton btnSetting = findViewById(R.id.floatingActionButton2);

        btnSetting.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "미개발",Toast.LENGTH_LONG).show();
            }
        });

        btnGraph.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Billuse_Activity.this,Graph_Activity.class );
                startActivity(intent);
            }
        });


        rotate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                bill_text.setText(Bill(1220)+"원");
            }
        });

    }



    public static int Bill(int UsedElectry){
        double bill;
        UsedElectry = (int) (UsedElectry/2*0.1);
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
