using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Valve.VR;
using Mapbox.Unity.Map;
using Mapbox.Unity.Utilities;
using Mapbox.Unity.Map.TileProviders;//For map rangeAroundcenter
public class interactionSettings : MonoBehaviour
{
    /* public Camera camera;
     public GameObject vrPlayer;
     bool VRActived;*/
    public GameObject vrPlayer;
    public bool change;
    bool stop;
    public AbstractMap map;
    public float zoomingskip = 1f;
    public float cameraMove = 10f;
    public process processor;
    public line_gen lineGen;
    public Spawn_Bird spawn;
    public int count;
    List<GameObject> Model_List;// list of bird models
    Vector3 PlayerPos;
    int playerHeight = 300;
    Vector3 curPlayerPos;
    private void Start()
    {
        count = 0;
        vrPlayer.transform.position = new Vector3(0, 0, 0);
        vrPlayer.transform.eulerAngles = new Vector3(0f, 0.0f, 0.0f);
        spawn = map.GetComponent<Spawn_Bird>();
        Model_List = spawn.spawned_individuals;
        change = false;
    }
    void Update()
    {
        checkChangeView();//from overview to vr scene
        zoomin();//zoom in
        zoomout();//zoom out
        checkMapUpdate();//center button for map update
        ExtendMap();//Move the camera in overview mode
    }
    //Change the view of the player
    void checkChangeView()
    {
        if (SteamVR_Actions._default.ChangeView.GetStateUp(SteamVR_Input_Sources.RightHand))
        { //Right controller, the player can switch the individual to observe
            Debug.Log("menu pressed");
            //change = !change;
            count++;
            if (count >= Model_List.Count)
            {
                count = 0;
            }
        }
        if (SteamVR_Actions._default.ChangeView.GetStateUp(SteamVR_Input_Sources.LeftHand))
        { //Left controller, the player will fly with the individual
            Debug.Log("left menu pressed");
            processor.mode = !processor.mode;
            //get current individual's position
            curPlayerPos = new Vector3(Model_List[count].transform.position.x + 30, Model_List[count].transform.position.y + playerHeight, Model_List[count].transform.position.z + 30);

        }
        if (processor.mode)
        {
            //get the model and let player look at
            vrPlayer.transform.position = new Vector3(Model_List[count].transform.position.x+30, Model_List[count].transform.position.y+50, Model_List[count].transform.position.z+30);
            vrPlayer.transform.LookAt(Model_List[count].transform);
        }
        else
        {


            vrPlayer.transform.position = curPlayerPos;
            //vrPlayer.transform.LookAt(Model_List[count].transform);
            //processor.mode = true;
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
            /*if (processor.mode == false)
            {
                GameObject.FindGameObjectWithTag("Player").transform.position = new Vector3(0, 10, 0);
            }
            else
            {
                GameObject.FindGameObjectWithTag("Player").transform.position = new Vector3(0, playerHeight, 0);
            }*/
            lineGen.needUpdate = true;
        }
    }
    void ExtendMap()
    {
       
            PlayerPos = GameObject.FindGameObjectWithTag("Player").transform.position;
            if (SteamVR_Actions._default.OverviewRight.GetStateUp(SteamVR_Input_Sources.LeftHand))
            {
                Debug.Log("left touchpad right pressed");
                map.TileProvider.GetComponent<RangeTileProvider>()._rangeTileProviderOptions.east++;
            }
            if (SteamVR_Actions._default.OverviewUp.GetStateUp(SteamVR_Input_Sources.LeftHand))
            {
                Debug.Log("left touchpad up pressed");
                map.TileProvider.GetComponent<RangeTileProvider>()._rangeTileProviderOptions.north++; 
            }
            if (SteamVR_Actions._default.OverviewLeft.GetStateUp(SteamVR_Input_Sources.LeftHand))
            {
                Debug.Log("left touchpad left pressed");
                map.TileProvider.GetComponent<RangeTileProvider>()._rangeTileProviderOptions.west++;
            }
            if (SteamVR_Actions._default.OverviewDown.GetStateUp(SteamVR_Input_Sources.LeftHand))
            {
                Debug.Log("left touchpad down pressed");
                map.TileProvider.GetComponent<RangeTileProvider>()._rangeTileProviderOptions.south++;
            }
        
    }

}
