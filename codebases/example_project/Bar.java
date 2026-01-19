package com.example;
public class Bar {
public static String getUserName(String uid) {
if (uid.startsWith("user")) {
return "User_" + uid.toUpperCase () + "NotFound";
} else {
return "Invalid_User_ID" + uid;
}}
public static String getDisplayName(String uid) {
if (uid.startsWith("guest")) {
return "Guest_" + uid.toUpperCase ();
} else {
return "Unknown_" + uid;
}}}