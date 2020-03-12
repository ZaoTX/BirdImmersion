using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mapbox.Unity.Utilities;
//using System.Collections.Generic;
using Mapbox.Unity.Map;
using Mapbox.Examples;

public class line_gen : MonoBehaviour
{
    public Spawn_Bird spawn_bird;
    //public SpawnOnMap MySpawnMap;
    //
    public AbstractMap _map;
    //read data from 
    public csvReader reader;
    public process process;
    //the number of individual
    private int indiviudal_num;
    // array of colors
    private Color[] colors;
    // Start is called before the first frame update
    //private LineRenderer line;
    void Start()
    {
        
        createColors();
        drawline();

    }
    void createColors() {
        indiviudal_num = reader.gp.individualBehaviors.Count;
        colors = new Color [indiviudal_num];
        
        for (int i = 0; i < indiviudal_num; i++)
        {/*
            
            colors[i] = color;
            Debug.Log(color.r);*/
        }
    }
    void Update() {
        updateLine();
    }
    void updateLine() {
        int count = this.transform.childCount;
        for (int i = 0; i < count; i++)
        {
            GameObject child = this.transform.GetChild(i).transform.gameObject;
            IndividualBehavior id = reader.gp.individualBehaviors[i];
            int trackCount = id.Individualtracks.Count;//number of datapoints for each individual
            string[] locations = spawn_bird._LocationStrings[i];
            float[] heights = spawn_bird._HeightArray[i];
            Vector3[] vP = new Vector3[trackCount];
            child.GetComponent<LineRenderer>().positionCount = trackCount;
            child.GetComponent<LineRenderer>().widthMultiplier = process.lineScale;
            for (int j = 0; j < trackCount; j++)
            {
                string loc = locations[j];
                float height = heights[j];
                var location = Conversions.StringToLatLon(loc);
                var localPosition = _map.GeoToWorldPosition(location,  true);
                Vector3 point = new Vector3(localPosition.x, localPosition.y+height, localPosition.z);
                vP[j] = point;
            }
            child.GetComponent<LineRenderer>().SetPositions(vP);
        }
    }
    void drawline() {
        for (int i = 0; i < indiviudal_num; i++)
        {
            //random bright color
            Color color = new Color(
            Random.Range(0.3f, 3f),
            Random.Range(0.3f, 3f),
            Random.Range(0.3f, 3f)
            );
           
            string childID =  i.ToString();
            GameObject child = new GameObject(childID);
            child.AddComponent<birdMovement>();
            child.transform.parent = this.transform;
            LineRenderer lineRenderer = child.AddComponent<LineRenderer>();
            //Color color = colors[i];
            lineRenderer.widthMultiplier = 30f;
            lineRenderer.material = new Material(Shader.Find("Standard"));
            lineRenderer.material.SetColor("_Color",color);

            IndividualBehavior id = reader.gp.individualBehaviors[i];
            int trackCount = id.Individualtracks.Count;//number of datapoints for each individual
            string[] locations = spawn_bird._LocationStrings[i];
            float[] heights = spawn_bird._HeightArray[i];
            Vector3[] vP = new Vector3[trackCount];
            lineRenderer.positionCount=trackCount;
            for (int j = 0; j < trackCount; j++) {
                string loc = locations[j];
                float height = heights[j];
                var location = Conversions.StringToLatLon(loc);
                var localPosition = _map.GeoToWorldPosition(location, true);
                Vector3 point = new Vector3(localPosition.x, localPosition.y+height, localPosition.z);
                vP[j] = point;
            }
            //Debug.Log(vP.Length);
            lineRenderer.SetPositions(vP);
        }
    }
}
