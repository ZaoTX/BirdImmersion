using UnityEngine;
using UnityEngine.UI;
using System;
public class timelineController : MonoBehaviour
{
    public Transform timeline;
    public GameObject textIndicator;

    public GameObject dataManager;

    public GameObject polylineManager;
    float speed;
    double overallTime;
    public  double timeDiffSec;
    //float timeDiffSecFloat;
    DateTime tMin;
    DateTime tMax;
    
    [SerializeField] private double currentAmount;
    
    void Start()
    {
        
        speed = dataManager.GetComponent<process>().speed;
        string Min = polylineManager.GetComponent<line_gen>().curMin;
        Min = Min.Replace('-', '/');
        DateTime.TryParse(Min, out tMin);
        string Max = polylineManager.GetComponent<line_gen>().curMax;
        Max = Max.Replace('-', '/');
        DateTime.TryParse(Max, out tMax);
        TimeSpan TimeDiff = tMax-tMin;
        timeDiffSec = TimeDiff.TotalSeconds;
        //float timeDiffSecFloat = Convert.ToInt32(timeDiffSec);
        //check  
        //Debug.Log("Timeline"+timeDiffSecFloat);
    }
    // Update is called once per frame
    void Update()
    {
        speed = dataManager.GetComponent<process>().speed;
        string Min = polylineManager.GetComponent<line_gen>().curMin;
        Min = Min.Replace('-', '/');
        DateTime.TryParse(Min, out tMin);
        
        if (currentAmount < 100) {
            currentAmount += speed * Time.deltaTime/ timeDiffSec;
            overallTime = polylineManager.GetComponent<line_gen>().OverallTime;
            string textInhalt = tMin.AddSeconds(overallTime).ToString("yyyy-MM-dd HH:mm:ss");
            textIndicator.GetComponent<Text>().text = textInhalt;
        }
        timeline.GetComponent<Slider>().value = (float)currentAmount/ 100;
    }
}
