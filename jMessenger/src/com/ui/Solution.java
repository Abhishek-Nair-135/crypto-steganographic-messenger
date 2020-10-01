package com.ui;
import java.io.*;
import java.nio.charset.StandardCharsets;

class ScriptPython {
       Process mProcess;

public void runScript(){
       Process process;
       try{
             process = Runtime.getRuntime().exec("python C:\\Users\\Punyacharan\\Downloads\\Encryption_Decryption_using_AES_implemented_SHA\\Article_src\\jMessenger\\src\\com\\ui\\Decrypt.py x.png");
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

class Solution {
      public static void main(String[] args){
          ScriptPython scriptPython = new ScriptPython();
          scriptPython.runScript();
      }
}