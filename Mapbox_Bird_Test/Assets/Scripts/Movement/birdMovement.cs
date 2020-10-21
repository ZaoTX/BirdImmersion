using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
/*
  This script is designed to automatically attached to 
  each trajectories under the polyline manager
     */
public class birdMovement : MonoBehaviour
{
    public Spawn_Bird spawn;
    LineRenderer lineRenderer;
    GameObject bird;
    Vector3[] positions;
    //flying overallSpeed 
    public double overallSpeed; // it takes 1/overallSpeed s to fly between datapoints,
    //the local time
    public double t=0;
    //whether the bird is ready to fly
    public  bool isok = false;
    //count where is the bird
    int count=0;
    //the whole number of datapoints
    int num;
    int index;
    //Time difference
    //public float TimeDiff = 2f;
    Vector3 birdpos;
    //if the time is ok for individual
    public bool canStart;
    public string firstTimestamp;
    public GameObject DataManager;
    public IndividualBehavior idb;
    double timeDiffSecDou;
    double multipler;
    Vector3 nextpos;
    // Start is called before the first frame update
    void Start()
    {
        initialize();
        canStart = false;

    }
    void initialize() {
        // find the spawn bird script
        spawn = GameObject.Find("mapbase").GetComponent<Spawn_Bird>();
        //get the linerenderer from this obj
        lineRenderer = transform.GetComponent<LineRenderer>();
        //get the list of birds
        List<GameObject> spawned_individuals = spawn.spawned_individuals;
        //get the name of the object(correspond to the index of spawned_individuals)
        string objectName = transform.name;
        index = int.Parse(objectName);
        //this bird should be animated
        bird = spawned_individuals[index];
        positions = new Vector3[lineRenderer.positionCount];
        num=lineRenderer.GetPositions(positions);//get an array of positions
        birdpos = positions[0];
        nextpos = positions[1];
        /* check
         * if (num == lineRenderer.positionCount) {
         *   Debug.Log(positions[0]);
         * }
         */
        //code below is to initialize a list information for each individual
        DataManager = GameObject.Find("DataManager");
        csvReader reader = DataManager.GetComponent<csvReader>();
        idb = reader.gp.individualBehaviors[index];
        Individual first = idb.Individualtracks[0];
        Individual second = idb.Individualtracks[1];
        overallSpeed = spawn.speed;
        //Debug.Log("OverallSpeed " + overallSpeed);
        string time1 = first.timestamp;
        string time2 = second.timestamp;
        DateTime t1;
        DateTime.TryParse(time1, out t1);
        DateTime t2;
        DateTime.TryParse(time2, out t2);
        TimeSpan TimeDiff = t2 - t1;
        double timeDiffSec = TimeDiff.TotalSeconds;
        //timeDiffSecDou = Convert.ToInt64(timeDiffSec);
        multipler = overallSpeed / timeDiffSec;
    }
    // Update is called once per frame
    void FixedUpdate()
    {

        overallSpeed = spawn.speed;
        /*if (canStart)
        {*/

            if (bird.transform.position == positions[0] && count < num - 1)
            {
                isok = true;// it's ready to do animation
            }
            if (isok)
            {
                //check for update the scene
                if (this.transform.parent.GetComponent<line_gen>().canUpdateModel )
                {
                    lineRenderer = transform.GetComponent<LineRenderer>();
                    positions = new Vector3[lineRenderer.positionCount];
                    lineRenderer.GetPositions(positions);

                    birdpos = positions[count];
                    bird.transform.position = new Vector3(birdpos.x, birdpos.y, birdpos.z);
                    nextpos = positions[count + 1];
                    this.transform.parent.GetComponent<line_gen>().canUpdateModel = false;
                }
                //check restart
                if (this.transform.parent.GetComponent<line_gen>().restart)
                {
                    count = 0;
                    initialize();

                    this.transform.parent.GetComponent<line_gen>().OverallTime = 0;
                    this.transform.parent.GetComponent<line_gen>().restart = false;
                    //this below is to ensure the restart when the animation is finished
                    bird.SetActive(true);
                    //enable the line
                    this.gameObject.SetActive(true);
                    isok = true;
                }
                //check out of range
                if (count == num )
                {//this position is out of range
                    //Debug.Log("The " + index + " in first if shoud be finished");
                    
                    bird.transform.position = new Vector3(positions[count].x, positions[count].y, positions[count].z);
                    isok = false;
                    //t = 0f;
                    //count = 0;
                    return;
                }
                
                if (t >= Math.Abs(1-0.0012*overallSpeed))
                {
                    //we switch to next position
                    count++;
                    if (count == num - 1)
                    {//the next position is out of range
                        Debug.Log("The " + index+" shoud be finished");
                        bird.SetActive(false);
                        //disable the line
                        this.gameObject.SetActive(false);
                        isok = false;
                        return;
                    }
                    //Here we want to calculate the time difference between this position and next position
                    Individual id = idb.Individualtracks[count];
                    Individual nextId = idb.Individualtracks[count + 1];

                    string time1 = id.timestamp;
                    string time2 = nextId.timestamp;
                    time1 = time1.Replace('-', '/');
                    time2 = time2.Replace('-', '/');

                    DateTime t1;
                    DateTime.TryParse(time1, out t1);
                    DateTime t2;
                    DateTime.TryParse(time2, out t2);
                    TimeSpan TimeDiff = t2 - t1;
                    double timeDiffSec = TimeDiff.TotalSeconds;
                    //timeDiffSecDou =double) Convert.ToInt64(timeDiffSec);

                    birdpos = nextpos;
                    nextpos = positions[count + 1];
                    multipler = overallSpeed / timeDiffSec;
                    //initialize the time t
                    t = 0f;

                    Debug.Log("The time we need is: " + (1 / multipler));

                }
                if(t<1) {
                    if (count == num - 1) {
                        return;
                    }
                    
                    bird.transform.LookAt(nextpos);
                    t += Time.deltaTime * multipler;
                    

                }
                bird.transform.position = Vector3.Lerp(birdpos, nextpos, (float)t);
                Debug.Log("However, the real t is: " + (float)t);



            }
       /* }
        else
        { //we check whether we can start
            GameObject parent = this.transform.parent.gameObject;//polylineManager
            double overallTime = parent.GetComponent<line_gen>().OverallTime;
            
            String Min = parent.GetComponent<line_gen>().curMin;
            Min=Min.Replace('-', '/');
            DateTime tMin;
            DateTime.TryParse(Min, out tMin);
            firstTimestamp = firstTimestamp.Replace('-', '/');
            DateTime tLocal;
            DateTime.TryParse(firstTimestamp, out tLocal);

            if(DateTime.Compare(tMin.AddSeconds(overallTime), tLocal)>0){
                    canStart = true;
            }

        }*/
        
    }
}
