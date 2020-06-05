using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mapbox.Unity.Utilities;
//using System.Collections.Generic;
using Mapbox.Unity.Map;
using Mapbox.Examples;

/**
*  we append this to a game object and we this will spawn lines automatically
*/
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
    public double OverallTime;

    public string curMin;
    public string curMax;
    public bool needUpdate;
    public bool canUpdateModel;
    public float overallSpeed;
    public bool restart;
    /*public int minIndex;
    public int maxIndex;*/
    void Start()
    {
        needUpdate = true;
        restart = false;
        canUpdateModel = true;
        indiviudal_num = reader.gp.individualBehaviors.Count;
        colors = new Color[indiviudal_num];
        drawline();
        OverallTime=0;
        GetMinMaxTime();


    }
    void Update() {
       if (needUpdate) {
            //We check whether is needed to update the line again
            updateLine();
            needUpdate = false;
            canUpdateModel = true;
        }
        overallSpeed = spawn_bird.speed;
        OverallTime+=Time.deltaTime*overallSpeed;
    }
    //After reading the data we want to understand:
    //when does the first individual come,
    //when does the last individual finish
    void GetMinMaxTime()
    {
        IndividualBehavior firstId = reader.gp.individualBehaviors[0];
        int firstlen = firstId.Individualtracks.Count;
        string fFirst = firstId.Individualtracks[0].timestamp;
        string fLast = firstId.Individualtracks[firstlen - 1].timestamp;
        curMin=fFirst;
        curMax=fLast;
        /*minIndex=0;
        maxIndex=0;*/
        for (int i = 1; i < indiviudal_num; i++)
        {
            IndividualBehavior id = reader.gp.individualBehaviors[i];
            int len = id.Individualtracks.Count;
            string localFirst = id.Individualtracks[0].timestamp;
            string localLast = id.Individualtracks[len-1].timestamp;
            if (!compareTime(localFirst, curMin)) 
            { //local is ealier
                curMin = localFirst;
                //minIndex = i;
            }
            if (!compareTime(curMax, localLast))
            { //local is later
                curMax = localLast;
               //maxIndex = i;
            }

        }
    }
    //the form of timstamp is like 2014-08-31 18:00:06.000
    //we use space to divide the date and the time
    // false for time2>time1(time1 erlier)
    bool compareTime(string time1, string time2)
    {
        time1 = time1.Replace('-', '/');
        time2 = time2.Replace('-', '/');
        System.DateTime t1;
        System.DateTime.TryParse(time1, out t1);
        System.DateTime t2;
        System.DateTime.TryParse(time2, out t2);
        int result = System.DateTime.Compare(t1, t2);
        if (result < 0) { //t1 is ealier
            return false;
        }//else
        return true;
    }
    // Here we need to update the scale and positions of important vertices in our line
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
    //Initialize we want to draw different lines for different individuals
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
            //Color color = ;
            colors[i] = color;
            lineRenderer.widthMultiplier = 30f;
            lineRenderer.material = new Material(Shader.Find("Standard"));
            lineRenderer.material.SetColor("_Color",color);

            IndividualBehavior id = reader.gp.individualBehaviors[i];
            int trackCount = id.Individualtracks.Count;//number of datapoints for each individual
            string[] locations = spawn_bird._LocationStrings[i];
            float[] heights = spawn_bird._HeightArray[i];
            Vector3[] vP = new Vector3[trackCount];
            lineRenderer.positionCount=trackCount;
            child.GetComponent<birdMovement>().firstTimestamp = id.Individualtracks[0].timestamp;
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
