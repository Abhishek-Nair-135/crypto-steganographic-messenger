package com.ui;
import java.io.*;
import java.nio.charset.StandardCharsets;

import com.socket.Message;

class ScriptPython_encrypt {
       Process mProcess;

public void runScript(){
       Process process;
       try{
             process = Runtime.getRuntime().exec("python C:\\Users\\Punyacharan\\Downloads\\Encryption_Decryption_using_AES_implemented_SHA\\Article_src\\jMessenger\\src\\com\\ui\\Encrypt.py C:\\Users\\Punyacharan\\Downloads\\Encryption_Decryption_using_AES_implemented_SHA\\Article_src\\jMessenger\\src\\com\\ui\\sh.png \"This shit is crazy");
             mProcess = process;
       }catch(Exception e) {
          System.out.println("Exception Raised" + e.toString());
       }
       InputStream stdout = mProcess.getInputStream();
       BufferedReader reader = new BufferedReader(new InputStreamReader(stdout,StandardCharsets.UTF_8));
       String line;
       try{
          while((line = reader.readLine()) != null){
               System.out.println(line);
          }
       }catch(IOException e){
             System.out.println("Exception in reading output"+ e.toString());
       }
}
}

class Solution_encrypt {
      public static void main(String[] args){
          ScriptPython_encrypt scriptPython = new ScriptPython_encrypt();
          scriptPython.runScript();
      }
}