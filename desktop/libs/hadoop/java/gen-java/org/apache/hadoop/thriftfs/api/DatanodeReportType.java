/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
package org.apache.hadoop.thriftfs.api;


import java.util.Map;
import java.util.HashMap;
import org.apache.thrift.TEnum;
public enum DatanodeReportType implements TEnum{
    ALL_DATANODES(1),
    LIVE_DATANODES(2),
    DEAD_DATANODES(3);

  private static final Map<Integer, DatanodeReportType> BY_VALUE = new HashMap<Integer,DatanodeReportType>() {{
    for(DatanodeReportType val : DatanodeReportType.values()) {
      put(val.getValue(), val);
    }
  }};

  private final int value;

  private DatanodeReportType(int value) {
    this.value = value;
  }

  /**
   * Get the integer value of this enum value, as defined in the Thrift IDL.
   */
  public int getValue() {
    return value;
  }

  /**
   * Find a the enum type by its integer value, as defined in the Thrift IDL.
   * @return null if the value is not found.
   */
  public static DatanodeReportType findByValue(int value) { 
    return BY_VALUE.get(value);
  }
}