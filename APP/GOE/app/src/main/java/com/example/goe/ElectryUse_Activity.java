package com.example.goe;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class ElectryUse_Activity extends AppCompatActivity {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_electry_use_);

        final int a = 1220;
        final TextView txt = findViewById(R.id.elec);
        ImageButton btn = findViewById(R.id.btnrotate);



        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                txt.setText(a+"Kwh");
            }
        });


    }
}
