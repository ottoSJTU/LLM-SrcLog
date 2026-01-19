package com.example;
import com.example.Bar;
public class Foo {
public void logSomething(String type) {
if ("ERROR".equals(type)) {
log.error(Bar.getUserName("0"));
} else {
log.fatal(Bar.getDisplayName("1"));
}}}