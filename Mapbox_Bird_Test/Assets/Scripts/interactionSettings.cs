using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Valve.VR;
using Mapbox.Unity.Map;
using Mapbox.Unity.Utilities;
public class interactionSettings : MonoBehaviour
{
    /* public Camera camera;
     public GameObject vrPlayer;
     bool VRActived;*/
    public GameObject vrPlayer;
    bool change;
    bool stop;
    public AbstractMap map;
    public float zoomingskip = 1f;
    public float cameraMove = 10f;
    public process processor;
    public line_gen lineGen;
    Vector3 PlayerPos;
    int playerHeight = 500;
    private void Start()
    {
        vrPlayer.transform.position = new Vector3(0, 0, 0);
        vrPlayer.transform.eulerAngles = new Vector3(0f, 0.0f, 0.0f);
        
        change = false;
    }
    void Update()
    {
        checkChangeView();//from overview to vr scene
        zoomin();//zoom in
        zoomout();//zoom out
        checkMapUpdate();//center button for map update
        OverviewMove();//Move the camera in overview mode
    }
    void checkChangeView()
    {
        if (SteamVR_Actions._default.ChangeView.GetStateUp(SteamVR_Input_Sources.RightHand))
        { //Both controller
            Debug.Log("menu pressed");
            change = !change;
        }
        if (!change)
        {//vr
            vrPlayer.transform.position = new Vector3(vrPlayer.transform.position.x, 10, vrPlayer.transform.position.z);
            vrPlayer.transform.eulerAngles = new Vector3(0.0f, 0.0f, 0.0f);
            processor.mode = false;
        }
        else
        {
            vrPlayer.transform.position = new Vector3(vrPlayer.transform.position.x, playerHeight, vrPlayer.transform.position.z);
            vrPlayer.transform.eulerAngles = new Vector3(90.0f, 0.0f, 0.0f);
            processor.mode = true;
        }
    }
    void zoomin()
    {
        if (SteamVR_Actions._default.ZoomingLevelUp.GetStateDown(SteamVR_Input_Sources.RightHand))
        { //Right controller
            Debug.Log("right pad north pressed");
            map.SetZoom(map.Zoom + zoomingskip);
            map.UpdateMap(map.Zoom);
            lineGen.needUpdate = true;
        }
    }
    void zoomout()
    {
        if (SteamVR_Actions._default.ZoomingLevelDown.GetStateDown(SteamVR_Input_Sources.RightHand))
        { //Right controller
            Debug.Log("right pad south pressed");
            map.SetZoom(map.Zoom - zoomingskip);
            map.UpdateMap(map.Zoom);
            lineGen.needUpdate = true;
        }
    }
    void checkMapUpdate()
    { //Only Update the View in VR scene
        if (SteamVR_Actions._default.Update.GetStateUp(SteamVR_Input_Sources.RightHand))
        { //Both controller
            Debug.Log("touchpad center pressed");
            MapBoxupdate();

        }

    }
    void MapBoxupdate()
    {
        var OldLatLon = Conversions.StringToLatLon(map._options.locationOptions.latitudeLongitude);

        //Debug.Log(PlayerPos);
        //PlayerPos = new Vector3(PlayerPos.x, 0, PlayerPos.z);
        PlayerPos = GameObject.FindGameObjectWithTag("Player").transform.position;
        var newMapPos = map.WorldToGeoPosition(PlayerPos);
        //Debug.Log(newMapPos);
        //PlayerPos = new Vector3(PlayerPos.x+20, 10, PlayerPos.z);

        //newMapPos = map.WorldToGeoPosition(PlayerPos);
        //Debug.Log(newMapPos);
        //Debug.Log(LatLon.GetType());
        if (OldLatLon != newMapPos)
        {
            map.UpdateMap(newMapPos, map.Zoom);
            if (processor.mode == false)
            {
                GameObject.FindGameObjectWithTag("Player").transform.position = new Vector3(0, 10, 0);
            }
            else
            {
                GameObject.FindGameObjectWithTag("Player").transform.position = new Vector3(0, playerHeight, 0);
            }
            lineGen.needUpdate = true;
        }
    }
    void OverviewMove()
    {
        if (processor.mode == true)
        {
            PlayerPos = GameObject.FindGameObjectWithTag("Player").transform.position;
            if (SteamVR_Actions._default.OverviewRight.GetStateUp(SteamVR_Input_Sources.LeftHand))
            {
                Debug.Log("left touchpad right pressed");
                GameObject.FindGameObjectWithTag("Player").transform.position = new Vector3(PlayerPos.x + cameraMove, 200, PlayerPos.z);
            }
            if (SteamVR_Actions._default.OverviewUp.GetStateUp(SteamVR_Input_Sources.LeftHand))
            {
                Debug.Log("left touchpad up pressed");
                GameObject.FindGameObjectWithTag("Player").transform.position = new Vector3(PlayerPos.x, 200, PlayerPos.z + cameraMove);
            }
            if (SteamVR_Actions._default.OverviewLeft.GetStateUp(SteamVR_Input_Sources.LeftHand))
            {
                Debug.Log("left touchpad left pressed");
                GameObject.FindGameObjectWithTag("Player").transform.position = new Vector3(PlayerPos.x - cameraMove, 200, PlayerPos.z);
            }
            if (SteamVR_Actions._default.OverviewDown.GetStateUp(SteamVR_Input_Sources.LeftHand))
            {
                Debug.Log("left touchpad down pressed");
                GameObject.FindGameObjectWithTag("Player").transform.position = new Vector3(PlayerPos.x, 200, PlayerPos.z - cameraMove);
            }
        }
    }

}
