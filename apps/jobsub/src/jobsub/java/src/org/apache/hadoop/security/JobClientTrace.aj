// Licensed to Cloudera, Inc. under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  Cloudera, Inc. licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
package org.apache.hadoop.security;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.security.Credentials;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public aspect JobClientTrace {
  private static final Log LOG = LogFactory.getLog(JobClientTracer.class);

  JobClientTrace() {
    LOG.info("Hue job submission aspect loaded.");
  }

  RunningJob around(JobConf conf):
    call(RunningJob JobClient.submitJobInternal(JobConf)) && args(conf) {
    RunningJob ret = proceed(conf);
    JobClientTracer.getInstance().submittedJob(ret);
    return ret;
  }

  void around(Configuration conf, Credentials credentials):
    call(void JobClient.readTokensFromFiles(Configuration, Credentials)) && args(conf, credentials) {
    conf.set("mapreduce.job.credentials.binary", System.getenv("HADOOP_TOKEN_FILE_LOCATION"));
    conf.setBoolean("mapreduce.job.complete.cancel.delegation.tokens", false);
    proceed(conf, credentials);
  }
}
