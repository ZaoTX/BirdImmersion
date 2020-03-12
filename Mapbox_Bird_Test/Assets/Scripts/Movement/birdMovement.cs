using System.Collections;
using System.Collections.Generic;
using UnityEngine;
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
    //flying speed 
    public float speed; // it takes 1/speed s to fly between datapoints,
    //the local time
    public float t=0f;
    //whether the bird is ready to fly
    bool isok = false;
    //count where is the bird
    int count=0;
    //the whole number of datapoints
    int num;
    //Time difference
    //public float TimeDiff = 2f;
    Vector3 birdpos;
    // Start is called before the first frame update
    void Start()
    {
        initialize();

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
        int index = int.Parse(objectName);
        //this bird should be animated
        bird = spawned_individuals[index];
        positions = new Vector3[lineRenderer.positionCount];
        num=lineRenderer.GetPositions(positions);//get an array of positions
        birdpos = positions[0];
        /* check
         * if (num == lineRenderer.positionCount) {
            Debug.Log(positions[0]);
        }*/
    }
    // Update is called once per frame
    void Update()
    {
        speed = spawn.speed;
        if (bird.transform.position == positions[0]) {
            isok = true;// it's ready to do animation
        }
        if (isok)
        {
            if (count < num)
            {

                t += Time.deltaTime * speed;
                if (count + 1 == num)
                {//the next position is out of range
                    isok = false;
                    bird.transform.position = birdpos;
                    t = 0f;
                    //count = 0;
                    return;
                }
                Vector3 nextpos = positions[count + 1];
                
                bird.transform.position = Vector3.Lerp(birdpos, nextpos, t);
                bird.transform.LookAt(nextpos);
                if (t >= 1)//let the bird fly for the TimeDiff
                {
                    //we switch to next position
                    count++;
                    t = 0f;
                    birdpos = bird.transform.position;
                    if(count==num)
                    {
                        isok = false;
                        bird.transform.position = birdpos;
                        t = 0f;
                        //count = 0;
                        return;
                    }

                }

            }
        }
        
    }
}
