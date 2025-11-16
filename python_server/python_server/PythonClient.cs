// PythonClient.cs
using System;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class PythonClient : MonoBehaviour
{
    private TcpClient client;
    private NetworkStream stream;

    public string serverIP = "127.0.0.1";
    public int serverPort = 65432;

    void Start()
    {
        try
        {
            client = new TcpClient(serverIP, serverPort);
            stream = client.GetStream();
            Debug.Log("Connected to Python server");
        }
        catch (Exception e)
        {
            Debug.LogError("Socket error: " + e.Message);
        }
    }

    void Update()
    {
        if (stream != null && stream.DataAvailable)
        {
            byte[] buffer = new byte[1024];
            int len = stream.Read(buffer, 0, buffer.Length);
            string msg = Encoding.UTF8.GetString(buffer, 0, len);
            Debug.Log("Emotion from Python: " + msg);
            
            // Based on `msg`, you can change your scene, spawn objects etc.
            HandleEmotion(msg);
        }
    }

    private void HandleEmotion(string emotion)
    {
        // Example: react to emotion
        if (emotion == "peaceful")
        {
            // do something
            Debug.Log("Dream is peaceful");
        }
        else if (emotion == "anxious")
        {
            Debug.Log("Dream is anxious");
        }
        else if (emotion == "curious")
        {
            Debug.Log("Dream is curious");
        }
    }

    void OnDestroy()
    {
        if (stream != null) stream.Close();
        if (client != null) client.Close();
    }
}
