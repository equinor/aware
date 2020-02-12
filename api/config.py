import os


class Config:
    ignore_alert_list = os.getenv('IGNORE_ALERTS', '').split(',')
    flask_debug = os.getenv('FLASK_DEBUG', False)
    prometheus_api = os.getenv('PROMETHEUS_API', 'http://prometheus-operator-prometheus.monitoring:9090/api/v1/alerts')
    sensu_api = os.getenv('SENSU_API', 'http://mon01.prod.sdp.statoil.no:8080/api/core/v2/namespaces/default/events')
    sensu_key = os.getenv("SENSU_KEY", None)


    mockdata2 = r'''{"status":"success","data":{"alerts":[{"labels":{"alertname":"Watchdog","severity":"none"},"annotations":{"message":"This is an alert meant to ensure that the entire alerting pipeline is functional.\nThis alert is always firing, therefore it should always be firing in Alertmanager\nand always fire against a receiver. There are integrations with various notification\nmechanisms that send a notification when this alert is not firing. For example the\n\"DeadMansSnitch\" integration in PagerDuty.\n"},"state":"firing","activeAt":"2019-04-07T05:52:15.470372903Z","value":1}]}}
    '''
    mock_data = '''
    {"status":"success","data":{"alerts":[{"labels":{"alertname":"TargetDown","job":"apiserver","severity":"warning"},"annotations":{"message":"100% of the apiserver targets are down."},"state":"firing","activeAt":"2019-03-14T01:12:15.470372903Z","value":100},{"labels":{"alertname":"TargetDown","job":"kube-dns","severity":"warning"},"annotations":{"message":"100% of the kube-dns targets are down."},"state":"firing","activeAt":"2019-03-14T01:12:15.470372903Z","value":100},{"labels":{"alertname":"DeadMansSwitch","severity":"none"},"annotations":{"message":"This is a DeadMansSwitch meant to ensure that the entire alerting pipeline is functional."},"state":"firing","activeAt":"2019-03-14T01:12:15.470372903Z","value":1},{"labels":{"alertname":"KubePodCrashLooping","container":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"filebeat-hllqh","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Pod monitoring/filebeat-hllqh (filebeat) is restarting 0.00 times / second.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodcrashlooping"},"state":"firing","activeAt":"2019-03-14T01:14:49.362790506Z","value":0.003448275862068966},{"labels":{"alertname":"KubePodCrashLooping","container":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"filebeat-bg5hb","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Pod monitoring/filebeat-bg5hb (filebeat) is restarting 0.00 times / second.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodcrashlooping"},"state":"firing","activeAt":"2019-03-14T01:15:19.362790506Z","value":0.0022988505747126436},{"labels":{"alertname":"KubePodNotReady","namespace":"kube-system","pod":"oauth2-proxy-ks-6b9dd85456-s6dsg","severity":"critical"},"annotations":{"message":"Pod kube-system/oauth2-proxy-ks-6b9dd85456-s6dsg has been in a non-ready state for longer than an hour.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodnotready"},"state":"firing","activeAt":"2019-03-14T01:12:49.362790506Z","value":1},{"labels":{"alertname":"KubeDeploymentReplicasMismatch","deployment":"oauth2-proxy-ks","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"kube-system","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Deployment kube-system/oauth2-proxy-ks has not matched the expected number of replicas for longer than an hour.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedeploymentreplicasmismatch"},"state":"firing","activeAt":"2019-03-14T01:12:49.362790506Z","value":1},{"labels":{"alertname":"KubeDaemonSetRolloutStuck","daemonset":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Only 0% of the desired Pods of DaemonSet monitoring/filebeat are scheduled and ready.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedaemonsetrolloutstuck"},"state":"firing","activeAt":"2019-03-14T01:12:49.362790506Z","value":0},{"labels":{"alertname":"KubeJobCompletion","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","job_name":"elasticsearch-curator-1552611600","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"warning"},"annotations":{"message":"Job monitoring/elasticsearch-curator-1552611600 is taking more than one hour to complete.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubejobcompletion"},"state":"firing","activeAt":"2019-03-15T01:00:49.362790506Z","value":1},{"labels":{"alertname":"KubeJobFailed","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","job_name":"elasticsearch-curator-1552611600","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"warning"},"annotations":{"message":"Job monitoring/elasticsearch-curator-1552611600 failed to complete.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubejobfailed"},"state":"firing","activeAt":"2019-03-15T01:00:49.362790506Z","value":6},{"labels":{"alertname":"CPUThrottlingHigh","container_name":"config-reloader","namespace":"monitoring","pod_name":"alertmanager-prometheus-operator-alertmanager-0","severity":"warning"},"annotations":{"message":"33% throttling of CPU in namespace monitoring for container config-reloader in pod alertmanager-prometheus-operator-alertmanager-0.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh"},"state":"firing","activeAt":"2019-03-15T11:07:34.559334876Z","value":33.333333333333336},{"labels":{"alertname":"CPUThrottlingHigh","container_name":"rules-configmap-reloader","namespace":"monitoring","pod_name":"prometheus-prometheus-operator-prometheus-0","severity":"warning"},"annotations":{"message":"33% throttling of CPU in namespace monitoring for container rules-configmap-reloader in pod prometheus-prometheus-operator-prometheus-0.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh"},"state":"pending","activeAt":"2019-03-15T11:12:34.559334876Z","value":33.333333333333336},{"labels":{"alertname":"CPUThrottlingHigh","container_name":"prometheus-config-reloader","namespace":"monitoring","pod_name":"prometheus-prometheus-operator-prometheus-0","severity":"warning"},"annotations":{"message":"33% throttling of CPU in namespace monitoring for container prometheus-config-reloader in pod prometheus-prometheus-operator-prometheus-0.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh"},"state":"firing","activeAt":"2019-03-15T10:56:34.559334876Z","value":33.333333333333336},{"labels":{"alertname":"CPUThrottlingHigh","container_name":"heapster-nanny","namespace":"kube-system","pod_name":"heapster-5fb7488d97-l5mtl","severity":"warning"},"annotations":{"message":"25% throttling of CPU in namespace kube-system for container heapster-nanny in pod heapster-5fb7488d97-l5mtl.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh"},"state":"pending","activeAt":"2019-03-15T11:25:34.559334876Z","value":25.2},{"labels":{"alertname":"KubeAPIDown","severity":"critical"},"annotations":{"message":"KubeAPI has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapidown"},"state":"firing","activeAt":"2019-03-14T01:12:24.667662181Z","value":1},{"labels":{"alertname":"KubeControllerManagerDown","severity":"critical"},"annotations":{"message":"KubeControllerManager has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubecontrollermanagerdown"},"state":"firing","activeAt":"2019-03-14T01:12:24.667662181Z","value":1},{"labels":{"alertname":"KubeSchedulerDown","severity":"critical"},"annotations":{"message":"KubeScheduler has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeschedulerdown"},"state":"firing","activeAt":"2019-03-14T01:12:24.667662181Z","value":1},{"labels":{"alertname":"TargetDown","job":"apiserver","severity":"warning"},"annotations":{"description":"100% of apiserver targets are down.","summary":"Targets are down"},"state":"firing","activeAt":"2019-03-14T01:12:08.503964295Z","value":100},{"labels":{"alertname":"TargetDown","job":"kube-dns","severity":"warning"},"annotations":{"description":"100% of kube-dns targets are down.","summary":"Targets are down"},"state":"firing","activeAt":"2019-03-14T01:12:08.503964295Z","value":100},{"labels":{"alertname":"DeadMansSwitch","severity":"none"},"annotations":{"description":"This is a DeadMansSwitch meant to ensure that the entire Alerting pipeline is functional.","summary":"Alerting DeadMansSwitch"},"state":"firing","activeAt":"2019-03-14T01:12:08.503964295Z","value":1},{"labels":{"alertname":"CoreDNSDown","severity":"critical"},"annotations":{"message":"CoreDNS has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-corednsdown"},"state":"firing","activeAt":"2019-03-14T01:12:22.392757395Z","value":1},{"labels":{"alertname":"KubeAPIDown","severity":"critical"},"annotations":{"message":"KubeAPI has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapidown"},"state":"firing","activeAt":"2019-03-14T01:12:22.392757395Z","value":1},{"labels":{"alertname":"KubeControllerManagerDown","severity":"critical"},"annotations":{"message":"KubeControllerManager has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubecontrollermanagerdown"},"state":"firing","activeAt":"2019-03-14T01:12:22.392757395Z","value":1},{"labels":{"alertname":"KubeSchedulerDown","severity":"critical"},"annotations":{"message":"KubeScheduler has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeschedulerdown"},"state":"firing","activeAt":"2019-03-14T01:12:22.392757395Z","value":1},{"labels":{"alertname":"KubePodCrashLooping","container":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"filebeat-hllqh","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Pod monitoring/filebeat-hllqh (filebeat) is restarting 1.03 times / 5 minutes.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodcrashlooping"},"state":"firing","activeAt":"2019-03-14T01:14:47.743318242Z","value":1.0344827586206897},{"labels":{"alertname":"KubePodCrashLooping","container":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"filebeat-bg5hb","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Pod monitoring/filebeat-bg5hb (filebeat) is restarting 0.69 times / 5 minutes.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodcrashlooping"},"state":"firing","activeAt":"2019-03-14T01:15:17.743318242Z","value":0.6896551724137931},{"labels":{"alertname":"KubePodNotReady","namespace":"kube-system","pod":"oauth2-proxy-ks-6b9dd85456-s6dsg","severity":"critical"},"annotations":{"message":"Pod kube-system/oauth2-proxy-ks-6b9dd85456-s6dsg has been in a non-ready state for longer than an hour.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodnotready"},"state":"firing","activeAt":"2019-03-14T01:12:47.743318242Z","value":1},{"labels":{"alertname":"KubeDeploymentReplicasMismatch","deployment":"oauth2-proxy-ks","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"kube-system","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Deployment kube-system/oauth2-proxy-ks has not matched the expected number of replicas for longer than an hour.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedeploymentreplicasmismatch"},"state":"firing","activeAt":"2019-03-14T01:12:47.743318242Z","value":1},{"labels":{"alertname":"KubeDaemonSetRolloutStuck","daemonset":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Only 0% of the desired Pods of DaemonSet monitoring/filebeat are scheduled and ready.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedaemonsetrolloutstuck"},"state":"firing","activeAt":"2019-03-14T01:12:47.743318242Z","value":0},{"labels":{"alertname":"KubeJobCompletion","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","job_name":"elasticsearch-curator-1552611600","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"warning"},"annotations":{"message":"Job monitoring/elasticsearch-curator-1552611600 is taking more than one hour to complete.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubejobcompletion"},"state":"firing","activeAt":"2019-03-15T01:00:47.743318242Z","value":1},{"labels":{"alertname":"KubeJobFailed","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","job_name":"elasticsearch-curator-1552611600","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"warning"},"annotations":{"message":"Job monitoring/elasticsearch-curator-1552611600 failed to complete.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubejobfailed"},"state":"firing","activeAt":"2019-03-15T01:00:47.743318242Z","value":6}]}}
'''
    sensu_mock_data = '''[
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1137",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:c2:a3:23:ad:64",
              "addresses": [
                "10.36.34.80/21",
                "fe80::4c2:a3ff:fe23:ad64/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.dev.vlmtrc.statoil.no"
      ],
      "last_seen": 1581127506,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.dev.vlmtrc.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006458466,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1137",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:c2:a3:23:ad:64",
              "addresses": [
                "10.36.34.80/21",
                "fe80::4c2:a3ff:fe23:ad64/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.dev.vlmtrc.statoil.no"
      ],
      "last_seen": 1581127506,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.dev.vlmtrc.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004940645,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 55804 MiB (54.50% inode=95%);\n /dev 7915 MiB (100.00% inode=100%);\n| /=46584MiB;81910;92149;0;102388 /dev=0MiB;6332;7123;0;7915\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18568,
      "occurrences_watermark": 18568,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506655,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1137",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:c2:a3:23:ad:64",
              "addresses": [
                "10.36.34.80/21",
                "fe80::4c2:a3ff:fe23:ad64/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.dev.vlmtrc.statoil.no"
      ],
      "last_seen": 1581127506,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.dev.vlmtrc.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.350027945,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (app01.dev.vlmtrc.statoil.no) resolves to my IP (10.36.34.80)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507447,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1137",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:c2:a3:23:ad:64",
              "addresses": [
                "10.36.34.80/21",
                "fe80::4c2:a3ff:fe23:ad64/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.dev.vlmtrc.statoil.no"
      ],
      "last_seen": 1581507446,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.dev.vlmtrc.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507447,
      "history": [
        {
          "status": 0,
          "executed": 1581507046
        },
        {
          "status": 0,
          "executed": 1581507066
        },
        {
          "status": 0,
          "executed": 1581507086
        },
        {
          "status": 0,
          "executed": 1581507106
        },
        {
          "status": 0,
          "executed": 1581507126
        },
        {
          "status": 0,
          "executed": 1581507146
        },
        {
          "status": 0,
          "executed": 1581507166
        },
        {
          "status": 0,
          "executed": 1581507187
        },
        {
          "status": 0,
          "executed": 1581507206
        },
        {
          "status": 0,
          "executed": 1581507226
        },
        {
          "status": 0,
          "executed": 1581507247
        },
        {
          "status": 0,
          "executed": 1581507266
        },
        {
          "status": 0,
          "executed": 1581507286
        },
        {
          "status": 0,
          "executed": 1581507306
        },
        {
          "status": 0,
          "executed": 1581507326
        },
        {
          "status": 0,
          "executed": 1581507346
        },
        {
          "status": 0,
          "executed": 1581507366
        },
        {
          "status": 0,
          "executed": 1581507386
        },
        {
          "status": 0,
          "executed": 1581507406
        },
        {
          "status": 0,
          "executed": 1581507427
        },
        {
          "status": 0,
          "executed": 1581507447
        }
      ],
      "issued": 1581507447,
      "output": "Keepalive last sent from app01.dev.vlmtrc.statoil.no at 2020-02-12 11:37:26 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507447,
      "occurrences": 55708,
      "occurrences_watermark": 55708,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507424,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1137",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:c2:a3:23:ad:64",
              "addresses": [
                "10.36.34.80/21",
                "fe80::4c2:a3ff:fe23:ad64/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.dev.vlmtrc.statoil.no"
      ],
      "last_seen": 1581127506,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.dev.vlmtrc.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006868855,
      "executed": 1581507424,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506524
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506704
        },
        {
          "status": 0,
          "executed": 1581506764
        },
        {
          "status": 0,
          "executed": 1581506824
        },
        {
          "status": 0,
          "executed": 1581506884
        },
        {
          "status": 0,
          "executed": 1581506944
        },
        {
          "status": 0,
          "executed": 1581507004
        },
        {
          "status": 0,
          "executed": 1581507064
        },
        {
          "status": 0,
          "executed": 1581507124
        },
        {
          "status": 0,
          "executed": 1581507184
        },
        {
          "status": 0,
          "executed": 1581507244
        },
        {
          "status": 0,
          "executed": 1581507304
        },
        {
          "status": 0,
          "executed": 1581507364
        },
        {
          "status": 0,
          "executed": 1581507424
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.01, 0.02, 0.05|load1=0.010;80.000;90.000;0; load5=0.020;80.000;90.000;0; load15=0.050;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507424,
      "occurrences": 18567,
      "occurrences_watermark": 18567,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1137",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:c2:a3:23:ad:64",
              "addresses": [
                "10.36.34.80/21",
                "fe80::4c2:a3ff:fe23:ad64/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.dev.vlmtrc.statoil.no"
      ],
      "last_seen": 1581127506,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.dev.vlmtrc.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004439261,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 0% free (0 MB out of 0 MB) - Swap is either disabled, not present, or of zero size. |swap=0MB;0;0;0;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18568,
      "occurrences_watermark": 18568,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1089",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:ea:33:87:e3:66",
              "addresses": [
                "10.36.36.181/21",
                "fe80::4ea:33ff:fe87:e366/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:44:b6:27",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:44:b6:27",
              "addresses": null
            },
            {
              "name": "br-66ef7c940272",
              "mac": "02:42:e0:5c:1b:33",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-865551603f4e",
              "mac": "02:42:28:5c:b5:c2",
              "addresses": [
                "172.19.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:82:ba:f1:97",
              "addresses": [
                "172.17.0.1/16"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.prod.dh.statoil.no"
      ],
      "last_seen": 1580295807,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.prod.dh.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006684995,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1089",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:ea:33:87:e3:66",
              "addresses": [
                "10.36.36.181/21",
                "fe80::4ea:33ff:fe87:e366/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:44:b6:27",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:44:b6:27",
              "addresses": null
            },
            {
              "name": "br-66ef7c940272",
              "mac": "02:42:e0:5c:1b:33",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-865551603f4e",
              "mac": "02:42:28:5c:b5:c2",
              "addresses": [
                "172.19.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:82:ba:f1:97",
              "addresses": [
                "172.17.0.1/16"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.prod.dh.statoil.no"
      ],
      "last_seen": 1580295807,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.prod.dh.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004791596,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 82643 MiB (80.71% inode=93%);\n /dev 1855 MiB (100.00% inode=100%);\n| /=19745MiB;81910;92149;0;102388 /dev=0MiB;1484;1669;0;1855\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506655,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1089",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:ea:33:87:e3:66",
              "addresses": [
                "10.36.36.181/21",
                "fe80::4ea:33ff:fe87:e366/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:44:b6:27",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:44:b6:27",
              "addresses": null
            },
            {
              "name": "br-66ef7c940272",
              "mac": "02:42:e0:5c:1b:33",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-865551603f4e",
              "mac": "02:42:28:5c:b5:c2",
              "addresses": [
                "172.19.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:82:ba:f1:97",
              "addresses": [
                "172.17.0.1/16"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.prod.dh.statoil.no"
      ],
      "last_seen": 1580295807,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.prod.dh.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.332768411,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (app01.prod.dh.statoil.no) resolves to my IP (10.36.36.181)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507447,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1089",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:ea:33:87:e3:66",
              "addresses": [
                "10.36.36.181/21",
                "fe80::4ea:33ff:fe87:e366/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:44:b6:27",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:44:b6:27",
              "addresses": null
            },
            {
              "name": "br-66ef7c940272",
              "mac": "02:42:e0:5c:1b:33",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-865551603f4e",
              "mac": "02:42:28:5c:b5:c2",
              "addresses": [
                "172.19.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:82:ba:f1:97",
              "addresses": [
                "172.17.0.1/16"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.prod.dh.statoil.no"
      ],
      "last_seen": 1581507447,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.prod.dh.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507447,
      "history": [
        {
          "status": 0,
          "executed": 1581507047
        },
        {
          "status": 0,
          "executed": 1581507067
        },
        {
          "status": 0,
          "executed": 1581507087
        },
        {
          "status": 0,
          "executed": 1581507107
        },
        {
          "status": 0,
          "executed": 1581507127
        },
        {
          "status": 0,
          "executed": 1581507147
        },
        {
          "status": 0,
          "executed": 1581507167
        },
        {
          "status": 0,
          "executed": 1581507187
        },
        {
          "status": 0,
          "executed": 1581507207
        },
        {
          "status": 0,
          "executed": 1581507227
        },
        {
          "status": 0,
          "executed": 1581507247
        },
        {
          "status": 0,
          "executed": 1581507267
        },
        {
          "status": 0,
          "executed": 1581507287
        },
        {
          "status": 0,
          "executed": 1581507307
        },
        {
          "status": 0,
          "executed": 1581507327
        },
        {
          "status": 0,
          "executed": 1581507347
        },
        {
          "status": 0,
          "executed": 1581507367
        },
        {
          "status": 0,
          "executed": 1581507387
        },
        {
          "status": 0,
          "executed": 1581507407
        },
        {
          "status": 0,
          "executed": 1581507427
        },
        {
          "status": 0,
          "executed": 1581507447
        }
      ],
      "issued": 1581507447,
      "output": "Keepalive last sent from app01.prod.dh.statoil.no at 2020-02-12 11:37:27 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507447,
      "occurrences": 55710,
      "occurrences_watermark": 55710,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507424,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1089",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:ea:33:87:e3:66",
              "addresses": [
                "10.36.36.181/21",
                "fe80::4ea:33ff:fe87:e366/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:44:b6:27",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:44:b6:27",
              "addresses": null
            },
            {
              "name": "br-66ef7c940272",
              "mac": "02:42:e0:5c:1b:33",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-865551603f4e",
              "mac": "02:42:28:5c:b5:c2",
              "addresses": [
                "172.19.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:82:ba:f1:97",
              "addresses": [
                "172.17.0.1/16"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.prod.dh.statoil.no"
      ],
      "last_seen": 1580295807,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.prod.dh.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006759904,
      "executed": 1581507424,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506524
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506704
        },
        {
          "status": 0,
          "executed": 1581506764
        },
        {
          "status": 0,
          "executed": 1581506824
        },
        {
          "status": 0,
          "executed": 1581506884
        },
        {
          "status": 0,
          "executed": 1581506944
        },
        {
          "status": 0,
          "executed": 1581507004
        },
        {
          "status": 0,
          "executed": 1581507064
        },
        {
          "status": 0,
          "executed": 1581507124
        },
        {
          "status": 0,
          "executed": 1581507184
        },
        {
          "status": 0,
          "executed": 1581507244
        },
        {
          "status": 0,
          "executed": 1581507304
        },
        {
          "status": 0,
          "executed": 1581507364
        },
        {
          "status": 0,
          "executed": 1581507424
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.04, 0.04, 0.05|load1=0.040;80.000;90.000;0; load5=0.040;80.000;90.000;0; load15=0.050;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507424,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1089",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:ea:33:87:e3:66",
              "addresses": [
                "10.36.36.181/21",
                "fe80::4ea:33ff:fe87:e366/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:44:b6:27",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:44:b6:27",
              "addresses": null
            },
            {
              "name": "br-66ef7c940272",
              "mac": "02:42:e0:5c:1b:33",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-865551603f4e",
              "mac": "02:42:28:5c:b5:c2",
              "addresses": [
                "172.19.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:82:ba:f1:97",
              "addresses": [
                "172.17.0.1/16"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:app01.prod.dh.statoil.no"
      ],
      "last_seen": 1580295807,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "app01.prod.dh.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.00459426,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 95% free (1930 MB out of 2047 MB) |swap=1930MB;1023;409;0;2047\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1084",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:d5:67:78:1b:3a",
              "addresses": [
                "10.36.38.168/21",
                "fe80::4d5:67ff:fe78:1b3a/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:6d:b0:45",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:6d:b0:45",
              "addresses": null
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "backup",
        "entity:backup01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296061,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "backup01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006565573,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1084",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:d5:67:78:1b:3a",
              "addresses": [
                "10.36.38.168/21",
                "fe80::4d5:67ff:fe78:1b3a/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:6d:b0:45",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:6d:b0:45",
              "addresses": null
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "backup",
        "entity:backup01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296061,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "backup01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004587213,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 29027 MiB (56.70% inode=98%);\n /dev 3870 MiB (100.00% inode=100%);\n /zfs 1243798 MiB (47.10% inode=99%);\n| /=22160MiB;40950;46069;0;51188 /dev=0MiB;3096;3483;0;3870 /zfs=1396832MiB;2112504;2376567;0;2640630\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506655,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1084",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:d5:67:78:1b:3a",
              "addresses": [
                "10.36.38.168/21",
                "fe80::4d5:67ff:fe78:1b3a/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:6d:b0:45",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:6d:b0:45",
              "addresses": null
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "backup",
        "entity:backup01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296061,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "backup01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.406662351,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (backup01.prod.sdp.statoil.no) resolves to my IP (10.36.38.168)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507443,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1084",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:d5:67:78:1b:3a",
              "addresses": [
                "10.36.38.168/21",
                "fe80::4d5:67ff:fe78:1b3a/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:6d:b0:45",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:6d:b0:45",
              "addresses": null
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "backup",
        "entity:backup01.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507443,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "backup01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507443,
      "history": [
        {
          "status": 0,
          "executed": 1581507043
        },
        {
          "status": 0,
          "executed": 1581507063
        },
        {
          "status": 0,
          "executed": 1581507083
        },
        {
          "status": 0,
          "executed": 1581507103
        },
        {
          "status": 0,
          "executed": 1581507123
        },
        {
          "status": 0,
          "executed": 1581507143
        },
        {
          "status": 0,
          "executed": 1581507163
        },
        {
          "status": 0,
          "executed": 1581507183
        },
        {
          "status": 0,
          "executed": 1581507203
        },
        {
          "status": 0,
          "executed": 1581507223
        },
        {
          "status": 0,
          "executed": 1581507243
        },
        {
          "status": 0,
          "executed": 1581507263
        },
        {
          "status": 0,
          "executed": 1581507283
        },
        {
          "status": 0,
          "executed": 1581507303
        },
        {
          "status": 0,
          "executed": 1581507323
        },
        {
          "status": 0,
          "executed": 1581507343
        },
        {
          "status": 0,
          "executed": 1581507363
        },
        {
          "status": 0,
          "executed": 1581507383
        },
        {
          "status": 0,
          "executed": 1581507403
        },
        {
          "status": 0,
          "executed": 1581507423
        },
        {
          "status": 0,
          "executed": 1581507443
        }
      ],
      "issued": 1581507443,
      "output": "Keepalive last sent from backup01.prod.sdp.statoil.no at 2020-02-12 11:37:23 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507443,
      "occurrences": 55710,
      "occurrences_watermark": 55710,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507424,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1084",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:d5:67:78:1b:3a",
              "addresses": [
                "10.36.38.168/21",
                "fe80::4d5:67ff:fe78:1b3a/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:6d:b0:45",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:6d:b0:45",
              "addresses": null
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "backup",
        "entity:backup01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296061,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "backup01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006776299,
      "executed": 1581507424,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506524
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506704
        },
        {
          "status": 0,
          "executed": 1581506764
        },
        {
          "status": 0,
          "executed": 1581506824
        },
        {
          "status": 0,
          "executed": 1581506884
        },
        {
          "status": 0,
          "executed": 1581506944
        },
        {
          "status": 0,
          "executed": 1581507004
        },
        {
          "status": 0,
          "executed": 1581507064
        },
        {
          "status": 0,
          "executed": 1581507124
        },
        {
          "status": 0,
          "executed": 1581507184
        },
        {
          "status": 0,
          "executed": 1581507244
        },
        {
          "status": 0,
          "executed": 1581507304
        },
        {
          "status": 0,
          "executed": 1581507364
        },
        {
          "status": 0,
          "executed": 1581507424
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.09, 0.45, 0.85|load1=0.090;80.000;90.000;0; load5=0.450;80.000;90.000;0; load15=0.850;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507424,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1084",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:d5:67:78:1b:3a",
              "addresses": [
                "10.36.38.168/21",
                "fe80::4d5:67ff:fe78:1b3a/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:6d:b0:45",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:6d:b0:45",
              "addresses": null
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "backup",
        "entity:backup01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296061,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "backup01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004305866,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 100% free (11981 MB out of 11999 MB) |swap=11981MB;5999;2399;0;11999\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1049.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:80:1a",
              "addresses": [
                "10.217.112.50/22",
                "fe80::250:56ff:fea2:801a/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:4b:70:76:3d",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:4bff:fe70:763d/64"
              ]
            },
            {
              "name": "br-df4089c8c3b9",
              "mac": "02:42:44:c2:2f:43",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:44ff:fec2:2f43/64"
              ]
            },
            {
              "name": "br-e866b3312b65",
              "mac": "02:42:17:77:fd:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:17ff:fe77:fd1c/64"
              ]
            },
            {
              "name": "br-065210aa80b7",
              "mac": "02:42:0c:00:f2:26",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:cff:fe00:f226/64"
              ]
            },
            {
              "name": "br-b3cf0f7f081a",
              "mac": "02:42:70:f3:e1:cf",
              "addresses": [
                "172.28.0.1/16",
                "fe80::42:70ff:fef3:e1cf/64"
              ]
            },
            {
              "name": "vethd370675",
              "mac": "46:9f:4a:77:26:b9",
              "addresses": [
                "fe80::449f:4aff:fe77:26b9/64"
              ]
            },
            {
              "name": "br-ccccf3006860",
              "mac": "02:42:f4:dd:91:af",
              "addresses": [
                "192.168.96.1/20",
                "fe80::42:f4ff:fedd:91af/64"
              ]
            },
            {
              "name": "veth079efc9",
              "mac": "f2:e9:cc:c0:3c:45",
              "addresses": [
                "fe80::f0e9:ccff:fec0:3c45/64"
              ]
            },
            {
              "name": "br-de04a0c1512d",
              "mac": "02:42:1d:8c:a4:ce",
              "addresses": [
                "172.26.0.1/16",
                "fe80::42:1dff:fe8c:a4ce/64"
              ]
            },
            {
              "name": "veth11ade1e",
              "mac": "c2:0b:3f:69:51:57",
              "addresses": [
                "fe80::c00b:3fff:fe69:5157/64"
              ]
            },
            {
              "name": "br-b222c3393efb",
              "mac": "02:42:35:b8:34:4a",
              "addresses": [
                "192.168.32.1/20",
                "fe80::42:35ff:feb8:344a/64"
              ]
            },
            {
              "name": "vethb618ec0",
              "mac": "72:65:c9:44:68:cb",
              "addresses": [
                "fe80::7065:c9ff:fe44:68cb/64"
              ]
            },
            {
              "name": "br-db776b07584f",
              "mac": "02:42:58:19:ef:78",
              "addresses": [
                "192.168.0.1/20",
                "fe80::42:58ff:fe19:ef78/64"
              ]
            },
            {
              "name": "veth7a417ca",
              "mac": "d6:37:0d:1f:87:77",
              "addresses": [
                "fe80::d437:dff:fe1f:8777/64"
              ]
            },
            {
              "name": "veth618ce85",
              "mac": "72:d4:97:b8:94:2e",
              "addresses": [
                "fe80::70d4:97ff:feb8:942e/64"
              ]
            },
            {
              "name": "veth86f4d93",
              "mac": "86:29:77:a4:01:e1",
              "addresses": [
                "fe80::8429:77ff:fea4:1e1/64"
              ]
            },
            {
              "name": "veth01cea04",
              "mac": "aa:4e:d1:8e:17:dd",
              "addresses": [
                "fe80::a84e:d1ff:fe8e:17dd/64"
              ]
            },
            {
              "name": "vethe29c7c6",
              "mac": "be:a4:77:9e:45:35",
              "addresses": [
                "fe80::bca4:77ff:fe9e:4535/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:bld01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296802,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "bld01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.0"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006559982,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 617,
      "occurrences_watermark": 617,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1049.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:80:1a",
              "addresses": [
                "10.217.112.50/22",
                "fe80::250:56ff:fea2:801a/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:4b:70:76:3d",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:4bff:fe70:763d/64"
              ]
            },
            {
              "name": "br-df4089c8c3b9",
              "mac": "02:42:44:c2:2f:43",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:44ff:fec2:2f43/64"
              ]
            },
            {
              "name": "br-e866b3312b65",
              "mac": "02:42:17:77:fd:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:17ff:fe77:fd1c/64"
              ]
            },
            {
              "name": "br-065210aa80b7",
              "mac": "02:42:0c:00:f2:26",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:cff:fe00:f226/64"
              ]
            },
            {
              "name": "br-b3cf0f7f081a",
              "mac": "02:42:70:f3:e1:cf",
              "addresses": [
                "172.28.0.1/16",
                "fe80::42:70ff:fef3:e1cf/64"
              ]
            },
            {
              "name": "vethd370675",
              "mac": "46:9f:4a:77:26:b9",
              "addresses": [
                "fe80::449f:4aff:fe77:26b9/64"
              ]
            },
            {
              "name": "br-ccccf3006860",
              "mac": "02:42:f4:dd:91:af",
              "addresses": [
                "192.168.96.1/20",
                "fe80::42:f4ff:fedd:91af/64"
              ]
            },
            {
              "name": "veth079efc9",
              "mac": "f2:e9:cc:c0:3c:45",
              "addresses": [
                "fe80::f0e9:ccff:fec0:3c45/64"
              ]
            },
            {
              "name": "br-de04a0c1512d",
              "mac": "02:42:1d:8c:a4:ce",
              "addresses": [
                "172.26.0.1/16",
                "fe80::42:1dff:fe8c:a4ce/64"
              ]
            },
            {
              "name": "veth11ade1e",
              "mac": "c2:0b:3f:69:51:57",
              "addresses": [
                "fe80::c00b:3fff:fe69:5157/64"
              ]
            },
            {
              "name": "br-b222c3393efb",
              "mac": "02:42:35:b8:34:4a",
              "addresses": [
                "192.168.32.1/20",
                "fe80::42:35ff:feb8:344a/64"
              ]
            },
            {
              "name": "vethb618ec0",
              "mac": "72:65:c9:44:68:cb",
              "addresses": [
                "fe80::7065:c9ff:fe44:68cb/64"
              ]
            },
            {
              "name": "br-db776b07584f",
              "mac": "02:42:58:19:ef:78",
              "addresses": [
                "192.168.0.1/20",
                "fe80::42:58ff:fe19:ef78/64"
              ]
            },
            {
              "name": "veth7a417ca",
              "mac": "d6:37:0d:1f:87:77",
              "addresses": [
                "fe80::d437:dff:fe1f:8777/64"
              ]
            },
            {
              "name": "veth618ce85",
              "mac": "72:d4:97:b8:94:2e",
              "addresses": [
                "fe80::70d4:97ff:feb8:942e/64"
              ]
            },
            {
              "name": "veth86f4d93",
              "mac": "86:29:77:a4:01:e1",
              "addresses": [
                "fe80::8429:77ff:fea4:1e1/64"
              ]
            },
            {
              "name": "veth01cea04",
              "mac": "aa:4e:d1:8e:17:dd",
              "addresses": [
                "fe80::a84e:d1ff:fe8e:17dd/64"
              ]
            },
            {
              "name": "vethe29c7c6",
              "mac": "be:a4:77:9e:45:35",
              "addresses": [
                "fe80::bca4:77ff:fe9e:4535/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:bld01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296802,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "bld01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.0"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006571804,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 178252 MiB (64.64% inode=99%);\n /dev 3896 MiB (100.00% inode=100%);\n /boot 281 MiB (62.93% inode=100%);\n /tmp 8149 MiB (99.60% inode=100%);\n /var 5091 MiB (62.22% inode=100%);\n| /=97476MiB;220583;248156;0;275729 /dev=0MiB;3116;3506;0;3896 /boot=165MiB;380;428;0;476 /tmp=32MiB;6545;7363;0;8182 /var=3090MiB;6545;7363;0;8182\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18556,
      "occurrences_watermark": 18556,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506657,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1049.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:80:1a",
              "addresses": [
                "10.217.112.50/22",
                "fe80::250:56ff:fea2:801a/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:4b:70:76:3d",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:4bff:fe70:763d/64"
              ]
            },
            {
              "name": "br-df4089c8c3b9",
              "mac": "02:42:44:c2:2f:43",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:44ff:fec2:2f43/64"
              ]
            },
            {
              "name": "br-e866b3312b65",
              "mac": "02:42:17:77:fd:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:17ff:fe77:fd1c/64"
              ]
            },
            {
              "name": "br-065210aa80b7",
              "mac": "02:42:0c:00:f2:26",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:cff:fe00:f226/64"
              ]
            },
            {
              "name": "br-b3cf0f7f081a",
              "mac": "02:42:70:f3:e1:cf",
              "addresses": [
                "172.28.0.1/16",
                "fe80::42:70ff:fef3:e1cf/64"
              ]
            },
            {
              "name": "vethd370675",
              "mac": "46:9f:4a:77:26:b9",
              "addresses": [
                "fe80::449f:4aff:fe77:26b9/64"
              ]
            },
            {
              "name": "br-ccccf3006860",
              "mac": "02:42:f4:dd:91:af",
              "addresses": [
                "192.168.96.1/20",
                "fe80::42:f4ff:fedd:91af/64"
              ]
            },
            {
              "name": "veth079efc9",
              "mac": "f2:e9:cc:c0:3c:45",
              "addresses": [
                "fe80::f0e9:ccff:fec0:3c45/64"
              ]
            },
            {
              "name": "br-de04a0c1512d",
              "mac": "02:42:1d:8c:a4:ce",
              "addresses": [
                "172.26.0.1/16",
                "fe80::42:1dff:fe8c:a4ce/64"
              ]
            },
            {
              "name": "veth11ade1e",
              "mac": "c2:0b:3f:69:51:57",
              "addresses": [
                "fe80::c00b:3fff:fe69:5157/64"
              ]
            },
            {
              "name": "br-b222c3393efb",
              "mac": "02:42:35:b8:34:4a",
              "addresses": [
                "192.168.32.1/20",
                "fe80::42:35ff:feb8:344a/64"
              ]
            },
            {
              "name": "vethb618ec0",
              "mac": "72:65:c9:44:68:cb",
              "addresses": [
                "fe80::7065:c9ff:fe44:68cb/64"
              ]
            },
            {
              "name": "br-db776b07584f",
              "mac": "02:42:58:19:ef:78",
              "addresses": [
                "192.168.0.1/20",
                "fe80::42:58ff:fe19:ef78/64"
              ]
            },
            {
              "name": "veth7a417ca",
              "mac": "d6:37:0d:1f:87:77",
              "addresses": [
                "fe80::d437:dff:fe1f:8777/64"
              ]
            },
            {
              "name": "veth618ce85",
              "mac": "72:d4:97:b8:94:2e",
              "addresses": [
                "fe80::70d4:97ff:feb8:942e/64"
              ]
            },
            {
              "name": "veth86f4d93",
              "mac": "86:29:77:a4:01:e1",
              "addresses": [
                "fe80::8429:77ff:fea4:1e1/64"
              ]
            },
            {
              "name": "veth01cea04",
              "mac": "aa:4e:d1:8e:17:dd",
              "addresses": [
                "fe80::a84e:d1ff:fe8e:17dd/64"
              ]
            },
            {
              "name": "vethe29c7c6",
              "mac": "be:a4:77:9e:45:35",
              "addresses": [
                "fe80::bca4:77ff:fe9e:4535/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:bld01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296802,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "bld01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.0"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 2.315210807,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (bld01.prod.sdp.statoil.no) resolves to my IP (10.217.112.50)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507440,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1049.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:80:1a",
              "addresses": [
                "10.217.112.50/22",
                "fe80::250:56ff:fea2:801a/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:4b:70:76:3d",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:4bff:fe70:763d/64"
              ]
            },
            {
              "name": "br-df4089c8c3b9",
              "mac": "02:42:44:c2:2f:43",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:44ff:fec2:2f43/64"
              ]
            },
            {
              "name": "br-e866b3312b65",
              "mac": "02:42:17:77:fd:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:17ff:fe77:fd1c/64"
              ]
            },
            {
              "name": "br-065210aa80b7",
              "mac": "02:42:0c:00:f2:26",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:cff:fe00:f226/64"
              ]
            },
            {
              "name": "br-b3cf0f7f081a",
              "mac": "02:42:70:f3:e1:cf",
              "addresses": [
                "172.28.0.1/16",
                "fe80::42:70ff:fef3:e1cf/64"
              ]
            },
            {
              "name": "vethd370675",
              "mac": "46:9f:4a:77:26:b9",
              "addresses": [
                "fe80::449f:4aff:fe77:26b9/64"
              ]
            },
            {
              "name": "br-ccccf3006860",
              "mac": "02:42:f4:dd:91:af",
              "addresses": [
                "192.168.96.1/20",
                "fe80::42:f4ff:fedd:91af/64"
              ]
            },
            {
              "name": "veth079efc9",
              "mac": "f2:e9:cc:c0:3c:45",
              "addresses": [
                "fe80::f0e9:ccff:fec0:3c45/64"
              ]
            },
            {
              "name": "br-de04a0c1512d",
              "mac": "02:42:1d:8c:a4:ce",
              "addresses": [
                "172.26.0.1/16",
                "fe80::42:1dff:fe8c:a4ce/64"
              ]
            },
            {
              "name": "veth11ade1e",
              "mac": "c2:0b:3f:69:51:57",
              "addresses": [
                "fe80::c00b:3fff:fe69:5157/64"
              ]
            },
            {
              "name": "br-b222c3393efb",
              "mac": "02:42:35:b8:34:4a",
              "addresses": [
                "192.168.32.1/20",
                "fe80::42:35ff:feb8:344a/64"
              ]
            },
            {
              "name": "vethb618ec0",
              "mac": "72:65:c9:44:68:cb",
              "addresses": [
                "fe80::7065:c9ff:fe44:68cb/64"
              ]
            },
            {
              "name": "br-db776b07584f",
              "mac": "02:42:58:19:ef:78",
              "addresses": [
                "192.168.0.1/20",
                "fe80::42:58ff:fe19:ef78/64"
              ]
            },
            {
              "name": "veth7a417ca",
              "mac": "d6:37:0d:1f:87:77",
              "addresses": [
                "fe80::d437:dff:fe1f:8777/64"
              ]
            },
            {
              "name": "veth618ce85",
              "mac": "72:d4:97:b8:94:2e",
              "addresses": [
                "fe80::70d4:97ff:feb8:942e/64"
              ]
            },
            {
              "name": "veth86f4d93",
              "mac": "86:29:77:a4:01:e1",
              "addresses": [
                "fe80::8429:77ff:fea4:1e1/64"
              ]
            },
            {
              "name": "veth01cea04",
              "mac": "aa:4e:d1:8e:17:dd",
              "addresses": [
                "fe80::a84e:d1ff:fe8e:17dd/64"
              ]
            },
            {
              "name": "vethe29c7c6",
              "mac": "be:a4:77:9e:45:35",
              "addresses": [
                "fe80::bca4:77ff:fe9e:4535/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:bld01.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507440,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "bld01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.0"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507440,
      "history": [
        {
          "status": 0,
          "executed": 1581507041
        },
        {
          "status": 0,
          "executed": 1581507060
        },
        {
          "status": 0,
          "executed": 1581507081
        },
        {
          "status": 0,
          "executed": 1581507101
        },
        {
          "status": 0,
          "executed": 1581507121
        },
        {
          "status": 0,
          "executed": 1581507140
        },
        {
          "status": 0,
          "executed": 1581507161
        },
        {
          "status": 0,
          "executed": 1581507181
        },
        {
          "status": 0,
          "executed": 1581507201
        },
        {
          "status": 0,
          "executed": 1581507221
        },
        {
          "status": 0,
          "executed": 1581507241
        },
        {
          "status": 0,
          "executed": 1581507260
        },
        {
          "status": 0,
          "executed": 1581507281
        },
        {
          "status": 0,
          "executed": 1581507300
        },
        {
          "status": 0,
          "executed": 1581507321
        },
        {
          "status": 0,
          "executed": 1581507341
        },
        {
          "status": 0,
          "executed": 1581507360
        },
        {
          "status": 0,
          "executed": 1581507380
        },
        {
          "status": 0,
          "executed": 1581507401
        },
        {
          "status": 0,
          "executed": 1581507420
        },
        {
          "status": 0,
          "executed": 1581507440
        }
      ],
      "issued": 1581507440,
      "output": "Keepalive last sent from bld01.prod.sdp.statoil.no at 2020-02-12 11:37:20 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507440,
      "occurrences": 55693,
      "occurrences_watermark": 55693,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507425,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1049.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:80:1a",
              "addresses": [
                "10.217.112.50/22",
                "fe80::250:56ff:fea2:801a/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:4b:70:76:3d",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:4bff:fe70:763d/64"
              ]
            },
            {
              "name": "br-df4089c8c3b9",
              "mac": "02:42:44:c2:2f:43",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:44ff:fec2:2f43/64"
              ]
            },
            {
              "name": "br-e866b3312b65",
              "mac": "02:42:17:77:fd:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:17ff:fe77:fd1c/64"
              ]
            },
            {
              "name": "br-065210aa80b7",
              "mac": "02:42:0c:00:f2:26",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:cff:fe00:f226/64"
              ]
            },
            {
              "name": "br-b3cf0f7f081a",
              "mac": "02:42:70:f3:e1:cf",
              "addresses": [
                "172.28.0.1/16",
                "fe80::42:70ff:fef3:e1cf/64"
              ]
            },
            {
              "name": "vethd370675",
              "mac": "46:9f:4a:77:26:b9",
              "addresses": [
                "fe80::449f:4aff:fe77:26b9/64"
              ]
            },
            {
              "name": "br-ccccf3006860",
              "mac": "02:42:f4:dd:91:af",
              "addresses": [
                "192.168.96.1/20",
                "fe80::42:f4ff:fedd:91af/64"
              ]
            },
            {
              "name": "veth079efc9",
              "mac": "f2:e9:cc:c0:3c:45",
              "addresses": [
                "fe80::f0e9:ccff:fec0:3c45/64"
              ]
            },
            {
              "name": "br-de04a0c1512d",
              "mac": "02:42:1d:8c:a4:ce",
              "addresses": [
                "172.26.0.1/16",
                "fe80::42:1dff:fe8c:a4ce/64"
              ]
            },
            {
              "name": "veth11ade1e",
              "mac": "c2:0b:3f:69:51:57",
              "addresses": [
                "fe80::c00b:3fff:fe69:5157/64"
              ]
            },
            {
              "name": "br-b222c3393efb",
              "mac": "02:42:35:b8:34:4a",
              "addresses": [
                "192.168.32.1/20",
                "fe80::42:35ff:feb8:344a/64"
              ]
            },
            {
              "name": "vethb618ec0",
              "mac": "72:65:c9:44:68:cb",
              "addresses": [
                "fe80::7065:c9ff:fe44:68cb/64"
              ]
            },
            {
              "name": "br-db776b07584f",
              "mac": "02:42:58:19:ef:78",
              "addresses": [
                "192.168.0.1/20",
                "fe80::42:58ff:fe19:ef78/64"
              ]
            },
            {
              "name": "veth7a417ca",
              "mac": "d6:37:0d:1f:87:77",
              "addresses": [
                "fe80::d437:dff:fe1f:8777/64"
              ]
            },
            {
              "name": "veth618ce85",
              "mac": "72:d4:97:b8:94:2e",
              "addresses": [
                "fe80::70d4:97ff:feb8:942e/64"
              ]
            },
            {
              "name": "veth86f4d93",
              "mac": "86:29:77:a4:01:e1",
              "addresses": [
                "fe80::8429:77ff:fea4:1e1/64"
              ]
            },
            {
              "name": "veth01cea04",
              "mac": "aa:4e:d1:8e:17:dd",
              "addresses": [
                "fe80::a84e:d1ff:fe8e:17dd/64"
              ]
            },
            {
              "name": "vethe29c7c6",
              "mac": "be:a4:77:9e:45:35",
              "addresses": [
                "fe80::bca4:77ff:fe9e:4535/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:bld01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296802,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "bld01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.0"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.010264841,
      "executed": 1581507425,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506525
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506705
        },
        {
          "status": 0,
          "executed": 1581506765
        },
        {
          "status": 0,
          "executed": 1581506825
        },
        {
          "status": 0,
          "executed": 1581506885
        },
        {
          "status": 0,
          "executed": 1581506945
        },
        {
          "status": 0,
          "executed": 1581507005
        },
        {
          "status": 0,
          "executed": 1581507065
        },
        {
          "status": 0,
          "executed": 1581507125
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507365
        },
        {
          "status": 0,
          "executed": 1581507425
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.04, 0.08, 0.16|load1=0.040;80.000;90.000;0; load5=0.080;80.000;90.000;0; load15=0.160;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507425,
      "occurrences": 18559,
      "occurrences_watermark": 18559,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1049.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:80:1a",
              "addresses": [
                "10.217.112.50/22",
                "fe80::250:56ff:fea2:801a/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:4b:70:76:3d",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:4bff:fe70:763d/64"
              ]
            },
            {
              "name": "br-df4089c8c3b9",
              "mac": "02:42:44:c2:2f:43",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:44ff:fec2:2f43/64"
              ]
            },
            {
              "name": "br-e866b3312b65",
              "mac": "02:42:17:77:fd:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:17ff:fe77:fd1c/64"
              ]
            },
            {
              "name": "br-065210aa80b7",
              "mac": "02:42:0c:00:f2:26",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:cff:fe00:f226/64"
              ]
            },
            {
              "name": "br-b3cf0f7f081a",
              "mac": "02:42:70:f3:e1:cf",
              "addresses": [
                "172.28.0.1/16",
                "fe80::42:70ff:fef3:e1cf/64"
              ]
            },
            {
              "name": "vethd370675",
              "mac": "46:9f:4a:77:26:b9",
              "addresses": [
                "fe80::449f:4aff:fe77:26b9/64"
              ]
            },
            {
              "name": "br-ccccf3006860",
              "mac": "02:42:f4:dd:91:af",
              "addresses": [
                "192.168.96.1/20",
                "fe80::42:f4ff:fedd:91af/64"
              ]
            },
            {
              "name": "veth079efc9",
              "mac": "f2:e9:cc:c0:3c:45",
              "addresses": [
                "fe80::f0e9:ccff:fec0:3c45/64"
              ]
            },
            {
              "name": "br-de04a0c1512d",
              "mac": "02:42:1d:8c:a4:ce",
              "addresses": [
                "172.26.0.1/16",
                "fe80::42:1dff:fe8c:a4ce/64"
              ]
            },
            {
              "name": "veth11ade1e",
              "mac": "c2:0b:3f:69:51:57",
              "addresses": [
                "fe80::c00b:3fff:fe69:5157/64"
              ]
            },
            {
              "name": "br-b222c3393efb",
              "mac": "02:42:35:b8:34:4a",
              "addresses": [
                "192.168.32.1/20",
                "fe80::42:35ff:feb8:344a/64"
              ]
            },
            {
              "name": "vethb618ec0",
              "mac": "72:65:c9:44:68:cb",
              "addresses": [
                "fe80::7065:c9ff:fe44:68cb/64"
              ]
            },
            {
              "name": "br-db776b07584f",
              "mac": "02:42:58:19:ef:78",
              "addresses": [
                "192.168.0.1/20",
                "fe80::42:58ff:fe19:ef78/64"
              ]
            },
            {
              "name": "veth7a417ca",
              "mac": "d6:37:0d:1f:87:77",
              "addresses": [
                "fe80::d437:dff:fe1f:8777/64"
              ]
            },
            {
              "name": "veth618ce85",
              "mac": "72:d4:97:b8:94:2e",
              "addresses": [
                "fe80::70d4:97ff:feb8:942e/64"
              ]
            },
            {
              "name": "veth86f4d93",
              "mac": "86:29:77:a4:01:e1",
              "addresses": [
                "fe80::8429:77ff:fea4:1e1/64"
              ]
            },
            {
              "name": "veth01cea04",
              "mac": "aa:4e:d1:8e:17:dd",
              "addresses": [
                "fe80::a84e:d1ff:fe8e:17dd/64"
              ]
            },
            {
              "name": "vethe29c7c6",
              "mac": "be:a4:77:9e:45:35",
              "addresses": [
                "fe80::bca4:77ff:fe9e:4535/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:bld01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296802,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "bld01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.0"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004337968,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 91% free (7397 MB out of 8191 MB) |swap=7397MB;4095;1638;0;8191\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18559,
      "occurrences_watermark": 18559,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1046",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:18:51:43:9c:f0",
              "addresses": [
                "10.36.37.238/21",
                "fe80::418:51ff:fe43:9cf0/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:1f:93:02",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:1f:93:02",
              "addresses": null
            },
            {
              "name": "br-956930c48ea1",
              "mac": "02:42:d8:e1:b5:46",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:d8ff:fee1:b546/64"
              ]
            },
            {
              "name": "br-de142f048307",
              "mac": "02:42:17:82:cc:47",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-5a5cf4fd42a3",
              "mac": "02:42:c3:7c:1e:0c",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:49:73:17:fe",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethab6da56",
              "mac": "ce:42:92:6e:07:51",
              "addresses": [
                "fe80::cc42:92ff:fe6e:751/64"
              ]
            },
            {
              "name": "vetha8b8454",
              "mac": "a6:fc:d8:fb:06:fa",
              "addresses": [
                "fe80::a4fc:d8ff:fefb:6fa/64"
              ]
            },
            {
              "name": "veth705ec95",
              "mac": "ce:57:6d:d4:64:51",
              "addresses": [
                "fe80::cc57:6dff:fed4:6451/64"
              ]
            },
            {
              "name": "veth184536b",
              "mac": "f6:34:d7:5d:b8:18",
              "addresses": [
                "fe80::f434:d7ff:fe5d:b818/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:elk01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580295845,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "elk01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.008257333,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1046",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:18:51:43:9c:f0",
              "addresses": [
                "10.36.37.238/21",
                "fe80::418:51ff:fe43:9cf0/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:1f:93:02",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:1f:93:02",
              "addresses": null
            },
            {
              "name": "br-956930c48ea1",
              "mac": "02:42:d8:e1:b5:46",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:d8ff:fee1:b546/64"
              ]
            },
            {
              "name": "br-de142f048307",
              "mac": "02:42:17:82:cc:47",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-5a5cf4fd42a3",
              "mac": "02:42:c3:7c:1e:0c",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:49:73:17:fe",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethab6da56",
              "mac": "ce:42:92:6e:07:51",
              "addresses": [
                "fe80::cc42:92ff:fe6e:751/64"
              ]
            },
            {
              "name": "vetha8b8454",
              "mac": "a6:fc:d8:fb:06:fa",
              "addresses": [
                "fe80::a4fc:d8ff:fefb:6fa/64"
              ]
            },
            {
              "name": "veth705ec95",
              "mac": "ce:57:6d:d4:64:51",
              "addresses": [
                "fe80::cc57:6dff:fed4:6451/64"
              ]
            },
            {
              "name": "veth184536b",
              "mac": "f6:34:d7:5d:b8:18",
              "addresses": [
                "fe80::f434:d7ff:fe5d:b818/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:elk01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580295845,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "elk01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006364323,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 51899 MiB (84.48% inode=99%);\n /dev 15966 MiB (100.00% inode=100%);\n /data 728619 MiB (89.00% inode=100%);\n| /=9529MiB;49142;55285;0;61428 /dev=0MiB;12772;14369;0;15966 /data=90004MiB;654899;736761;0;818624\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506655,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1046",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:18:51:43:9c:f0",
              "addresses": [
                "10.36.37.238/21",
                "fe80::418:51ff:fe43:9cf0/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:1f:93:02",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:1f:93:02",
              "addresses": null
            },
            {
              "name": "br-956930c48ea1",
              "mac": "02:42:d8:e1:b5:46",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:d8ff:fee1:b546/64"
              ]
            },
            {
              "name": "br-de142f048307",
              "mac": "02:42:17:82:cc:47",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-5a5cf4fd42a3",
              "mac": "02:42:c3:7c:1e:0c",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:49:73:17:fe",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethab6da56",
              "mac": "ce:42:92:6e:07:51",
              "addresses": [
                "fe80::cc42:92ff:fe6e:751/64"
              ]
            },
            {
              "name": "vetha8b8454",
              "mac": "a6:fc:d8:fb:06:fa",
              "addresses": [
                "fe80::a4fc:d8ff:fefb:6fa/64"
              ]
            },
            {
              "name": "veth705ec95",
              "mac": "ce:57:6d:d4:64:51",
              "addresses": [
                "fe80::cc57:6dff:fed4:6451/64"
              ]
            },
            {
              "name": "veth184536b",
              "mac": "f6:34:d7:5d:b8:18",
              "addresses": [
                "fe80::f434:d7ff:fe5d:b818/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:elk01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580295845,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "elk01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.36702684,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (elk01.prod.sdp.statoil.no) resolves to my IP (10.36.37.238)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507445,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1046",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:18:51:43:9c:f0",
              "addresses": [
                "10.36.37.238/21",
                "fe80::418:51ff:fe43:9cf0/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:1f:93:02",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:1f:93:02",
              "addresses": null
            },
            {
              "name": "br-956930c48ea1",
              "mac": "02:42:d8:e1:b5:46",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:d8ff:fee1:b546/64"
              ]
            },
            {
              "name": "br-de142f048307",
              "mac": "02:42:17:82:cc:47",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-5a5cf4fd42a3",
              "mac": "02:42:c3:7c:1e:0c",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:49:73:17:fe",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethab6da56",
              "mac": "ce:42:92:6e:07:51",
              "addresses": [
                "fe80::cc42:92ff:fe6e:751/64"
              ]
            },
            {
              "name": "vetha8b8454",
              "mac": "a6:fc:d8:fb:06:fa",
              "addresses": [
                "fe80::a4fc:d8ff:fefb:6fa/64"
              ]
            },
            {
              "name": "veth705ec95",
              "mac": "ce:57:6d:d4:64:51",
              "addresses": [
                "fe80::cc57:6dff:fed4:6451/64"
              ]
            },
            {
              "name": "veth184536b",
              "mac": "f6:34:d7:5d:b8:18",
              "addresses": [
                "fe80::f434:d7ff:fe5d:b818/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:elk01.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507445,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "elk01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507445,
      "history": [
        {
          "status": 0,
          "executed": 1581507045
        },
        {
          "status": 0,
          "executed": 1581507065
        },
        {
          "status": 0,
          "executed": 1581507085
        },
        {
          "status": 0,
          "executed": 1581507105
        },
        {
          "status": 0,
          "executed": 1581507125
        },
        {
          "status": 0,
          "executed": 1581507145
        },
        {
          "status": 0,
          "executed": 1581507165
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507205
        },
        {
          "status": 0,
          "executed": 1581507225
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507265
        },
        {
          "status": 0,
          "executed": 1581507285
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507325
        },
        {
          "status": 0,
          "executed": 1581507345
        },
        {
          "status": 0,
          "executed": 1581507365
        },
        {
          "status": 0,
          "executed": 1581507385
        },
        {
          "status": 0,
          "executed": 1581507405
        },
        {
          "status": 0,
          "executed": 1581507427
        },
        {
          "status": 0,
          "executed": 1581507445
        }
      ],
      "issued": 1581507445,
      "output": "Keepalive last sent from elk01.prod.sdp.statoil.no at 2020-02-12 11:37:25 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507445,
      "occurrences": 55710,
      "occurrences_watermark": 55710,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507424,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1046",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:18:51:43:9c:f0",
              "addresses": [
                "10.36.37.238/21",
                "fe80::418:51ff:fe43:9cf0/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:1f:93:02",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:1f:93:02",
              "addresses": null
            },
            {
              "name": "br-956930c48ea1",
              "mac": "02:42:d8:e1:b5:46",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:d8ff:fee1:b546/64"
              ]
            },
            {
              "name": "br-de142f048307",
              "mac": "02:42:17:82:cc:47",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-5a5cf4fd42a3",
              "mac": "02:42:c3:7c:1e:0c",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:49:73:17:fe",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethab6da56",
              "mac": "ce:42:92:6e:07:51",
              "addresses": [
                "fe80::cc42:92ff:fe6e:751/64"
              ]
            },
            {
              "name": "vetha8b8454",
              "mac": "a6:fc:d8:fb:06:fa",
              "addresses": [
                "fe80::a4fc:d8ff:fefb:6fa/64"
              ]
            },
            {
              "name": "veth705ec95",
              "mac": "ce:57:6d:d4:64:51",
              "addresses": [
                "fe80::cc57:6dff:fed4:6451/64"
              ]
            },
            {
              "name": "veth184536b",
              "mac": "f6:34:d7:5d:b8:18",
              "addresses": [
                "fe80::f434:d7ff:fe5d:b818/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:elk01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580295845,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "elk01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.008736953,
      "executed": 1581507424,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506524
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506704
        },
        {
          "status": 0,
          "executed": 1581506764
        },
        {
          "status": 0,
          "executed": 1581506824
        },
        {
          "status": 0,
          "executed": 1581506884
        },
        {
          "status": 0,
          "executed": 1581506944
        },
        {
          "status": 0,
          "executed": 1581507004
        },
        {
          "status": 0,
          "executed": 1581507064
        },
        {
          "status": 0,
          "executed": 1581507124
        },
        {
          "status": 0,
          "executed": 1581507184
        },
        {
          "status": 0,
          "executed": 1581507244
        },
        {
          "status": 0,
          "executed": 1581507304
        },
        {
          "status": 0,
          "executed": 1581507364
        },
        {
          "status": 0,
          "executed": 1581507424
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.01, 0.04, 0.05|load1=0.010;80.000;90.000;0; load5=0.040;80.000;90.000;0; load15=0.050;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507424,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1046",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:18:51:43:9c:f0",
              "addresses": [
                "10.36.37.238/21",
                "fe80::418:51ff:fe43:9cf0/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:1f:93:02",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:1f:93:02",
              "addresses": null
            },
            {
              "name": "br-956930c48ea1",
              "mac": "02:42:d8:e1:b5:46",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:d8ff:fee1:b546/64"
              ]
            },
            {
              "name": "br-de142f048307",
              "mac": "02:42:17:82:cc:47",
              "addresses": [
                "172.18.0.1/16"
              ]
            },
            {
              "name": "br-5a5cf4fd42a3",
              "mac": "02:42:c3:7c:1e:0c",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:49:73:17:fe",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethab6da56",
              "mac": "ce:42:92:6e:07:51",
              "addresses": [
                "fe80::cc42:92ff:fe6e:751/64"
              ]
            },
            {
              "name": "vetha8b8454",
              "mac": "a6:fc:d8:fb:06:fa",
              "addresses": [
                "fe80::a4fc:d8ff:fefb:6fa/64"
              ]
            },
            {
              "name": "veth705ec95",
              "mac": "ce:57:6d:d4:64:51",
              "addresses": [
                "fe80::cc57:6dff:fed4:6451/64"
              ]
            },
            {
              "name": "veth184536b",
              "mac": "f6:34:d7:5d:b8:18",
              "addresses": [
                "fe80::f434:d7ff:fe5d:b818/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:elk01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580295845,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "elk01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006164583,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 100% free (2045 MB out of 2047 MB) |swap=2045MB;1023;409;0;2047\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp01.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:78:66",
              "addresses": [
                "143.97.90.197/24",
                "143.97.90.196/24",
                "fe80::250:56ff:fe85:7866/64"
              ]
            },
            {
              "name": "br-278f15c31f8b",
              "mac": "02:42:90:83:28:46",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:90ff:fe83:2846/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:42:7b:85:87",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethcddbaf5",
              "mac": "36:91:b9:2c:71:fd",
              "addresses": [
                "fe80::3491:b9ff:fe2c:71fd/64"
              ]
            },
            {
              "name": "veth766ba17",
              "mac": "b2:5f:c8:55:d5:31",
              "addresses": [
                "fe80::b05f:c8ff:fe55:d531/64"
              ]
            },
            {
              "name": "vetheee0e3c",
              "mac": "1a:95:8d:6c:04:39",
              "addresses": [
                "fe80::1895:8dff:fe6c:439/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:git01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580385234,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "git01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.00776027,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp01.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:78:66",
              "addresses": [
                "143.97.90.197/24",
                "143.97.90.196/24",
                "fe80::250:56ff:fe85:7866/64"
              ]
            },
            {
              "name": "br-278f15c31f8b",
              "mac": "02:42:90:83:28:46",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:90ff:fe83:2846/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:42:7b:85:87",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethcddbaf5",
              "mac": "36:91:b9:2c:71:fd",
              "addresses": [
                "fe80::3491:b9ff:fe2c:71fd/64"
              ]
            },
            {
              "name": "veth766ba17",
              "mac": "b2:5f:c8:55:d5:31",
              "addresses": [
                "fe80::b05f:c8ff:fe55:d531/64"
              ]
            },
            {
              "name": "vetheee0e3c",
              "mac": "1a:95:8d:6c:04:39",
              "addresses": [
                "fe80::1895:8dff:fe6c:439/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:git01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580385234,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "git01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.00473342,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n/ 21345 MB (76.59% inode=93%);\n/dev 15992 MB (100.00% inode=100%);\n/boot 284 MB (63.51% inode=100%);\n/data 775781 MB (37.41% inode=99%);\n/tmp 7473 MB (99.51% inode=100%);\n/var 6763 MB (50.80% inode=98%);\n| /=6523MB;23507;26445;0;29384 /dev=0MB;12793;14392;0;15992 /boot=163MB;380;428;0;476 /data=1297932MB;1733528;1950219;0;2166911 /tmp=36MB;6348;7141;0;7935 /var=6548MB;11186;12584;0;13983\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 6998,
      "occurrences_watermark": 6998,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506657,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp01.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:78:66",
              "addresses": [
                "143.97.90.197/24",
                "143.97.90.196/24",
                "fe80::250:56ff:fe85:7866/64"
              ]
            },
            {
              "name": "br-278f15c31f8b",
              "mac": "02:42:90:83:28:46",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:90ff:fe83:2846/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:42:7b:85:87",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethcddbaf5",
              "mac": "36:91:b9:2c:71:fd",
              "addresses": [
                "fe80::3491:b9ff:fe2c:71fd/64"
              ]
            },
            {
              "name": "veth766ba17",
              "mac": "b2:5f:c8:55:d5:31",
              "addresses": [
                "fe80::b05f:c8ff:fe55:d531/64"
              ]
            },
            {
              "name": "vetheee0e3c",
              "mac": "1a:95:8d:6c:04:39",
              "addresses": [
                "fe80::1895:8dff:fe6c:439/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:git01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580385234,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "git01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 2.397471547,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (git01.prod.sdp.statoil.no) resolves to my IP (143.97.90.197)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507445,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp01.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:78:66",
              "addresses": [
                "143.97.90.197/24",
                "143.97.90.196/24",
                "fe80::250:56ff:fe85:7866/64"
              ]
            },
            {
              "name": "br-278f15c31f8b",
              "mac": "02:42:90:83:28:46",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:90ff:fe83:2846/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:42:7b:85:87",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethcddbaf5",
              "mac": "36:91:b9:2c:71:fd",
              "addresses": [
                "fe80::3491:b9ff:fe2c:71fd/64"
              ]
            },
            {
              "name": "veth766ba17",
              "mac": "b2:5f:c8:55:d5:31",
              "addresses": [
                "fe80::b05f:c8ff:fe55:d531/64"
              ]
            },
            {
              "name": "vetheee0e3c",
              "mac": "1a:95:8d:6c:04:39",
              "addresses": [
                "fe80::1895:8dff:fe6c:439/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:git01.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507445,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "git01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507445,
      "history": [
        {
          "status": 0,
          "executed": 1581507045
        },
        {
          "status": 0,
          "executed": 1581507065
        },
        {
          "status": 0,
          "executed": 1581507085
        },
        {
          "status": 0,
          "executed": 1581507105
        },
        {
          "status": 0,
          "executed": 1581507125
        },
        {
          "status": 0,
          "executed": 1581507145
        },
        {
          "status": 0,
          "executed": 1581507165
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507205
        },
        {
          "status": 0,
          "executed": 1581507225
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507265
        },
        {
          "status": 0,
          "executed": 1581507285
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507325
        },
        {
          "status": 0,
          "executed": 1581507345
        },
        {
          "status": 0,
          "executed": 1581507365
        },
        {
          "status": 0,
          "executed": 1581507385
        },
        {
          "status": 0,
          "executed": 1581507405
        },
        {
          "status": 0,
          "executed": 1581507427
        },
        {
          "status": 0,
          "executed": 1581507445
        }
      ],
      "issued": 1581507445,
      "output": "Keepalive last sent from git01.prod.sdp.statoil.no at 2020-02-12 11:37:25 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507445,
      "occurrences": 55709,
      "occurrences_watermark": 55709,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507425,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp01.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:78:66",
              "addresses": [
                "143.97.90.197/24",
                "143.97.90.196/24",
                "fe80::250:56ff:fe85:7866/64"
              ]
            },
            {
              "name": "br-278f15c31f8b",
              "mac": "02:42:90:83:28:46",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:90ff:fe83:2846/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:42:7b:85:87",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethcddbaf5",
              "mac": "36:91:b9:2c:71:fd",
              "addresses": [
                "fe80::3491:b9ff:fe2c:71fd/64"
              ]
            },
            {
              "name": "veth766ba17",
              "mac": "b2:5f:c8:55:d5:31",
              "addresses": [
                "fe80::b05f:c8ff:fe55:d531/64"
              ]
            },
            {
              "name": "vetheee0e3c",
              "mac": "1a:95:8d:6c:04:39",
              "addresses": [
                "fe80::1895:8dff:fe6c:439/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:git01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580385234,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "git01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.032526179,
      "executed": 1581507425,
      "history": [
        {
          "status": 0,
          "executed": 1581506225
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506405
        },
        {
          "status": 0,
          "executed": 1581506465
        },
        {
          "status": 0,
          "executed": 1581506525
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506645
        },
        {
          "status": 0,
          "executed": 1581506705
        },
        {
          "status": 0,
          "executed": 1581506765
        },
        {
          "status": 0,
          "executed": 1581506825
        },
        {
          "status": 0,
          "executed": 1581506885
        },
        {
          "status": 0,
          "executed": 1581506945
        },
        {
          "status": 0,
          "executed": 1581507005
        },
        {
          "status": 0,
          "executed": 1581507065
        },
        {
          "status": 0,
          "executed": 1581507125
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507365
        },
        {
          "status": 0,
          "executed": 1581507425
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 6.44, 6.47, 5.20|load1=6.440;80.000;90.000;0; load5=6.470;80.000;90.000;0; load15=5.200;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507425,
      "occurrences": 18568,
      "occurrences_watermark": 18568,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp01.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:78:66",
              "addresses": [
                "143.97.90.197/24",
                "143.97.90.196/24",
                "fe80::250:56ff:fe85:7866/64"
              ]
            },
            {
              "name": "br-278f15c31f8b",
              "mac": "02:42:90:83:28:46",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:90ff:fe83:2846/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:42:7b:85:87",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "vethcddbaf5",
              "mac": "36:91:b9:2c:71:fd",
              "addresses": [
                "fe80::3491:b9ff:fe2c:71fd/64"
              ]
            },
            {
              "name": "veth766ba17",
              "mac": "b2:5f:c8:55:d5:31",
              "addresses": [
                "fe80::b05f:c8ff:fe55:d531/64"
              ]
            },
            {
              "name": "vetheee0e3c",
              "mac": "1a:95:8d:6c:04:39",
              "addresses": [
                "fe80::1895:8dff:fe6c:439/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:git01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580385234,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "git01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.003590281,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 72% free (5887 MB out of 8191 MB) |swap=5887MB;4095;1638;0;8191\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18568,
      "occurrences_watermark": 18568,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1085",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:76:7d:1b:39:c4",
              "addresses": [
                "10.36.36.69/21",
                "fe80::476:7dff:fe1b:39c4/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:ea:14:d8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:ea:14:d8",
              "addresses": null
            },
            {
              "name": "br-3d62d30c0714",
              "mac": "02:42:5a:fe:dc:40",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:5aff:fefe:dc40/64"
              ]
            },
            {
              "name": "br-4dac75d74972",
              "mac": "02:42:95:56:40:0e",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:95ff:fe56:400e/64"
              ]
            },
            {
              "name": "br-bacc82cfeb74",
              "mac": "02:42:fb:2f:22:23",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:fbff:fe2f:2223/64"
              ]
            },
            {
              "name": "br-bb1be0bc86be",
              "mac": "02:42:2c:8e:49:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:2cff:fe8e:491c/64"
              ]
            },
            {
              "name": "br-fa2bc25bcc21",
              "mac": "02:42:74:ec:7b:cc",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:74ff:feec:7bcc/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:33:06:e2:d4",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-91af0cfa044c",
              "mac": "02:42:25:10:23:50",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:25ff:fe10:2350/64"
              ]
            },
            {
              "name": "br-a9499f907b88",
              "mac": "02:42:dc:01:f3:10",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:dcff:fe01:f310/64"
              ]
            },
            {
              "name": "br-6b25d90ac9db",
              "mac": "02:42:3c:65:da:4b",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:3cff:fe65:da4b/64"
              ]
            },
            {
              "name": "vethab95424",
              "mac": "aa:0c:60:91:1b:68",
              "addresses": [
                "fe80::a80c:60ff:fe91:1b68/64"
              ]
            },
            {
              "name": "veth352f19b",
              "mac": "0e:d8:07:23:cd:4c",
              "addresses": [
                "fe80::cd8:7ff:fe23:cd4c/64"
              ]
            },
            {
              "name": "veth667e749",
              "mac": "16:d2:00:a0:4b:52",
              "addresses": [
                "fe80::14d2:ff:fea0:4b52/64"
              ]
            },
            {
              "name": "veth6a8ded4",
              "mac": "9e:fe:12:4b:30:8d",
              "addresses": [
                "fe80::9cfe:12ff:fe4b:308d/64"
              ]
            },
            {
              "name": "veth9ce2544",
              "mac": "22:25:e0:ef:45:2b",
              "addresses": [
                "fe80::2025:e0ff:feef:452b/64"
              ]
            },
            {
              "name": "veth612b181",
              "mac": "ea:e8:00:3c:59:25",
              "addresses": [
                "fe80::e8e8:ff:fe3c:5925/64"
              ]
            },
            {
              "name": "vethb1520c1",
              "mac": "7a:34:8c:a3:f7:6d",
              "addresses": [
                "fe80::7834:8cff:fea3:f76d/64"
              ]
            },
            {
              "name": "vethc5494f8",
              "mac": "22:f9:f8:57:5a:b0",
              "addresses": [
                "fe80::20f9:f8ff:fe57:5ab0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580385212,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.031638253,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1085",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:76:7d:1b:39:c4",
              "addresses": [
                "10.36.36.69/21",
                "fe80::476:7dff:fe1b:39c4/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:ea:14:d8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:ea:14:d8",
              "addresses": null
            },
            {
              "name": "br-3d62d30c0714",
              "mac": "02:42:5a:fe:dc:40",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:5aff:fefe:dc40/64"
              ]
            },
            {
              "name": "br-4dac75d74972",
              "mac": "02:42:95:56:40:0e",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:95ff:fe56:400e/64"
              ]
            },
            {
              "name": "br-bacc82cfeb74",
              "mac": "02:42:fb:2f:22:23",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:fbff:fe2f:2223/64"
              ]
            },
            {
              "name": "br-bb1be0bc86be",
              "mac": "02:42:2c:8e:49:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:2cff:fe8e:491c/64"
              ]
            },
            {
              "name": "br-fa2bc25bcc21",
              "mac": "02:42:74:ec:7b:cc",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:74ff:feec:7bcc/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:33:06:e2:d4",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-91af0cfa044c",
              "mac": "02:42:25:10:23:50",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:25ff:fe10:2350/64"
              ]
            },
            {
              "name": "br-a9499f907b88",
              "mac": "02:42:dc:01:f3:10",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:dcff:fe01:f310/64"
              ]
            },
            {
              "name": "br-6b25d90ac9db",
              "mac": "02:42:3c:65:da:4b",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:3cff:fe65:da4b/64"
              ]
            },
            {
              "name": "vethab95424",
              "mac": "aa:0c:60:91:1b:68",
              "addresses": [
                "fe80::a80c:60ff:fe91:1b68/64"
              ]
            },
            {
              "name": "veth352f19b",
              "mac": "0e:d8:07:23:cd:4c",
              "addresses": [
                "fe80::cd8:7ff:fe23:cd4c/64"
              ]
            },
            {
              "name": "veth667e749",
              "mac": "16:d2:00:a0:4b:52",
              "addresses": [
                "fe80::14d2:ff:fea0:4b52/64"
              ]
            },
            {
              "name": "veth6a8ded4",
              "mac": "9e:fe:12:4b:30:8d",
              "addresses": [
                "fe80::9cfe:12ff:fe4b:308d/64"
              ]
            },
            {
              "name": "veth9ce2544",
              "mac": "22:25:e0:ef:45:2b",
              "addresses": [
                "fe80::2025:e0ff:feef:452b/64"
              ]
            },
            {
              "name": "veth612b181",
              "mac": "ea:e8:00:3c:59:25",
              "addresses": [
                "fe80::e8e8:ff:fe3c:5925/64"
              ]
            },
            {
              "name": "vethb1520c1",
              "mac": "7a:34:8c:a3:f7:6d",
              "addresses": [
                "fe80::7834:8cff:fea3:f76d/64"
              ]
            },
            {
              "name": "vethc5494f8",
              "mac": "22:f9:f8:57:5a:b0",
              "addresses": [
                "fe80::20f9:f8ff:fe57:5ab0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580385212,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.056371496,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 32144 MiB (62.79% inode=99%);\n /dev 7903 MiB (100.00% inode=100%);\n /data 559157 MiB (91.05% inode=99%);\n| /=19044MiB;40950;46069;0;51188 /dev=0MiB;6322;7112;0;7903 /data=54938MiB;491276;552686;0;614096\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506658,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1085",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:76:7d:1b:39:c4",
              "addresses": [
                "10.36.36.69/21",
                "fe80::476:7dff:fe1b:39c4/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:ea:14:d8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:ea:14:d8",
              "addresses": null
            },
            {
              "name": "br-3d62d30c0714",
              "mac": "02:42:5a:fe:dc:40",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:5aff:fefe:dc40/64"
              ]
            },
            {
              "name": "br-4dac75d74972",
              "mac": "02:42:95:56:40:0e",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:95ff:fe56:400e/64"
              ]
            },
            {
              "name": "br-bacc82cfeb74",
              "mac": "02:42:fb:2f:22:23",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:fbff:fe2f:2223/64"
              ]
            },
            {
              "name": "br-bb1be0bc86be",
              "mac": "02:42:2c:8e:49:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:2cff:fe8e:491c/64"
              ]
            },
            {
              "name": "br-fa2bc25bcc21",
              "mac": "02:42:74:ec:7b:cc",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:74ff:feec:7bcc/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:33:06:e2:d4",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-91af0cfa044c",
              "mac": "02:42:25:10:23:50",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:25ff:fe10:2350/64"
              ]
            },
            {
              "name": "br-a9499f907b88",
              "mac": "02:42:dc:01:f3:10",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:dcff:fe01:f310/64"
              ]
            },
            {
              "name": "br-6b25d90ac9db",
              "mac": "02:42:3c:65:da:4b",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:3cff:fe65:da4b/64"
              ]
            },
            {
              "name": "vethab95424",
              "mac": "aa:0c:60:91:1b:68",
              "addresses": [
                "fe80::a80c:60ff:fe91:1b68/64"
              ]
            },
            {
              "name": "veth352f19b",
              "mac": "0e:d8:07:23:cd:4c",
              "addresses": [
                "fe80::cd8:7ff:fe23:cd4c/64"
              ]
            },
            {
              "name": "veth667e749",
              "mac": "16:d2:00:a0:4b:52",
              "addresses": [
                "fe80::14d2:ff:fea0:4b52/64"
              ]
            },
            {
              "name": "veth6a8ded4",
              "mac": "9e:fe:12:4b:30:8d",
              "addresses": [
                "fe80::9cfe:12ff:fe4b:308d/64"
              ]
            },
            {
              "name": "veth9ce2544",
              "mac": "22:25:e0:ef:45:2b",
              "addresses": [
                "fe80::2025:e0ff:feef:452b/64"
              ]
            },
            {
              "name": "veth612b181",
              "mac": "ea:e8:00:3c:59:25",
              "addresses": [
                "fe80::e8e8:ff:fe3c:5925/64"
              ]
            },
            {
              "name": "vethb1520c1",
              "mac": "7a:34:8c:a3:f7:6d",
              "addresses": [
                "fe80::7834:8cff:fea3:f76d/64"
              ]
            },
            {
              "name": "vethc5494f8",
              "mac": "22:f9:f8:57:5a:b0",
              "addresses": [
                "fe80::20f9:f8ff:fe57:5ab0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580385212,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 3.203296332,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (jenkins01.prod.sdp.statoil.no) resolves to my IP (10.36.36.69)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507452,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1085",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:76:7d:1b:39:c4",
              "addresses": [
                "10.36.36.69/21",
                "fe80::476:7dff:fe1b:39c4/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:ea:14:d8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:ea:14:d8",
              "addresses": null
            },
            {
              "name": "br-3d62d30c0714",
              "mac": "02:42:5a:fe:dc:40",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:5aff:fefe:dc40/64"
              ]
            },
            {
              "name": "br-4dac75d74972",
              "mac": "02:42:95:56:40:0e",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:95ff:fe56:400e/64"
              ]
            },
            {
              "name": "br-bacc82cfeb74",
              "mac": "02:42:fb:2f:22:23",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:fbff:fe2f:2223/64"
              ]
            },
            {
              "name": "br-bb1be0bc86be",
              "mac": "02:42:2c:8e:49:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:2cff:fe8e:491c/64"
              ]
            },
            {
              "name": "br-fa2bc25bcc21",
              "mac": "02:42:74:ec:7b:cc",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:74ff:feec:7bcc/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:33:06:e2:d4",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-91af0cfa044c",
              "mac": "02:42:25:10:23:50",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:25ff:fe10:2350/64"
              ]
            },
            {
              "name": "br-a9499f907b88",
              "mac": "02:42:dc:01:f3:10",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:dcff:fe01:f310/64"
              ]
            },
            {
              "name": "br-6b25d90ac9db",
              "mac": "02:42:3c:65:da:4b",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:3cff:fe65:da4b/64"
              ]
            },
            {
              "name": "vethab95424",
              "mac": "aa:0c:60:91:1b:68",
              "addresses": [
                "fe80::a80c:60ff:fe91:1b68/64"
              ]
            },
            {
              "name": "veth352f19b",
              "mac": "0e:d8:07:23:cd:4c",
              "addresses": [
                "fe80::cd8:7ff:fe23:cd4c/64"
              ]
            },
            {
              "name": "veth667e749",
              "mac": "16:d2:00:a0:4b:52",
              "addresses": [
                "fe80::14d2:ff:fea0:4b52/64"
              ]
            },
            {
              "name": "veth6a8ded4",
              "mac": "9e:fe:12:4b:30:8d",
              "addresses": [
                "fe80::9cfe:12ff:fe4b:308d/64"
              ]
            },
            {
              "name": "veth9ce2544",
              "mac": "22:25:e0:ef:45:2b",
              "addresses": [
                "fe80::2025:e0ff:feef:452b/64"
              ]
            },
            {
              "name": "veth612b181",
              "mac": "ea:e8:00:3c:59:25",
              "addresses": [
                "fe80::e8e8:ff:fe3c:5925/64"
              ]
            },
            {
              "name": "vethb1520c1",
              "mac": "7a:34:8c:a3:f7:6d",
              "addresses": [
                "fe80::7834:8cff:fea3:f76d/64"
              ]
            },
            {
              "name": "vethc5494f8",
              "mac": "22:f9:f8:57:5a:b0",
              "addresses": [
                "fe80::20f9:f8ff:fe57:5ab0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins01.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507452,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507452,
      "history": [
        {
          "status": 0,
          "executed": 1581507052
        },
        {
          "status": 0,
          "executed": 1581507072
        },
        {
          "status": 0,
          "executed": 1581507092
        },
        {
          "status": 0,
          "executed": 1581507112
        },
        {
          "status": 0,
          "executed": 1581507132
        },
        {
          "status": 0,
          "executed": 1581507152
        },
        {
          "status": 0,
          "executed": 1581507172
        },
        {
          "status": 0,
          "executed": 1581507192
        },
        {
          "status": 0,
          "executed": 1581507212
        },
        {
          "status": 0,
          "executed": 1581507232
        },
        {
          "status": 0,
          "executed": 1581507252
        },
        {
          "status": 0,
          "executed": 1581507272
        },
        {
          "status": 0,
          "executed": 1581507292
        },
        {
          "status": 0,
          "executed": 1581507312
        },
        {
          "status": 0,
          "executed": 1581507332
        },
        {
          "status": 0,
          "executed": 1581507352
        },
        {
          "status": 0,
          "executed": 1581507372
        },
        {
          "status": 0,
          "executed": 1581507392
        },
        {
          "status": 0,
          "executed": 1581507412
        },
        {
          "status": 0,
          "executed": 1581507432
        },
        {
          "status": 0,
          "executed": 1581507452
        }
      ],
      "issued": 1581507452,
      "output": "Keepalive last sent from jenkins01.prod.sdp.statoil.no at 2020-02-12 11:37:32 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507452,
      "occurrences": 55710,
      "occurrences_watermark": 55710,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507425,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1085",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:76:7d:1b:39:c4",
              "addresses": [
                "10.36.36.69/21",
                "fe80::476:7dff:fe1b:39c4/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:ea:14:d8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:ea:14:d8",
              "addresses": null
            },
            {
              "name": "br-3d62d30c0714",
              "mac": "02:42:5a:fe:dc:40",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:5aff:fefe:dc40/64"
              ]
            },
            {
              "name": "br-4dac75d74972",
              "mac": "02:42:95:56:40:0e",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:95ff:fe56:400e/64"
              ]
            },
            {
              "name": "br-bacc82cfeb74",
              "mac": "02:42:fb:2f:22:23",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:fbff:fe2f:2223/64"
              ]
            },
            {
              "name": "br-bb1be0bc86be",
              "mac": "02:42:2c:8e:49:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:2cff:fe8e:491c/64"
              ]
            },
            {
              "name": "br-fa2bc25bcc21",
              "mac": "02:42:74:ec:7b:cc",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:74ff:feec:7bcc/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:33:06:e2:d4",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-91af0cfa044c",
              "mac": "02:42:25:10:23:50",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:25ff:fe10:2350/64"
              ]
            },
            {
              "name": "br-a9499f907b88",
              "mac": "02:42:dc:01:f3:10",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:dcff:fe01:f310/64"
              ]
            },
            {
              "name": "br-6b25d90ac9db",
              "mac": "02:42:3c:65:da:4b",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:3cff:fe65:da4b/64"
              ]
            },
            {
              "name": "vethab95424",
              "mac": "aa:0c:60:91:1b:68",
              "addresses": [
                "fe80::a80c:60ff:fe91:1b68/64"
              ]
            },
            {
              "name": "veth352f19b",
              "mac": "0e:d8:07:23:cd:4c",
              "addresses": [
                "fe80::cd8:7ff:fe23:cd4c/64"
              ]
            },
            {
              "name": "veth667e749",
              "mac": "16:d2:00:a0:4b:52",
              "addresses": [
                "fe80::14d2:ff:fea0:4b52/64"
              ]
            },
            {
              "name": "veth6a8ded4",
              "mac": "9e:fe:12:4b:30:8d",
              "addresses": [
                "fe80::9cfe:12ff:fe4b:308d/64"
              ]
            },
            {
              "name": "veth9ce2544",
              "mac": "22:25:e0:ef:45:2b",
              "addresses": [
                "fe80::2025:e0ff:feef:452b/64"
              ]
            },
            {
              "name": "veth612b181",
              "mac": "ea:e8:00:3c:59:25",
              "addresses": [
                "fe80::e8e8:ff:fe3c:5925/64"
              ]
            },
            {
              "name": "vethb1520c1",
              "mac": "7a:34:8c:a3:f7:6d",
              "addresses": [
                "fe80::7834:8cff:fea3:f76d/64"
              ]
            },
            {
              "name": "vethc5494f8",
              "mac": "22:f9:f8:57:5a:b0",
              "addresses": [
                "fe80::20f9:f8ff:fe57:5ab0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580385212,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.108985382,
      "executed": 1581507424,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506525
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506705
        },
        {
          "status": 0,
          "executed": 1581506764
        },
        {
          "status": 0,
          "executed": 1581506824
        },
        {
          "status": 0,
          "executed": 1581506885
        },
        {
          "status": 0,
          "executed": 1581506945
        },
        {
          "status": 0,
          "executed": 1581507005
        },
        {
          "status": 0,
          "executed": 1581507064
        },
        {
          "status": 0,
          "executed": 1581507124
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507364
        },
        {
          "status": 0,
          "executed": 1581507424
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 8.46, 8.67, 6.93|load1=8.460;80.000;90.000;0; load5=8.670;80.000;90.000;0; load15=6.930;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507424,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1085",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:76:7d:1b:39:c4",
              "addresses": [
                "10.36.36.69/21",
                "fe80::476:7dff:fe1b:39c4/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:ea:14:d8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:ea:14:d8",
              "addresses": null
            },
            {
              "name": "br-3d62d30c0714",
              "mac": "02:42:5a:fe:dc:40",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:5aff:fefe:dc40/64"
              ]
            },
            {
              "name": "br-4dac75d74972",
              "mac": "02:42:95:56:40:0e",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:95ff:fe56:400e/64"
              ]
            },
            {
              "name": "br-bacc82cfeb74",
              "mac": "02:42:fb:2f:22:23",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:fbff:fe2f:2223/64"
              ]
            },
            {
              "name": "br-bb1be0bc86be",
              "mac": "02:42:2c:8e:49:1c",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:2cff:fe8e:491c/64"
              ]
            },
            {
              "name": "br-fa2bc25bcc21",
              "mac": "02:42:74:ec:7b:cc",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:74ff:feec:7bcc/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:33:06:e2:d4",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-91af0cfa044c",
              "mac": "02:42:25:10:23:50",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:25ff:fe10:2350/64"
              ]
            },
            {
              "name": "br-a9499f907b88",
              "mac": "02:42:dc:01:f3:10",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:dcff:fe01:f310/64"
              ]
            },
            {
              "name": "br-6b25d90ac9db",
              "mac": "02:42:3c:65:da:4b",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:3cff:fe65:da4b/64"
              ]
            },
            {
              "name": "vethab95424",
              "mac": "aa:0c:60:91:1b:68",
              "addresses": [
                "fe80::a80c:60ff:fe91:1b68/64"
              ]
            },
            {
              "name": "veth352f19b",
              "mac": "0e:d8:07:23:cd:4c",
              "addresses": [
                "fe80::cd8:7ff:fe23:cd4c/64"
              ]
            },
            {
              "name": "veth667e749",
              "mac": "16:d2:00:a0:4b:52",
              "addresses": [
                "fe80::14d2:ff:fea0:4b52/64"
              ]
            },
            {
              "name": "veth6a8ded4",
              "mac": "9e:fe:12:4b:30:8d",
              "addresses": [
                "fe80::9cfe:12ff:fe4b:308d/64"
              ]
            },
            {
              "name": "veth9ce2544",
              "mac": "22:25:e0:ef:45:2b",
              "addresses": [
                "fe80::2025:e0ff:feef:452b/64"
              ]
            },
            {
              "name": "veth612b181",
              "mac": "ea:e8:00:3c:59:25",
              "addresses": [
                "fe80::e8e8:ff:fe3c:5925/64"
              ]
            },
            {
              "name": "vethb1520c1",
              "mac": "7a:34:8c:a3:f7:6d",
              "addresses": [
                "fe80::7834:8cff:fea3:f76d/64"
              ]
            },
            {
              "name": "vethc5494f8",
              "mac": "22:f9:f8:57:5a:b0",
              "addresses": [
                "fe80::20f9:f8ff:fe57:5ab0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580385212,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.036019317,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 1,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 1,
          "executed": 1581507131
        },
        {
          "status": 1,
          "executed": 1581507191
        },
        {
          "status": 1,
          "executed": 1581507251
        },
        {
          "status": 1,
          "executed": 1581507311
        },
        {
          "status": 1,
          "executed": 1581507371
        },
        {
          "status": 1,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP WARNING - 49% free (5869 MB out of 11999 MB) |swap=5869MB;5999;2399;0;11999\n",
      "state": "failing",
      "status": 1,
      "total_state_change": 15,
      "last_ok": 1581507071,
      "occurrences": 6,
      "occurrences_watermark": 6,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1068.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:79:23",
              "addresses": [
                "10.217.112.67/22",
                "fe80::250:56ff:fea2:7923/64"
              ]
            },
            {
              "name": "br-5a027c89ba0f",
              "mac": "02:42:70:05:6d:1d",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:70ff:fe05:6d1d/64"
              ]
            },
            {
              "name": "br-97d8cbff7abc",
              "mac": "02:42:cb:c4:4f:a3",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:cbff:fec4:4fa3/64"
              ]
            },
            {
              "name": "br-d10afdebfd6a",
              "mac": "02:42:32:ae:f3:79",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:32ff:feae:f379/64"
              ]
            },
            {
              "name": "br-e6f32ca648b8",
              "mac": "02:42:b0:11:9f:93",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:b0ff:fe11:9f93/64"
              ]
            },
            {
              "name": "br-3423b42d1aa4",
              "mac": "02:42:a4:c7:d7:14",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:a4ff:fec7:d714/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:32:95:2d:26",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5dbc5d90dcd8",
              "mac": "02:42:06:dc:8c:a1",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:6ff:fedc:8ca1/64"
              ]
            },
            {
              "name": "br-ff87af178c06",
              "mac": "02:42:e4:b3:44:58",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:e4ff:feb3:4458/64"
              ]
            },
            {
              "name": "br-098dcb9ad9bd",
              "mac": "02:42:cd:06:59:e2",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:cdff:fe06:59e2/64"
              ]
            },
            {
              "name": "veth29ed73f",
              "mac": "4e:ab:0d:f0:7d:dc",
              "addresses": [
                "fe80::4cab:dff:fef0:7ddc/64"
              ]
            },
            {
              "name": "veth9d6463a",
              "mac": "7e:2a:fd:54:63:38",
              "addresses": [
                "fe80::7c2a:fdff:fe54:6338/64"
              ]
            },
            {
              "name": "veth9d0a837",
              "mac": "ca:80:3d:1a:8d:33",
              "addresses": [
                "fe80::c880:3dff:fe1a:8d33/64"
              ]
            },
            {
              "name": "vethfe746dc",
              "mac": "2e:03:63:39:7d:eb",
              "addresses": [
                "fe80::2c03:63ff:fe39:7deb/64"
              ]
            },
            {
              "name": "veth5955b7d",
              "mac": "fa:c1:4f:aa:a2:8d",
              "addresses": [
                "fe80::f8c1:4fff:feaa:a28d/64"
              ]
            },
            {
              "name": "veth7c9ae00",
              "mac": "8a:91:51:38:03:80",
              "addresses": [
                "fe80::8891:51ff:fe38:380/64"
              ]
            },
            {
              "name": "veth3eddd0b",
              "mac": "c6:5e:41:d1:8d:d6",
              "addresses": [
                "fe80::c45e:41ff:fed1:8dd6/64"
              ]
            },
            {
              "name": "veth9f80c17",
              "mac": "7a:ff:56:25:d5:a3",
              "addresses": [
                "fe80::78ff:56ff:fe25:d5a3/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins02.prod.sdp.statoil.no"
      ],
      "last_seen": 1580383197,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.008020003,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1068.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:79:23",
              "addresses": [
                "10.217.112.67/22",
                "fe80::250:56ff:fea2:7923/64"
              ]
            },
            {
              "name": "br-5a027c89ba0f",
              "mac": "02:42:70:05:6d:1d",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:70ff:fe05:6d1d/64"
              ]
            },
            {
              "name": "br-97d8cbff7abc",
              "mac": "02:42:cb:c4:4f:a3",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:cbff:fec4:4fa3/64"
              ]
            },
            {
              "name": "br-d10afdebfd6a",
              "mac": "02:42:32:ae:f3:79",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:32ff:feae:f379/64"
              ]
            },
            {
              "name": "br-e6f32ca648b8",
              "mac": "02:42:b0:11:9f:93",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:b0ff:fe11:9f93/64"
              ]
            },
            {
              "name": "br-3423b42d1aa4",
              "mac": "02:42:a4:c7:d7:14",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:a4ff:fec7:d714/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:32:95:2d:26",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5dbc5d90dcd8",
              "mac": "02:42:06:dc:8c:a1",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:6ff:fedc:8ca1/64"
              ]
            },
            {
              "name": "br-ff87af178c06",
              "mac": "02:42:e4:b3:44:58",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:e4ff:feb3:4458/64"
              ]
            },
            {
              "name": "br-098dcb9ad9bd",
              "mac": "02:42:cd:06:59:e2",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:cdff:fe06:59e2/64"
              ]
            },
            {
              "name": "veth29ed73f",
              "mac": "4e:ab:0d:f0:7d:dc",
              "addresses": [
                "fe80::4cab:dff:fef0:7ddc/64"
              ]
            },
            {
              "name": "veth9d6463a",
              "mac": "7e:2a:fd:54:63:38",
              "addresses": [
                "fe80::7c2a:fdff:fe54:6338/64"
              ]
            },
            {
              "name": "veth9d0a837",
              "mac": "ca:80:3d:1a:8d:33",
              "addresses": [
                "fe80::c880:3dff:fe1a:8d33/64"
              ]
            },
            {
              "name": "vethfe746dc",
              "mac": "2e:03:63:39:7d:eb",
              "addresses": [
                "fe80::2c03:63ff:fe39:7deb/64"
              ]
            },
            {
              "name": "veth5955b7d",
              "mac": "fa:c1:4f:aa:a2:8d",
              "addresses": [
                "fe80::f8c1:4fff:feaa:a28d/64"
              ]
            },
            {
              "name": "veth7c9ae00",
              "mac": "8a:91:51:38:03:80",
              "addresses": [
                "fe80::8891:51ff:fe38:380/64"
              ]
            },
            {
              "name": "veth3eddd0b",
              "mac": "c6:5e:41:d1:8d:d6",
              "addresses": [
                "fe80::c45e:41ff:fed1:8dd6/64"
              ]
            },
            {
              "name": "veth9f80c17",
              "mac": "7a:ff:56:25:d5:a3",
              "addresses": [
                "fe80::78ff:56ff:fe25:d5a3/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins02.prod.sdp.statoil.no"
      ],
      "last_seen": 1580383197,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004335772,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n/ 27194 MB (90.74% inode=100%);\n/dev 11960 MB (100.00% inode=100%);\n/boot 281 MB (62.96% inode=100%);\n/tmp 8149 MB (99.60% inode=100%);\n/var 6110 MB (74.68% inode=100%);\n/data 162386 MB (79.04% inode=99%);\n| /=2775MB;23975;26972;0;29969 /dev=0MB;9568;10764;0;11960 /boot=165MB;380;428;0;476 /tmp=32MB;6545;7363;0;8182 /var=2071MB;6545;7363;0;8182 /data=43050MB;164348;184892;0;205436\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18566,
      "occurrences_watermark": 18566,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506657,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1068.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:79:23",
              "addresses": [
                "10.217.112.67/22",
                "fe80::250:56ff:fea2:7923/64"
              ]
            },
            {
              "name": "br-5a027c89ba0f",
              "mac": "02:42:70:05:6d:1d",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:70ff:fe05:6d1d/64"
              ]
            },
            {
              "name": "br-97d8cbff7abc",
              "mac": "02:42:cb:c4:4f:a3",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:cbff:fec4:4fa3/64"
              ]
            },
            {
              "name": "br-d10afdebfd6a",
              "mac": "02:42:32:ae:f3:79",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:32ff:feae:f379/64"
              ]
            },
            {
              "name": "br-e6f32ca648b8",
              "mac": "02:42:b0:11:9f:93",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:b0ff:fe11:9f93/64"
              ]
            },
            {
              "name": "br-3423b42d1aa4",
              "mac": "02:42:a4:c7:d7:14",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:a4ff:fec7:d714/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:32:95:2d:26",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5dbc5d90dcd8",
              "mac": "02:42:06:dc:8c:a1",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:6ff:fedc:8ca1/64"
              ]
            },
            {
              "name": "br-ff87af178c06",
              "mac": "02:42:e4:b3:44:58",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:e4ff:feb3:4458/64"
              ]
            },
            {
              "name": "br-098dcb9ad9bd",
              "mac": "02:42:cd:06:59:e2",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:cdff:fe06:59e2/64"
              ]
            },
            {
              "name": "veth29ed73f",
              "mac": "4e:ab:0d:f0:7d:dc",
              "addresses": [
                "fe80::4cab:dff:fef0:7ddc/64"
              ]
            },
            {
              "name": "veth9d6463a",
              "mac": "7e:2a:fd:54:63:38",
              "addresses": [
                "fe80::7c2a:fdff:fe54:6338/64"
              ]
            },
            {
              "name": "veth9d0a837",
              "mac": "ca:80:3d:1a:8d:33",
              "addresses": [
                "fe80::c880:3dff:fe1a:8d33/64"
              ]
            },
            {
              "name": "vethfe746dc",
              "mac": "2e:03:63:39:7d:eb",
              "addresses": [
                "fe80::2c03:63ff:fe39:7deb/64"
              ]
            },
            {
              "name": "veth5955b7d",
              "mac": "fa:c1:4f:aa:a2:8d",
              "addresses": [
                "fe80::f8c1:4fff:feaa:a28d/64"
              ]
            },
            {
              "name": "veth7c9ae00",
              "mac": "8a:91:51:38:03:80",
              "addresses": [
                "fe80::8891:51ff:fe38:380/64"
              ]
            },
            {
              "name": "veth3eddd0b",
              "mac": "c6:5e:41:d1:8d:d6",
              "addresses": [
                "fe80::c45e:41ff:fed1:8dd6/64"
              ]
            },
            {
              "name": "veth9f80c17",
              "mac": "7a:ff:56:25:d5:a3",
              "addresses": [
                "fe80::78ff:56ff:fe25:d5a3/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins02.prod.sdp.statoil.no"
      ],
      "last_seen": 1580383197,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 2.3519762650000002,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (jenkins02.prod.sdp.statoil.no) resolves to my IP (10.217.112.67)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507453,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1068.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:79:23",
              "addresses": [
                "10.217.112.67/22",
                "fe80::250:56ff:fea2:7923/64"
              ]
            },
            {
              "name": "br-5a027c89ba0f",
              "mac": "02:42:70:05:6d:1d",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:70ff:fe05:6d1d/64"
              ]
            },
            {
              "name": "br-97d8cbff7abc",
              "mac": "02:42:cb:c4:4f:a3",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:cbff:fec4:4fa3/64"
              ]
            },
            {
              "name": "br-d10afdebfd6a",
              "mac": "02:42:32:ae:f3:79",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:32ff:feae:f379/64"
              ]
            },
            {
              "name": "br-e6f32ca648b8",
              "mac": "02:42:b0:11:9f:93",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:b0ff:fe11:9f93/64"
              ]
            },
            {
              "name": "br-3423b42d1aa4",
              "mac": "02:42:a4:c7:d7:14",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:a4ff:fec7:d714/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:32:95:2d:26",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5dbc5d90dcd8",
              "mac": "02:42:06:dc:8c:a1",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:6ff:fedc:8ca1/64"
              ]
            },
            {
              "name": "br-ff87af178c06",
              "mac": "02:42:e4:b3:44:58",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:e4ff:feb3:4458/64"
              ]
            },
            {
              "name": "br-098dcb9ad9bd",
              "mac": "02:42:cd:06:59:e2",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:cdff:fe06:59e2/64"
              ]
            },
            {
              "name": "veth29ed73f",
              "mac": "4e:ab:0d:f0:7d:dc",
              "addresses": [
                "fe80::4cab:dff:fef0:7ddc/64"
              ]
            },
            {
              "name": "veth9d6463a",
              "mac": "7e:2a:fd:54:63:38",
              "addresses": [
                "fe80::7c2a:fdff:fe54:6338/64"
              ]
            },
            {
              "name": "veth9d0a837",
              "mac": "ca:80:3d:1a:8d:33",
              "addresses": [
                "fe80::c880:3dff:fe1a:8d33/64"
              ]
            },
            {
              "name": "vethfe746dc",
              "mac": "2e:03:63:39:7d:eb",
              "addresses": [
                "fe80::2c03:63ff:fe39:7deb/64"
              ]
            },
            {
              "name": "veth5955b7d",
              "mac": "fa:c1:4f:aa:a2:8d",
              "addresses": [
                "fe80::f8c1:4fff:feaa:a28d/64"
              ]
            },
            {
              "name": "veth7c9ae00",
              "mac": "8a:91:51:38:03:80",
              "addresses": [
                "fe80::8891:51ff:fe38:380/64"
              ]
            },
            {
              "name": "veth3eddd0b",
              "mac": "c6:5e:41:d1:8d:d6",
              "addresses": [
                "fe80::c45e:41ff:fed1:8dd6/64"
              ]
            },
            {
              "name": "veth9f80c17",
              "mac": "7a:ff:56:25:d5:a3",
              "addresses": [
                "fe80::78ff:56ff:fe25:d5a3/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins02.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507453,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507453,
      "history": [
        {
          "status": 0,
          "executed": 1581507053
        },
        {
          "status": 0,
          "executed": 1581507073
        },
        {
          "status": 0,
          "executed": 1581507093
        },
        {
          "status": 0,
          "executed": 1581507113
        },
        {
          "status": 0,
          "executed": 1581507133
        },
        {
          "status": 0,
          "executed": 1581507153
        },
        {
          "status": 0,
          "executed": 1581507173
        },
        {
          "status": 0,
          "executed": 1581507193
        },
        {
          "status": 0,
          "executed": 1581507213
        },
        {
          "status": 0,
          "executed": 1581507233
        },
        {
          "status": 0,
          "executed": 1581507253
        },
        {
          "status": 0,
          "executed": 1581507273
        },
        {
          "status": 0,
          "executed": 1581507293
        },
        {
          "status": 0,
          "executed": 1581507313
        },
        {
          "status": 0,
          "executed": 1581507333
        },
        {
          "status": 0,
          "executed": 1581507353
        },
        {
          "status": 0,
          "executed": 1581507373
        },
        {
          "status": 0,
          "executed": 1581507393
        },
        {
          "status": 0,
          "executed": 1581507413
        },
        {
          "status": 0,
          "executed": 1581507433
        },
        {
          "status": 0,
          "executed": 1581507453
        }
      ],
      "issued": 1581507453,
      "output": "Keepalive last sent from jenkins02.prod.sdp.statoil.no at 2020-02-12 11:37:33 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507453,
      "occurrences": 55705,
      "occurrences_watermark": 55705,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507425,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1068.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:79:23",
              "addresses": [
                "10.217.112.67/22",
                "fe80::250:56ff:fea2:7923/64"
              ]
            },
            {
              "name": "br-5a027c89ba0f",
              "mac": "02:42:70:05:6d:1d",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:70ff:fe05:6d1d/64"
              ]
            },
            {
              "name": "br-97d8cbff7abc",
              "mac": "02:42:cb:c4:4f:a3",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:cbff:fec4:4fa3/64"
              ]
            },
            {
              "name": "br-d10afdebfd6a",
              "mac": "02:42:32:ae:f3:79",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:32ff:feae:f379/64"
              ]
            },
            {
              "name": "br-e6f32ca648b8",
              "mac": "02:42:b0:11:9f:93",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:b0ff:fe11:9f93/64"
              ]
            },
            {
              "name": "br-3423b42d1aa4",
              "mac": "02:42:a4:c7:d7:14",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:a4ff:fec7:d714/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:32:95:2d:26",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5dbc5d90dcd8",
              "mac": "02:42:06:dc:8c:a1",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:6ff:fedc:8ca1/64"
              ]
            },
            {
              "name": "br-ff87af178c06",
              "mac": "02:42:e4:b3:44:58",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:e4ff:feb3:4458/64"
              ]
            },
            {
              "name": "br-098dcb9ad9bd",
              "mac": "02:42:cd:06:59:e2",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:cdff:fe06:59e2/64"
              ]
            },
            {
              "name": "veth29ed73f",
              "mac": "4e:ab:0d:f0:7d:dc",
              "addresses": [
                "fe80::4cab:dff:fef0:7ddc/64"
              ]
            },
            {
              "name": "veth9d6463a",
              "mac": "7e:2a:fd:54:63:38",
              "addresses": [
                "fe80::7c2a:fdff:fe54:6338/64"
              ]
            },
            {
              "name": "veth9d0a837",
              "mac": "ca:80:3d:1a:8d:33",
              "addresses": [
                "fe80::c880:3dff:fe1a:8d33/64"
              ]
            },
            {
              "name": "vethfe746dc",
              "mac": "2e:03:63:39:7d:eb",
              "addresses": [
                "fe80::2c03:63ff:fe39:7deb/64"
              ]
            },
            {
              "name": "veth5955b7d",
              "mac": "fa:c1:4f:aa:a2:8d",
              "addresses": [
                "fe80::f8c1:4fff:feaa:a28d/64"
              ]
            },
            {
              "name": "veth7c9ae00",
              "mac": "8a:91:51:38:03:80",
              "addresses": [
                "fe80::8891:51ff:fe38:380/64"
              ]
            },
            {
              "name": "veth3eddd0b",
              "mac": "c6:5e:41:d1:8d:d6",
              "addresses": [
                "fe80::c45e:41ff:fed1:8dd6/64"
              ]
            },
            {
              "name": "veth9f80c17",
              "mac": "7a:ff:56:25:d5:a3",
              "addresses": [
                "fe80::78ff:56ff:fe25:d5a3/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins02.prod.sdp.statoil.no"
      ],
      "last_seen": 1580383197,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.008510818,
      "executed": 1581507425,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506525
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506705
        },
        {
          "status": 0,
          "executed": 1581506765
        },
        {
          "status": 0,
          "executed": 1581506825
        },
        {
          "status": 0,
          "executed": 1581506885
        },
        {
          "status": 0,
          "executed": 1581506945
        },
        {
          "status": 0,
          "executed": 1581507005
        },
        {
          "status": 0,
          "executed": 1581507065
        },
        {
          "status": 0,
          "executed": 1581507125
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507365
        },
        {
          "status": 0,
          "executed": 1581507425
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.01, 0.06, 0.05|load1=0.010;80.000;90.000;0; load5=0.060;80.000;90.000;0; load15=0.050;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507425,
      "occurrences": 18566,
      "occurrences_watermark": 18566,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1068.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:a2:79:23",
              "addresses": [
                "10.217.112.67/22",
                "fe80::250:56ff:fea2:7923/64"
              ]
            },
            {
              "name": "br-5a027c89ba0f",
              "mac": "02:42:70:05:6d:1d",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:70ff:fe05:6d1d/64"
              ]
            },
            {
              "name": "br-97d8cbff7abc",
              "mac": "02:42:cb:c4:4f:a3",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:cbff:fec4:4fa3/64"
              ]
            },
            {
              "name": "br-d10afdebfd6a",
              "mac": "02:42:32:ae:f3:79",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:32ff:feae:f379/64"
              ]
            },
            {
              "name": "br-e6f32ca648b8",
              "mac": "02:42:b0:11:9f:93",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:b0ff:fe11:9f93/64"
              ]
            },
            {
              "name": "br-3423b42d1aa4",
              "mac": "02:42:a4:c7:d7:14",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:a4ff:fec7:d714/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:32:95:2d:26",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5dbc5d90dcd8",
              "mac": "02:42:06:dc:8c:a1",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:6ff:fedc:8ca1/64"
              ]
            },
            {
              "name": "br-ff87af178c06",
              "mac": "02:42:e4:b3:44:58",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:e4ff:feb3:4458/64"
              ]
            },
            {
              "name": "br-098dcb9ad9bd",
              "mac": "02:42:cd:06:59:e2",
              "addresses": [
                "172.25.0.1/16",
                "fe80::42:cdff:fe06:59e2/64"
              ]
            },
            {
              "name": "veth29ed73f",
              "mac": "4e:ab:0d:f0:7d:dc",
              "addresses": [
                "fe80::4cab:dff:fef0:7ddc/64"
              ]
            },
            {
              "name": "veth9d6463a",
              "mac": "7e:2a:fd:54:63:38",
              "addresses": [
                "fe80::7c2a:fdff:fe54:6338/64"
              ]
            },
            {
              "name": "veth9d0a837",
              "mac": "ca:80:3d:1a:8d:33",
              "addresses": [
                "fe80::c880:3dff:fe1a:8d33/64"
              ]
            },
            {
              "name": "vethfe746dc",
              "mac": "2e:03:63:39:7d:eb",
              "addresses": [
                "fe80::2c03:63ff:fe39:7deb/64"
              ]
            },
            {
              "name": "veth5955b7d",
              "mac": "fa:c1:4f:aa:a2:8d",
              "addresses": [
                "fe80::f8c1:4fff:feaa:a28d/64"
              ]
            },
            {
              "name": "veth7c9ae00",
              "mac": "8a:91:51:38:03:80",
              "addresses": [
                "fe80::8891:51ff:fe38:380/64"
              ]
            },
            {
              "name": "veth3eddd0b",
              "mac": "c6:5e:41:d1:8d:d6",
              "addresses": [
                "fe80::c45e:41ff:fed1:8dd6/64"
              ]
            },
            {
              "name": "veth9f80c17",
              "mac": "7a:ff:56:25:d5:a3",
              "addresses": [
                "fe80::78ff:56ff:fe25:d5a3/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:jenkins02.prod.sdp.statoil.no"
      ],
      "last_seen": 1580383197,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.003328281,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 57% free (4638 MB out of 8191 MB) |swap=4638MB;4095;1638;0;8191\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18566,
      "occurrences_watermark": 18566,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507375,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.equinor.com -S -u \"/ioc/login?from=%2Fst%2F\" -w 15 -c 30",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.2826637,
      "executed": 1581507375,
      "history": [
        {
          "status": 0,
          "executed": 1581506175
        },
        {
          "status": 0,
          "executed": 1581506235
        },
        {
          "status": 0,
          "executed": 1581506295
        },
        {
          "status": 0,
          "executed": 1581506355
        },
        {
          "status": 0,
          "executed": 1581506415
        },
        {
          "status": 0,
          "executed": 1581506475
        },
        {
          "status": 0,
          "executed": 1581506535
        },
        {
          "status": 0,
          "executed": 1581506595
        },
        {
          "status": 0,
          "executed": 1581506655
        },
        {
          "status": 0,
          "executed": 1581506715
        },
        {
          "status": 0,
          "executed": 1581506775
        },
        {
          "status": 0,
          "executed": 1581506835
        },
        {
          "status": 0,
          "executed": 1581506895
        },
        {
          "status": 0,
          "executed": 1581506955
        },
        {
          "status": 0,
          "executed": 1581507015
        },
        {
          "status": 0,
          "executed": 1581507075
        },
        {
          "status": 0,
          "executed": 1581507135
        },
        {
          "status": 0,
          "executed": 1581507196
        },
        {
          "status": 0,
          "executed": 1581507255
        },
        {
          "status": 0,
          "executed": 1581507315
        },
        {
          "status": 0,
          "executed": 1581507375
        }
      ],
      "issued": 1581507413,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2864 bytes in 0.277 second response time |time=0.277066s;15.000000;30.000000;0.000000 size=2864B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507375,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.equinor.com_ioc",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507408,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.equinor.com -S -u \"/komodo/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.3624139,
      "executed": 1581507408,
      "history": [
        {
          "status": 0,
          "executed": 1581506208
        },
        {
          "status": 0,
          "executed": 1581506268
        },
        {
          "status": 0,
          "executed": 1581506328
        },
        {
          "status": 0,
          "executed": 1581506388
        },
        {
          "status": 0,
          "executed": 1581506448
        },
        {
          "status": 0,
          "executed": 1581506508
        },
        {
          "status": 0,
          "executed": 1581506568
        },
        {
          "status": 0,
          "executed": 1581506628
        },
        {
          "status": 0,
          "executed": 1581506688
        },
        {
          "status": 0,
          "executed": 1581506748
        },
        {
          "status": 0,
          "executed": 1581506808
        },
        {
          "status": 0,
          "executed": 1581506868
        },
        {
          "status": 0,
          "executed": 1581506928
        },
        {
          "status": 0,
          "executed": 1581506988
        },
        {
          "status": 0,
          "executed": 1581507048
        },
        {
          "status": 0,
          "executed": 1581507108
        },
        {
          "status": 0,
          "executed": 1581507168
        },
        {
          "status": 0,
          "executed": 1581507228
        },
        {
          "status": 0,
          "executed": 1581507288
        },
        {
          "status": 0,
          "executed": 1581507348
        },
        {
          "status": 0,
          "executed": 1581507408
        }
      ],
      "issued": 1581507446,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2935 bytes in 0.357 second response time |time=0.356544s;5.000000;10.000000;0.000000 size=2935B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507408,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.equinor.com_komodo",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507395,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.equinor.com -S -u \"/teamawesome/login?from=%2Fst%2F\" -w 15 -c 30",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.2728208,
      "executed": 1581507395,
      "history": [
        {
          "status": 0,
          "executed": 1581506195
        },
        {
          "status": 0,
          "executed": 1581506255
        },
        {
          "status": 0,
          "executed": 1581506315
        },
        {
          "status": 0,
          "executed": 1581506375
        },
        {
          "status": 0,
          "executed": 1581506435
        },
        {
          "status": 0,
          "executed": 1581506495
        },
        {
          "status": 0,
          "executed": 1581506555
        },
        {
          "status": 0,
          "executed": 1581506615
        },
        {
          "status": 0,
          "executed": 1581506675
        },
        {
          "status": 0,
          "executed": 1581506735
        },
        {
          "status": 0,
          "executed": 1581506795
        },
        {
          "status": 0,
          "executed": 1581506855
        },
        {
          "status": 0,
          "executed": 1581506915
        },
        {
          "status": 0,
          "executed": 1581506975
        },
        {
          "status": 0,
          "executed": 1581507035
        },
        {
          "status": 0,
          "executed": 1581507095
        },
        {
          "status": 0,
          "executed": 1581507155
        },
        {
          "status": 0,
          "executed": 1581507215
        },
        {
          "status": 0,
          "executed": 1581507275
        },
        {
          "status": 0,
          "executed": 1581507335
        },
        {
          "status": 0,
          "executed": 1581507395
        }
      ],
      "issued": 1581507433,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2920 bytes in 0.268 second response time |time=0.267566s;15.000000;30.000000;0.000000 size=2920B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507395,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.equinor.com_teamawesome",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507371,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.equinor.com -S -u \"/amteam/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.3587374,
      "executed": 1581507371,
      "history": [
        {
          "status": 0,
          "executed": 1581506171
        },
        {
          "status": 0,
          "executed": 1581506232
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506412
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506532
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        }
      ],
      "issued": 1581507409,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2953 bytes in 0.354 second response time |time=0.354203s;5.000000;10.000000;0.000000 size=2953B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507371,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_amteam",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507408,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/be/login?from=%2Fst%2F\" -w 15 -c 30",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.2710712,
      "executed": 1581507408,
      "history": [
        {
          "status": 0,
          "executed": 1581506208
        },
        {
          "status": 0,
          "executed": 1581506268
        },
        {
          "status": 0,
          "executed": 1581506328
        },
        {
          "status": 0,
          "executed": 1581506388
        },
        {
          "status": 0,
          "executed": 1581506448
        },
        {
          "status": 0,
          "executed": 1581506508
        },
        {
          "status": 0,
          "executed": 1581506568
        },
        {
          "status": 0,
          "executed": 1581506628
        },
        {
          "status": 0,
          "executed": 1581506688
        },
        {
          "status": 0,
          "executed": 1581506748
        },
        {
          "status": 0,
          "executed": 1581506808
        },
        {
          "status": 0,
          "executed": 1581506868
        },
        {
          "status": 0,
          "executed": 1581506928
        },
        {
          "status": 0,
          "executed": 1581506988
        },
        {
          "status": 0,
          "executed": 1581507048
        },
        {
          "status": 0,
          "executed": 1581507108
        },
        {
          "status": 0,
          "executed": 1581507168
        },
        {
          "status": 0,
          "executed": 1581507228
        },
        {
          "status": 0,
          "executed": 1581507288
        },
        {
          "status": 0,
          "executed": 1581507348
        },
        {
          "status": 0,
          "executed": 1581507408
        }
      ],
      "issued": 1581507446,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2858 bytes in 0.266 second response time |time=0.265584s;15.000000;30.000000;0.000000 size=2858B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507408,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_be",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507369,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/ds/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.4591835,
      "executed": 1581507369,
      "history": [
        {
          "status": 0,
          "executed": 1581506169
        },
        {
          "status": 0,
          "executed": 1581506229
        },
        {
          "status": 0,
          "executed": 1581506289
        },
        {
          "status": 0,
          "executed": 1581506349
        },
        {
          "status": 0,
          "executed": 1581506409
        },
        {
          "status": 0,
          "executed": 1581506469
        },
        {
          "status": 0,
          "executed": 1581506529
        },
        {
          "status": 0,
          "executed": 1581506589
        },
        {
          "status": 0,
          "executed": 1581506649
        },
        {
          "status": 0,
          "executed": 1581506709
        },
        {
          "status": 0,
          "executed": 1581506769
        },
        {
          "status": 0,
          "executed": 1581506829
        },
        {
          "status": 0,
          "executed": 1581506889
        },
        {
          "status": 0,
          "executed": 1581506949
        },
        {
          "status": 0,
          "executed": 1581507009
        },
        {
          "status": 0,
          "executed": 1581507069
        },
        {
          "status": 0,
          "executed": 1581507129
        },
        {
          "status": 0,
          "executed": 1581507189
        },
        {
          "status": 0,
          "executed": 1581507249
        },
        {
          "status": 0,
          "executed": 1581507309
        },
        {
          "status": 0,
          "executed": 1581507369
        }
      ],
      "issued": 1581507406,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2856 bytes in 0.454 second response time |time=0.453898s;5.000000;10.000000;0.000000 size=2856B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507369,
      "occurrences": 898,
      "occurrences_watermark": 898,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_ds",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507389,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/others/login?from=%2Fst%2F\" -w 15 -c 30",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.287733,
      "executed": 1581507389,
      "history": [
        {
          "status": 0,
          "executed": 1581506189
        },
        {
          "status": 0,
          "executed": 1581506249
        },
        {
          "status": 0,
          "executed": 1581506309
        },
        {
          "status": 0,
          "executed": 1581506369
        },
        {
          "status": 0,
          "executed": 1581506429
        },
        {
          "status": 0,
          "executed": 1581506489
        },
        {
          "status": 0,
          "executed": 1581506549
        },
        {
          "status": 0,
          "executed": 1581506609
        },
        {
          "status": 0,
          "executed": 1581506669
        },
        {
          "status": 0,
          "executed": 1581506729
        },
        {
          "status": 0,
          "executed": 1581506789
        },
        {
          "status": 0,
          "executed": 1581506849
        },
        {
          "status": 0,
          "executed": 1581506909
        },
        {
          "status": 0,
          "executed": 1581506969
        },
        {
          "status": 0,
          "executed": 1581507029
        },
        {
          "status": 0,
          "executed": 1581507089
        },
        {
          "status": 0,
          "executed": 1581507149
        },
        {
          "status": 0,
          "executed": 1581507209
        },
        {
          "status": 0,
          "executed": 1581507269
        },
        {
          "status": 0,
          "executed": 1581507329
        },
        {
          "status": 0,
          "executed": 1581507389
        }
      ],
      "issued": 1581507427,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2886 bytes in 0.282 second response time |time=0.282170s;15.000000;30.000000;0.000000 size=2886B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507389,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_others",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507396,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/pinpoint/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.5242203,
      "executed": 1581507395,
      "history": [
        {
          "status": 0,
          "executed": 1581506195
        },
        {
          "status": 0,
          "executed": 1581506255
        },
        {
          "status": 0,
          "executed": 1581506315
        },
        {
          "status": 0,
          "executed": 1581506375
        },
        {
          "status": 0,
          "executed": 1581506435
        },
        {
          "status": 0,
          "executed": 1581506495
        },
        {
          "status": 0,
          "executed": 1581506556
        },
        {
          "status": 0,
          "executed": 1581506616
        },
        {
          "status": 0,
          "executed": 1581506675
        },
        {
          "status": 0,
          "executed": 1581506735
        },
        {
          "status": 0,
          "executed": 1581506796
        },
        {
          "status": 0,
          "executed": 1581506855
        },
        {
          "status": 0,
          "executed": 1581506915
        },
        {
          "status": 0,
          "executed": 1581506975
        },
        {
          "status": 0,
          "executed": 1581507035
        },
        {
          "status": 0,
          "executed": 1581507095
        },
        {
          "status": 0,
          "executed": 1581507155
        },
        {
          "status": 0,
          "executed": 1581507215
        },
        {
          "status": 0,
          "executed": 1581507275
        },
        {
          "status": 0,
          "executed": 1581507335
        },
        {
          "status": 0,
          "executed": 1581507395
        }
      ],
      "issued": 1581507433,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2897 bytes in 0.519 second response time |time=0.518671s;5.000000;10.000000;0.000000 size=2897B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507395,
      "occurrences": 385,
      "occurrences_watermark": 385,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_pinpoint",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507371,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/public/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.5220818,
      "executed": 1581507371,
      "history": [
        {
          "status": 0,
          "executed": 1581506171
        },
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        }
      ],
      "issued": 1581507409,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2885 bytes in 0.517 second response time |time=0.516672s;5.000000;10.000000;0.000000 size=2885B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507371,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_public",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507403,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/res/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.2134377,
      "executed": 1581507403,
      "history": [
        {
          "status": 0,
          "executed": 1581506203
        },
        {
          "status": 0,
          "executed": 1581506263
        },
        {
          "status": 0,
          "executed": 1581506323
        },
        {
          "status": 0,
          "executed": 1581506383
        },
        {
          "status": 0,
          "executed": 1581506443
        },
        {
          "status": 0,
          "executed": 1581506503
        },
        {
          "status": 0,
          "executed": 1581506563
        },
        {
          "status": 0,
          "executed": 1581506623
        },
        {
          "status": 0,
          "executed": 1581506683
        },
        {
          "status": 0,
          "executed": 1581506743
        },
        {
          "status": 0,
          "executed": 1581506803
        },
        {
          "status": 0,
          "executed": 1581506863
        },
        {
          "status": 0,
          "executed": 1581506923
        },
        {
          "status": 0,
          "executed": 1581506983
        },
        {
          "status": 0,
          "executed": 1581507043
        },
        {
          "status": 0,
          "executed": 1581507103
        },
        {
          "status": 0,
          "executed": 1581507163
        },
        {
          "status": 0,
          "executed": 1581507223
        },
        {
          "status": 0,
          "executed": 1581507283
        },
        {
          "status": 0,
          "executed": 1581507343
        },
        {
          "status": 0,
          "executed": 1581507403
        }
      ],
      "issued": 1581507440,
      "output": "HTTP OK: HTTP/1.1 301 Moved Permanently - 387 bytes in 0.207 second response time |time=0.207349s;5.000000;10.000000;0.000000 size=387B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507403,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_res",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507366,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/sdp/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.4283006,
      "executed": 1581507365,
      "history": [
        {
          "status": 0,
          "executed": 1581506165
        },
        {
          "status": 0,
          "executed": 1581506225
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506405
        },
        {
          "status": 0,
          "executed": 1581506465
        },
        {
          "status": 0,
          "executed": 1581506526
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506645
        },
        {
          "status": 0,
          "executed": 1581506705
        },
        {
          "status": 0,
          "executed": 1581506765
        },
        {
          "status": 0,
          "executed": 1581506825
        },
        {
          "status": 0,
          "executed": 1581506885
        },
        {
          "status": 0,
          "executed": 1581506945
        },
        {
          "status": 0,
          "executed": 1581507005
        },
        {
          "status": 0,
          "executed": 1581507065
        },
        {
          "status": 0,
          "executed": 1581507125
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507365
        }
      ],
      "issued": 1581507403,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2915 bytes in 0.423 second response time |time=0.422839s;5.000000;10.000000;0.000000 size=2915B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507365,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_sdp",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507361,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/sentry/login?from=%2Fst%2F\" -w 15 -c 30",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.2159279,
      "executed": 1581507361,
      "history": [
        {
          "status": 0,
          "executed": 1581506160
        },
        {
          "status": 0,
          "executed": 1581506220
        },
        {
          "status": 0,
          "executed": 1581506280
        },
        {
          "status": 0,
          "executed": 1581506340
        },
        {
          "status": 0,
          "executed": 1581506401
        },
        {
          "status": 0,
          "executed": 1581506461
        },
        {
          "status": 0,
          "executed": 1581506521
        },
        {
          "status": 0,
          "executed": 1581506580
        },
        {
          "status": 0,
          "executed": 1581506641
        },
        {
          "status": 0,
          "executed": 1581506700
        },
        {
          "status": 0,
          "executed": 1581506760
        },
        {
          "status": 0,
          "executed": 1581506820
        },
        {
          "status": 0,
          "executed": 1581506880
        },
        {
          "status": 0,
          "executed": 1581506940
        },
        {
          "status": 0,
          "executed": 1581507001
        },
        {
          "status": 0,
          "executed": 1581507060
        },
        {
          "status": 0,
          "executed": 1581507120
        },
        {
          "status": 0,
          "executed": 1581507180
        },
        {
          "status": 0,
          "executed": 1581507241
        },
        {
          "status": 0,
          "executed": 1581507300
        },
        {
          "status": 0,
          "executed": 1581507361
        }
      ],
      "issued": 1581507399,
      "output": "HTTP OK: HTTP/1.1 301 Moved Permanently - 390 bytes in 0.210 second response time |time=0.210176s;15.000000;30.000000;0.000000 size=390B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507361,
      "occurrences": 1318,
      "occurrences_watermark": 1318,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_sentry",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507389,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/sigma/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.2130068,
      "executed": 1581507389,
      "history": [
        {
          "status": 0,
          "executed": 1581506188
        },
        {
          "status": 0,
          "executed": 1581506248
        },
        {
          "status": 0,
          "executed": 1581506308
        },
        {
          "status": 0,
          "executed": 1581506368
        },
        {
          "status": 0,
          "executed": 1581506428
        },
        {
          "status": 0,
          "executed": 1581506488
        },
        {
          "status": 0,
          "executed": 1581506548
        },
        {
          "status": 0,
          "executed": 1581506609
        },
        {
          "status": 0,
          "executed": 1581506668
        },
        {
          "status": 0,
          "executed": 1581506728
        },
        {
          "status": 0,
          "executed": 1581506788
        },
        {
          "status": 0,
          "executed": 1581506848
        },
        {
          "status": 0,
          "executed": 1581506908
        },
        {
          "status": 0,
          "executed": 1581506968
        },
        {
          "status": 0,
          "executed": 1581507028
        },
        {
          "status": 0,
          "executed": 1581507088
        },
        {
          "status": 0,
          "executed": 1581507148
        },
        {
          "status": 0,
          "executed": 1581507208
        },
        {
          "status": 0,
          "executed": 1581507268
        },
        {
          "status": 0,
          "executed": 1581507328
        },
        {
          "status": 0,
          "executed": 1581507389
        }
      ],
      "issued": 1581507427,
      "output": "HTTP OK: HTTP/1.1 301 Moved Permanently - 389 bytes in 0.208 second response time |time=0.207551s;5.000000;10.000000;0.000000 size=389B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507389,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_sigma",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507399,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/st/login?from=%2Fst%2F\" -w 15 -c 30",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.2735587,
      "executed": 1581507399,
      "history": [
        {
          "status": 0,
          "executed": 1581506199
        },
        {
          "status": 0,
          "executed": 1581506259
        },
        {
          "status": 0,
          "executed": 1581506319
        },
        {
          "status": 0,
          "executed": 1581506379
        },
        {
          "status": 0,
          "executed": 1581506439
        },
        {
          "status": 0,
          "executed": 1581506499
        },
        {
          "status": 0,
          "executed": 1581506559
        },
        {
          "status": 0,
          "executed": 1581506619
        },
        {
          "status": 0,
          "executed": 1581506679
        },
        {
          "status": 0,
          "executed": 1581506739
        },
        {
          "status": 0,
          "executed": 1581506799
        },
        {
          "status": 0,
          "executed": 1581506859
        },
        {
          "status": 0,
          "executed": 1581506919
        },
        {
          "status": 0,
          "executed": 1581506979
        },
        {
          "status": 0,
          "executed": 1581507039
        },
        {
          "status": 0,
          "executed": 1581507099
        },
        {
          "status": 0,
          "executed": 1581507159
        },
        {
          "status": 0,
          "executed": 1581507219
        },
        {
          "status": 0,
          "executed": 1581507279
        },
        {
          "status": 0,
          "executed": 1581507339
        },
        {
          "status": 0,
          "executed": 1581507399
        }
      ],
      "issued": 1581507437,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2857 bytes in 0.268 second response time |time=0.268273s;15.000000;30.000000;0.000000 size=2857B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507399,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_st",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507360,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.equinor.com -S -u \"/st_resmod/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.3612568,
      "executed": 1581507359,
      "history": [
        {
          "status": 0,
          "executed": 1581506159
        },
        {
          "status": 0,
          "executed": 1581506219
        },
        {
          "status": 0,
          "executed": 1581506279
        },
        {
          "status": 0,
          "executed": 1581506339
        },
        {
          "status": 0,
          "executed": 1581506399
        },
        {
          "status": 0,
          "executed": 1581506459
        },
        {
          "status": 0,
          "executed": 1581506519
        },
        {
          "status": 0,
          "executed": 1581506579
        },
        {
          "status": 0,
          "executed": 1581506639
        },
        {
          "status": 0,
          "executed": 1581506699
        },
        {
          "status": 0,
          "executed": 1581506759
        },
        {
          "status": 0,
          "executed": 1581506819
        },
        {
          "status": 0,
          "executed": 1581506879
        },
        {
          "status": 0,
          "executed": 1581506939
        },
        {
          "status": 0,
          "executed": 1581506999
        },
        {
          "status": 0,
          "executed": 1581507059
        },
        {
          "status": 0,
          "executed": 1581507119
        },
        {
          "status": 0,
          "executed": 1581507179
        },
        {
          "status": 0,
          "executed": 1581507239
        },
        {
          "status": 0,
          "executed": 1581507299
        },
        {
          "status": 0,
          "executed": 1581507359
        }
      ],
      "issued": 1581507397,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2975 bytes in 0.356 second response time |time=0.356006s;5.000000;10.000000;0.000000 size=2975B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507359,
      "occurrences": 1318,
      "occurrences_watermark": 1318,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_st_resmod",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507372,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/tr/login?from=%2Fst%2F\" -w 15 -c 30",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "jenkins"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.2723418,
      "executed": 1581507371,
      "history": [
        {
          "status": 0,
          "executed": 1581506171
        },
        {
          "status": 0,
          "executed": 1581506232
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506412
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506532
        },
        {
          "status": 0,
          "executed": 1581506592
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507192
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        }
      ],
      "issued": 1581507409,
      "output": "HTTP OK: HTTP/1.1 200 OK - 2857 bytes in 0.267 second response time |time=0.267233s;15.000000;30.000000;0.000000 size=2857B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507371,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no_tr",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506372,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.0078447,
      "executed": 1581506372,
      "history": [
        {
          "status": 0,
          "executed": 1581470371
        },
        {
          "status": 0,
          "executed": 1581472171
        },
        {
          "status": 0,
          "executed": 1581473971
        },
        {
          "status": 0,
          "executed": 1581475771
        },
        {
          "status": 0,
          "executed": 1581477571
        },
        {
          "status": 0,
          "executed": 1581479371
        },
        {
          "status": 0,
          "executed": 1581481171
        },
        {
          "status": 0,
          "executed": 1581482971
        },
        {
          "status": 0,
          "executed": 1581484771
        },
        {
          "status": 0,
          "executed": 1581486571
        },
        {
          "status": 0,
          "executed": 1581488371
        },
        {
          "status": 0,
          "executed": 1581490171
        },
        {
          "status": 0,
          "executed": 1581491972
        },
        {
          "status": 0,
          "executed": 1581493771
        },
        {
          "status": 0,
          "executed": 1581495571
        },
        {
          "status": 0,
          "executed": 1581497371
        },
        {
          "status": 0,
          "executed": 1581499171
        },
        {
          "status": 0,
          "executed": 1581500971
        },
        {
          "status": 0,
          "executed": 1581502771
        },
        {
          "status": 0,
          "executed": 1581504571
        },
        {
          "status": 0,
          "executed": 1581506372
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506372,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507364,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.0058645,
      "executed": 1581507364,
      "history": [
        {
          "status": 0,
          "executed": 1581506164
        },
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506284
        },
        {
          "status": 0,
          "executed": 1581506344
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506524
        },
        {
          "status": 0,
          "executed": 1581506584
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506704
        },
        {
          "status": 0,
          "executed": 1581506764
        },
        {
          "status": 0,
          "executed": 1581506824
        },
        {
          "status": 0,
          "executed": 1581506884
        },
        {
          "status": 0,
          "executed": 1581506944
        },
        {
          "status": 0,
          "executed": 1581507004
        },
        {
          "status": 0,
          "executed": 1581507064
        },
        {
          "status": 0,
          "executed": 1581507124
        },
        {
          "status": 0,
          "executed": 1581507184
        },
        {
          "status": 0,
          "executed": 1581507244
        },
        {
          "status": 0,
          "executed": 1581507304
        },
        {
          "status": 0,
          "executed": 1581507364
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 120879 MiB (92.58% inode=100%);\n /dev 8003 MiB (100.00% inode=100%);\n /boot 307 MiB (61.90% inode=100%);\n /mnt/resource 30422 MiB (99.84% inode=100%);\n| /=9677MiB;104444;117500;0;130556 /dev=0MiB;6402;7202;0;8003 /boot=189MiB;396;446;0;496 /mnt/resource=48MiB;25699;28911;0;32124\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507364,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506617,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.3365971,
      "executed": 1581506617,
      "history": [
        {
          "status": 0,
          "executed": 1581434617
        },
        {
          "status": 0,
          "executed": 1581438217
        },
        {
          "status": 0,
          "executed": 1581441817
        },
        {
          "status": 0,
          "executed": 1581445417
        },
        {
          "status": 0,
          "executed": 1581449017
        },
        {
          "status": 0,
          "executed": 1581452617
        },
        {
          "status": 0,
          "executed": 1581456217
        },
        {
          "status": 0,
          "executed": 1581459817
        },
        {
          "status": 0,
          "executed": 1581463417
        },
        {
          "status": 0,
          "executed": 1581467017
        },
        {
          "status": 0,
          "executed": 1581470617
        },
        {
          "status": 0,
          "executed": 1581474217
        },
        {
          "status": 0,
          "executed": 1581477817
        },
        {
          "status": 0,
          "executed": 1581481417
        },
        {
          "status": 0,
          "executed": 1581485017
        },
        {
          "status": 0,
          "executed": 1581488617
        },
        {
          "status": 0,
          "executed": 1581492217
        },
        {
          "status": 0,
          "executed": 1581495817
        },
        {
          "status": 0,
          "executed": 1581499417
        },
        {
          "status": 0,
          "executed": 1581503017
        },
        {
          "status": 0,
          "executed": 1581506617
        }
      ],
      "issued": 1581506655,
      "output": "My certname (jenkins03.sdp.equinor.com) resolves to my IP (10.24.16.198)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506617,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507448,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1581507410,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507448,
      "history": [
        {
          "status": 0,
          "executed": 1581507048
        },
        {
          "status": 0,
          "executed": 1581507068
        },
        {
          "status": 0,
          "executed": 1581507088
        },
        {
          "status": 0,
          "executed": 1581507108
        },
        {
          "status": 0,
          "executed": 1581507128
        },
        {
          "status": 0,
          "executed": 1581507148
        },
        {
          "status": 0,
          "executed": 1581507168
        },
        {
          "status": 0,
          "executed": 1581507188
        },
        {
          "status": 0,
          "executed": 1581507208
        },
        {
          "status": 0,
          "executed": 1581507228
        },
        {
          "status": 0,
          "executed": 1581507248
        },
        {
          "status": 0,
          "executed": 1581507268
        },
        {
          "status": 0,
          "executed": 1581507288
        },
        {
          "status": 0,
          "executed": 1581507308
        },
        {
          "status": 0,
          "executed": 1581507328
        },
        {
          "status": 0,
          "executed": 1581507348
        },
        {
          "status": 0,
          "executed": 1581507368
        },
        {
          "status": 0,
          "executed": 1581507388
        },
        {
          "status": 0,
          "executed": 1581507408
        },
        {
          "status": 0,
          "executed": 1581507428
        },
        {
          "status": 0,
          "executed": 1581507448
        }
      ],
      "issued": 1581507448,
      "output": "Keepalive last sent from jenkins03.sdp.equinor.com at 2020-02-12 11:36:50 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507448,
      "occurrences": 55709,
      "occurrences_watermark": 55709,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507387,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.0078694,
      "executed": 1581507387,
      "history": [
        {
          "status": 0,
          "executed": 1581506187
        },
        {
          "status": 0,
          "executed": 1581506247
        },
        {
          "status": 0,
          "executed": 1581506307
        },
        {
          "status": 0,
          "executed": 1581506367
        },
        {
          "status": 0,
          "executed": 1581506427
        },
        {
          "status": 0,
          "executed": 1581506487
        },
        {
          "status": 0,
          "executed": 1581506547
        },
        {
          "status": 0,
          "executed": 1581506607
        },
        {
          "status": 0,
          "executed": 1581506667
        },
        {
          "status": 0,
          "executed": 1581506727
        },
        {
          "status": 0,
          "executed": 1581506787
        },
        {
          "status": 0,
          "executed": 1581506847
        },
        {
          "status": 0,
          "executed": 1581506907
        },
        {
          "status": 0,
          "executed": 1581506967
        },
        {
          "status": 0,
          "executed": 1581507027
        },
        {
          "status": 0,
          "executed": 1581507087
        },
        {
          "status": 0,
          "executed": 1581507147
        },
        {
          "status": 0,
          "executed": 1581507207
        },
        {
          "status": 0,
          "executed": 1581507267
        },
        {
          "status": 0,
          "executed": 1581507327
        },
        {
          "status": 0,
          "executed": 1581507387
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.09, 0.09, 0.08|load1=0.090;80.000;90.000;0; load5=0.090;80.000;90.000;0; load15=0.080;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507387,
      "occurrences": 18568,
      "occurrences_watermark": 18568,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507393,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "zi-linapp1110.statoil.no",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "00:0d:3a:b1:7f:76",
              "addresses": [
                "10.24.16.198/21",
                "fe80::20d:3aff:feb1:7f76/64"
              ]
            },
            {
              "name": "br-59a73a37e2b0",
              "mac": "02:42:4d:99:a4:d8",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:4dff:fe99:a4d8/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:02:e3:d9:35",
              "addresses": [
                "172.17.0.1/16",
                "fe80::42:2ff:fee3:d935/64"
              ]
            },
            {
              "name": "br-27efd8dd2a6f",
              "mac": "02:42:f3:00:4c:b1",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:f3ff:fe00:4cb1/64"
              ]
            },
            {
              "name": "veth74eb366",
              "mac": "66:96:fe:83:4b:f0",
              "addresses": [
                "fe80::6496:feff:fe83:4bf0/64"
              ]
            },
            {
              "name": "veth5a3e8bc",
              "mac": "ea:d3:ab:2b:8a:68",
              "addresses": [
                "fe80::e8d3:abff:fe2b:8a68/64"
              ]
            },
            {
              "name": "br-c5c002624d75",
              "mac": "02:42:0f:e1:5a:55",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:fff:fee1:5a55/64"
              ]
            },
            {
              "name": "veth877917f",
              "mac": "ba:18:4c:39:5b:86",
              "addresses": [
                "fe80::b818:4cff:fe39:5b86/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "jenkins",
        "entity:jenkins03.sdp.equinor.com"
      ],
      "last_seen": 1580296034,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "jenkins03.sdp.equinor.com",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.0053239,
      "executed": 1581507393,
      "history": [
        {
          "status": 0,
          "executed": 1581506193
        },
        {
          "status": 0,
          "executed": 1581506253
        },
        {
          "status": 0,
          "executed": 1581506313
        },
        {
          "status": 0,
          "executed": 1581506373
        },
        {
          "status": 0,
          "executed": 1581506433
        },
        {
          "status": 0,
          "executed": 1581506493
        },
        {
          "status": 0,
          "executed": 1581506553
        },
        {
          "status": 0,
          "executed": 1581506613
        },
        {
          "status": 0,
          "executed": 1581506673
        },
        {
          "status": 0,
          "executed": 1581506733
        },
        {
          "status": 0,
          "executed": 1581506793
        },
        {
          "status": 0,
          "executed": 1581506853
        },
        {
          "status": 0,
          "executed": 1581506913
        },
        {
          "status": 0,
          "executed": 1581506973
        },
        {
          "status": 0,
          "executed": 1581507033
        },
        {
          "status": 0,
          "executed": 1581507093
        },
        {
          "status": 0,
          "executed": 1581507153
        },
        {
          "status": 0,
          "executed": 1581507213
        },
        {
          "status": 0,
          "executed": 1581507273
        },
        {
          "status": 0,
          "executed": 1581507333
        },
        {
          "status": 0,
          "executed": 1581507393
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 0% free (0 MB out of 0 MB) - Swap is either disabled, not present, or of zero size. |swap=0MB;0;0;0;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507393,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507451,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "lt-lx947113",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "enp0s31f6",
              "mac": "10:e7:c6:a8:af:43",
              "addresses": null
            },
            {
              "name": "wlp3s0",
              "mac": "00:24:d6:f9:82:6a",
              "addresses": [
                "10.54.44.115/23",
                "fe80::b39f:348c:9fbb:5881/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "system",
        "entity:lt-lx947113"
      ],
      "last_seen": 1581500880,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "lt-lx947113",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "check-cpu.rb -w 75 -c 90",
      "handlers": [
        "slack"
      ],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": [
        "cpu-checks-plugins",
        "sensu-ruby-runtime"
      ],
      "subscriptions": [
        "system"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 5.085656735,
      "executed": 1581507446,
      "history": [
        {
          "status": 0,
          "executed": 1581506246
        },
        {
          "status": 0,
          "executed": 1581506306
        },
        {
          "status": 0,
          "executed": 1581506366
        },
        {
          "status": 0,
          "executed": 1581506426
        },
        {
          "status": 0,
          "executed": 1581506486
        },
        {
          "status": 0,
          "executed": 1581506546
        },
        {
          "status": 1,
          "executed": 1581506606
        },
        {
          "status": 0,
          "executed": 1581506666
        },
        {
          "status": 0,
          "executed": 1581506726
        },
        {
          "status": 0,
          "executed": 1581506786
        },
        {
          "status": 0,
          "executed": 1581506846
        },
        {
          "status": 0,
          "executed": 1581506906
        },
        {
          "status": 0,
          "executed": 1581506966
        },
        {
          "status": 0,
          "executed": 1581507026
        },
        {
          "status": 0,
          "executed": 1581507086
        },
        {
          "status": 0,
          "executed": 1581507146
        },
        {
          "status": 0,
          "executed": 1581507206
        },
        {
          "status": 0,
          "executed": 1581507266
        },
        {
          "status": 0,
          "executed": 1581507326
        },
        {
          "status": 0,
          "executed": 1581507386
        },
        {
          "status": 0,
          "executed": 1581507446
        }
      ],
      "issued": 1581507446,
      "output": "CheckCPU TOTAL OK: total=25.88 user=19.89 nice=0.0 system=5.99 idle=69.36 iowait=4.76 irq=0.0 softirq=0.0 steal=0.0 guest=0.0 guest_nice=0.0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 9,
      "last_ok": 1581507446,
      "occurrences": 14,
      "occurrences_watermark": 14,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "check-cpu",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507439,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "lt-lx947113",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "enp0s31f6",
              "mac": "10:e7:c6:a8:af:43",
              "addresses": null
            },
            {
              "name": "wlp3s0",
              "mac": "00:24:d6:f9:82:6a",
              "addresses": [
                "10.54.44.115/23",
                "fe80::b39f:348c:9fbb:5881/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "system",
        "entity:lt-lx947113"
      ],
      "last_seen": 1581507439,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "lt-lx947113",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507439,
      "history": [
        {
          "status": 0,
          "executed": 1581507039
        },
        {
          "status": 0,
          "executed": 1581507059
        },
        {
          "status": 0,
          "executed": 1581507079
        },
        {
          "status": 0,
          "executed": 1581507099
        },
        {
          "status": 0,
          "executed": 1581507119
        },
        {
          "status": 0,
          "executed": 1581507139
        },
        {
          "status": 0,
          "executed": 1581507159
        },
        {
          "status": 0,
          "executed": 1581507179
        },
        {
          "status": 0,
          "executed": 1581507199
        },
        {
          "status": 0,
          "executed": 1581507219
        },
        {
          "status": 0,
          "executed": 1581507239
        },
        {
          "status": 0,
          "executed": 1581507259
        },
        {
          "status": 0,
          "executed": 1581507279
        },
        {
          "status": 0,
          "executed": 1581507299
        },
        {
          "status": 0,
          "executed": 1581507319
        },
        {
          "status": 0,
          "executed": 1581507339
        },
        {
          "status": 0,
          "executed": 1581507359
        },
        {
          "status": 0,
          "executed": 1581507379
        },
        {
          "status": 0,
          "executed": 1581507399
        },
        {
          "status": 0,
          "executed": 1581507419
        },
        {
          "status": 0,
          "executed": 1581507439
        }
      ],
      "issued": 1581507439,
      "output": "Keepalive last sent from lt-lx947113 at 2020-02-12 11:37:19 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507439,
      "occurrences": 335,
      "occurrences_watermark": 599,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1034",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:7e:58:55:13:58",
              "addresses": [
                "10.36.6.116/21",
                "fe80::87e:58ff:fe55:1358/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:dc:e7:95",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:dc:e7:95",
              "addresses": null
            },
            {
              "name": "docker0",
              "mac": "02:42:66:5d:c4:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-34a9952f1fa4",
              "mac": "02:42:78:e9:c3:fc",
              "addresses": [
                "172.22.0.1/16"
              ]
            },
            {
              "name": "br-28c332e88d8a",
              "mac": "02:42:02:b6:81:58",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:2ff:feb6:8158/64"
              ]
            },
            {
              "name": "veth4fdf2de",
              "mac": "2e:16:b4:9e:2c:80",
              "addresses": [
                "fe80::2c16:b4ff:fe9e:2c80/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:mon01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386404,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "mon01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006781571,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1034",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:7e:58:55:13:58",
              "addresses": [
                "10.36.6.116/21",
                "fe80::87e:58ff:fe55:1358/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:dc:e7:95",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:dc:e7:95",
              "addresses": null
            },
            {
              "name": "docker0",
              "mac": "02:42:66:5d:c4:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-34a9952f1fa4",
              "mac": "02:42:78:e9:c3:fc",
              "addresses": [
                "172.22.0.1/16"
              ]
            },
            {
              "name": "br-28c332e88d8a",
              "mac": "02:42:02:b6:81:58",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:2ff:feb6:8158/64"
              ]
            },
            {
              "name": "veth4fdf2de",
              "mac": "2e:16:b4:9e:2c:80",
              "addresses": [
                "fe80::2c16:b4ff:fe9e:2c80/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:mon01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386404,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "mon01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.005030441,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 41005 MiB (80.10% inode=99%);\n /dev 1855 MiB (100.00% inode=100%);\n /data 23048 MiB (45.03% inode=99%);\n| /=10183MiB;40950;46069;0;51188 /dev=0MiB;1484;1669;0;1855 /data=28125MiB;40939;46056;0;51174\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506655,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1034",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:7e:58:55:13:58",
              "addresses": [
                "10.36.6.116/21",
                "fe80::87e:58ff:fe55:1358/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:dc:e7:95",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:dc:e7:95",
              "addresses": null
            },
            {
              "name": "docker0",
              "mac": "02:42:66:5d:c4:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-34a9952f1fa4",
              "mac": "02:42:78:e9:c3:fc",
              "addresses": [
                "172.22.0.1/16"
              ]
            },
            {
              "name": "br-28c332e88d8a",
              "mac": "02:42:02:b6:81:58",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:2ff:feb6:8158/64"
              ]
            },
            {
              "name": "veth4fdf2de",
              "mac": "2e:16:b4:9e:2c:80",
              "addresses": [
                "fe80::2c16:b4ff:fe9e:2c80/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:mon01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386404,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "mon01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.349493172,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (mon01.prod.sdp.statoil.no) resolves to my IP (10.36.6.116)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507444,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1034",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:7e:58:55:13:58",
              "addresses": [
                "10.36.6.116/21",
                "fe80::87e:58ff:fe55:1358/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:dc:e7:95",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:dc:e7:95",
              "addresses": null
            },
            {
              "name": "docker0",
              "mac": "02:42:66:5d:c4:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-34a9952f1fa4",
              "mac": "02:42:78:e9:c3:fc",
              "addresses": [
                "172.22.0.1/16"
              ]
            },
            {
              "name": "br-28c332e88d8a",
              "mac": "02:42:02:b6:81:58",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:2ff:feb6:8158/64"
              ]
            },
            {
              "name": "veth4fdf2de",
              "mac": "2e:16:b4:9e:2c:80",
              "addresses": [
                "fe80::2c16:b4ff:fe9e:2c80/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:mon01.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507444,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "mon01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507444,
      "history": [
        {
          "status": 0,
          "executed": 1581507044
        },
        {
          "status": 0,
          "executed": 1581507064
        },
        {
          "status": 0,
          "executed": 1581507084
        },
        {
          "status": 0,
          "executed": 1581507104
        },
        {
          "status": 0,
          "executed": 1581507124
        },
        {
          "status": 0,
          "executed": 1581507144
        },
        {
          "status": 0,
          "executed": 1581507164
        },
        {
          "status": 0,
          "executed": 1581507184
        },
        {
          "status": 0,
          "executed": 1581507205
        },
        {
          "status": 0,
          "executed": 1581507224
        },
        {
          "status": 0,
          "executed": 1581507244
        },
        {
          "status": 0,
          "executed": 1581507264
        },
        {
          "status": 0,
          "executed": 1581507284
        },
        {
          "status": 0,
          "executed": 1581507304
        },
        {
          "status": 0,
          "executed": 1581507324
        },
        {
          "status": 0,
          "executed": 1581507344
        },
        {
          "status": 0,
          "executed": 1581507364
        },
        {
          "status": 0,
          "executed": 1581507384
        },
        {
          "status": 0,
          "executed": 1581507404
        },
        {
          "status": 0,
          "executed": 1581507424
        },
        {
          "status": 0,
          "executed": 1581507444
        }
      ],
      "issued": 1581507444,
      "output": "Keepalive last sent from mon01.prod.sdp.statoil.no at 2020-02-12 11:37:24 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507444,
      "occurrences": 55710,
      "occurrences_watermark": 55710,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507424,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1034",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:7e:58:55:13:58",
              "addresses": [
                "10.36.6.116/21",
                "fe80::87e:58ff:fe55:1358/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:dc:e7:95",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:dc:e7:95",
              "addresses": null
            },
            {
              "name": "docker0",
              "mac": "02:42:66:5d:c4:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-34a9952f1fa4",
              "mac": "02:42:78:e9:c3:fc",
              "addresses": [
                "172.22.0.1/16"
              ]
            },
            {
              "name": "br-28c332e88d8a",
              "mac": "02:42:02:b6:81:58",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:2ff:feb6:8158/64"
              ]
            },
            {
              "name": "veth4fdf2de",
              "mac": "2e:16:b4:9e:2c:80",
              "addresses": [
                "fe80::2c16:b4ff:fe9e:2c80/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:mon01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386404,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "mon01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.007020332,
      "executed": 1581507424,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506524
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506704
        },
        {
          "status": 0,
          "executed": 1581506764
        },
        {
          "status": 0,
          "executed": 1581506824
        },
        {
          "status": 0,
          "executed": 1581506884
        },
        {
          "status": 0,
          "executed": 1581506944
        },
        {
          "status": 0,
          "executed": 1581507004
        },
        {
          "status": 0,
          "executed": 1581507064
        },
        {
          "status": 0,
          "executed": 1581507124
        },
        {
          "status": 0,
          "executed": 1581507184
        },
        {
          "status": 0,
          "executed": 1581507244
        },
        {
          "status": 0,
          "executed": 1581507304
        },
        {
          "status": 0,
          "executed": 1581507364
        },
        {
          "status": 0,
          "executed": 1581507424
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.09, 0.13, 0.16|load1=0.090;80.000;90.000;0; load5=0.130;80.000;90.000;0; load15=0.160;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507424,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1034",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:7e:58:55:13:58",
              "addresses": [
                "10.36.6.116/21",
                "fe80::87e:58ff:fe55:1358/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:dc:e7:95",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:dc:e7:95",
              "addresses": null
            },
            {
              "name": "docker0",
              "mac": "02:42:66:5d:c4:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-34a9952f1fa4",
              "mac": "02:42:78:e9:c3:fc",
              "addresses": [
                "172.22.0.1/16"
              ]
            },
            {
              "name": "br-28c332e88d8a",
              "mac": "02:42:02:b6:81:58",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:2ff:feb6:8158/64"
              ]
            },
            {
              "name": "veth4fdf2de",
              "mac": "2e:16:b4:9e:2c:80",
              "addresses": [
                "fe80::2c16:b4ff:fe9e:2c80/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:mon01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386404,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "mon01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006348981,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 97% free (1977 MB out of 2047 MB) |swap=1977MB;1023;409;0;2047\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507451,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1122",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "06:29:11:5f:b7:ea",
              "addresses": [
                "10.36.36.183/21",
                "fe80::429:11ff:fe5f:b7ea/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:aa:84:92:5f",
              "addresses": [
                "172.17.0.1/16"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "test",
        "entity:test01.dev.sdp.statoil.no"
      ],
      "last_seen": 1581507451,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "test01.dev.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507451,
      "history": [
        {
          "status": 0,
          "executed": 1581507052
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507092
        },
        {
          "status": 0,
          "executed": 1581507111
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507152
        },
        {
          "status": 0,
          "executed": 1581507171
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507212
        },
        {
          "status": 0,
          "executed": 1581507232
        },
        {
          "status": 0,
          "executed": 1581507252
        },
        {
          "status": 0,
          "executed": 1581507272
        },
        {
          "status": 0,
          "executed": 1581507291
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507332
        },
        {
          "status": 0,
          "executed": 1581507351
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507392
        },
        {
          "status": 0,
          "executed": 1581507411
        },
        {
          "status": 0,
          "executed": 1581507431
        },
        {
          "status": 0,
          "executed": 1581507451
        }
      ],
      "issued": 1581507451,
      "output": "Keepalive last sent from test01.dev.sdp.statoil.no at 2020-02-12 11:37:31 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507451,
      "occurrences": 55710,
      "occurrences_watermark": 55710,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1024",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:33:c4:b0:11:9e",
              "addresses": [
                "10.36.6.197/21",
                "fe80::833:c4ff:feb0:119e/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:55:c5:c8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:55:c5:c8",
              "addresses": null
            },
            {
              "name": "br-18929e65f74d",
              "mac": "02:42:ed:b3:19:21",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:edff:feb3:1921/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:8c:f5:18:80",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5d4d8365c8bd",
              "mac": "02:42:3b:97:d9:4b",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:3bff:fe97:d94b/64"
              ]
            },
            {
              "name": "veth648cf6b",
              "mac": "92:c0:11:a4:88:9b",
              "addresses": [
                "fe80::90c0:11ff:fea4:889b/64"
              ]
            },
            {
              "name": "veth89b7e3d",
              "mac": "c2:ef:f3:f4:cc:f4",
              "addresses": [
                "fe80::c0ef:f3ff:fef4:ccf4/64"
              ]
            },
            {
              "name": "veth0a13c86",
              "mac": "0a:98:52:b7:95:0d",
              "addresses": [
                "fe80::898:52ff:feb7:950d/64"
              ]
            },
            {
              "name": "veth6ab1155",
              "mac": "32:b5:96:92:a6:87",
              "addresses": [
                "fe80::30b5:96ff:fe92:a687/64"
              ]
            },
            {
              "name": "veth63854c2",
              "mac": "06:5a:67:d2:d7:e4",
              "addresses": [
                "fe80::45a:67ff:fed2:d7e4/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:tig01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580295789,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "tig01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006473411,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1024",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:33:c4:b0:11:9e",
              "addresses": [
                "10.36.6.197/21",
                "fe80::833:c4ff:feb0:119e/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:55:c5:c8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:55:c5:c8",
              "addresses": null
            },
            {
              "name": "br-18929e65f74d",
              "mac": "02:42:ed:b3:19:21",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:edff:feb3:1921/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:8c:f5:18:80",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5d4d8365c8bd",
              "mac": "02:42:3b:97:d9:4b",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:3bff:fe97:d94b/64"
              ]
            },
            {
              "name": "veth648cf6b",
              "mac": "92:c0:11:a4:88:9b",
              "addresses": [
                "fe80::90c0:11ff:fea4:889b/64"
              ]
            },
            {
              "name": "veth89b7e3d",
              "mac": "c2:ef:f3:f4:cc:f4",
              "addresses": [
                "fe80::c0ef:f3ff:fef4:ccf4/64"
              ]
            },
            {
              "name": "veth0a13c86",
              "mac": "0a:98:52:b7:95:0d",
              "addresses": [
                "fe80::898:52ff:feb7:950d/64"
              ]
            },
            {
              "name": "veth6ab1155",
              "mac": "32:b5:96:92:a6:87",
              "addresses": [
                "fe80::30b5:96ff:fe92:a687/64"
              ]
            },
            {
              "name": "veth63854c2",
              "mac": "06:5a:67:d2:d7:e4",
              "addresses": [
                "fe80::45a:67ff:fed2:d7e4/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:tig01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580295789,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "tig01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004889689,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 27178 MiB (53.09% inode=99%);\n /dev 3871 MiB (100.00% inode=100%);\n /data 357298 MiB (93.40% inode=100%);\n /dockerroot 80048 MiB (83.79% inode=98%);\n| /=24009MiB;40950;46069;0;51188 /dev=0MiB;3096;3483;0;3871 /data=25244MiB;322431;362735;0;403039 /dockerroot=15476MiB;80528;90594;0;100660\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506655,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1024",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:33:c4:b0:11:9e",
              "addresses": [
                "10.36.6.197/21",
                "fe80::833:c4ff:feb0:119e/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:55:c5:c8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:55:c5:c8",
              "addresses": null
            },
            {
              "name": "br-18929e65f74d",
              "mac": "02:42:ed:b3:19:21",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:edff:feb3:1921/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:8c:f5:18:80",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5d4d8365c8bd",
              "mac": "02:42:3b:97:d9:4b",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:3bff:fe97:d94b/64"
              ]
            },
            {
              "name": "veth648cf6b",
              "mac": "92:c0:11:a4:88:9b",
              "addresses": [
                "fe80::90c0:11ff:fea4:889b/64"
              ]
            },
            {
              "name": "veth89b7e3d",
              "mac": "c2:ef:f3:f4:cc:f4",
              "addresses": [
                "fe80::c0ef:f3ff:fef4:ccf4/64"
              ]
            },
            {
              "name": "veth0a13c86",
              "mac": "0a:98:52:b7:95:0d",
              "addresses": [
                "fe80::898:52ff:feb7:950d/64"
              ]
            },
            {
              "name": "veth6ab1155",
              "mac": "32:b5:96:92:a6:87",
              "addresses": [
                "fe80::30b5:96ff:fe92:a687/64"
              ]
            },
            {
              "name": "veth63854c2",
              "mac": "06:5a:67:d2:d7:e4",
              "addresses": [
                "fe80::45a:67ff:fed2:d7e4/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:tig01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580295789,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "tig01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.359471085,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (tig01.prod.sdp.statoil.no) resolves to my IP (10.36.6.197)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507449,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1024",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:33:c4:b0:11:9e",
              "addresses": [
                "10.36.6.197/21",
                "fe80::833:c4ff:feb0:119e/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:55:c5:c8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:55:c5:c8",
              "addresses": null
            },
            {
              "name": "br-18929e65f74d",
              "mac": "02:42:ed:b3:19:21",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:edff:feb3:1921/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:8c:f5:18:80",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5d4d8365c8bd",
              "mac": "02:42:3b:97:d9:4b",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:3bff:fe97:d94b/64"
              ]
            },
            {
              "name": "veth648cf6b",
              "mac": "92:c0:11:a4:88:9b",
              "addresses": [
                "fe80::90c0:11ff:fea4:889b/64"
              ]
            },
            {
              "name": "veth89b7e3d",
              "mac": "c2:ef:f3:f4:cc:f4",
              "addresses": [
                "fe80::c0ef:f3ff:fef4:ccf4/64"
              ]
            },
            {
              "name": "veth0a13c86",
              "mac": "0a:98:52:b7:95:0d",
              "addresses": [
                "fe80::898:52ff:feb7:950d/64"
              ]
            },
            {
              "name": "veth6ab1155",
              "mac": "32:b5:96:92:a6:87",
              "addresses": [
                "fe80::30b5:96ff:fe92:a687/64"
              ]
            },
            {
              "name": "veth63854c2",
              "mac": "06:5a:67:d2:d7:e4",
              "addresses": [
                "fe80::45a:67ff:fed2:d7e4/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:tig01.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507449,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "tig01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507449,
      "history": [
        {
          "status": 0,
          "executed": 1581507049
        },
        {
          "status": 0,
          "executed": 1581507069
        },
        {
          "status": 0,
          "executed": 1581507089
        },
        {
          "status": 0,
          "executed": 1581507109
        },
        {
          "status": 0,
          "executed": 1581507129
        },
        {
          "status": 0,
          "executed": 1581507149
        },
        {
          "status": 0,
          "executed": 1581507169
        },
        {
          "status": 0,
          "executed": 1581507189
        },
        {
          "status": 0,
          "executed": 1581507209
        },
        {
          "status": 0,
          "executed": 1581507229
        },
        {
          "status": 0,
          "executed": 1581507249
        },
        {
          "status": 0,
          "executed": 1581507269
        },
        {
          "status": 0,
          "executed": 1581507289
        },
        {
          "status": 0,
          "executed": 1581507309
        },
        {
          "status": 0,
          "executed": 1581507329
        },
        {
          "status": 0,
          "executed": 1581507349
        },
        {
          "status": 0,
          "executed": 1581507369
        },
        {
          "status": 0,
          "executed": 1581507389
        },
        {
          "status": 0,
          "executed": 1581507409
        },
        {
          "status": 0,
          "executed": 1581507429
        },
        {
          "status": 0,
          "executed": 1581507449
        }
      ],
      "issued": 1581507449,
      "output": "Keepalive last sent from tig01.prod.sdp.statoil.no at 2020-02-12 11:37:29 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507449,
      "occurrences": 55710,
      "occurrences_watermark": 55710,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507424,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1024",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:33:c4:b0:11:9e",
              "addresses": [
                "10.36.6.197/21",
                "fe80::833:c4ff:feb0:119e/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:55:c5:c8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:55:c5:c8",
              "addresses": null
            },
            {
              "name": "br-18929e65f74d",
              "mac": "02:42:ed:b3:19:21",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:edff:feb3:1921/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:8c:f5:18:80",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5d4d8365c8bd",
              "mac": "02:42:3b:97:d9:4b",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:3bff:fe97:d94b/64"
              ]
            },
            {
              "name": "veth648cf6b",
              "mac": "92:c0:11:a4:88:9b",
              "addresses": [
                "fe80::90c0:11ff:fea4:889b/64"
              ]
            },
            {
              "name": "veth89b7e3d",
              "mac": "c2:ef:f3:f4:cc:f4",
              "addresses": [
                "fe80::c0ef:f3ff:fef4:ccf4/64"
              ]
            },
            {
              "name": "veth0a13c86",
              "mac": "0a:98:52:b7:95:0d",
              "addresses": [
                "fe80::898:52ff:feb7:950d/64"
              ]
            },
            {
              "name": "veth6ab1155",
              "mac": "32:b5:96:92:a6:87",
              "addresses": [
                "fe80::30b5:96ff:fe92:a687/64"
              ]
            },
            {
              "name": "veth63854c2",
              "mac": "06:5a:67:d2:d7:e4",
              "addresses": [
                "fe80::45a:67ff:fed2:d7e4/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:tig01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580295789,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "tig01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006858336,
      "executed": 1581507424,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506524
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506704
        },
        {
          "status": 0,
          "executed": 1581506764
        },
        {
          "status": 0,
          "executed": 1581506824
        },
        {
          "status": 0,
          "executed": 1581506884
        },
        {
          "status": 0,
          "executed": 1581506944
        },
        {
          "status": 0,
          "executed": 1581507004
        },
        {
          "status": 0,
          "executed": 1581507064
        },
        {
          "status": 0,
          "executed": 1581507124
        },
        {
          "status": 0,
          "executed": 1581507184
        },
        {
          "status": 0,
          "executed": 1581507244
        },
        {
          "status": 0,
          "executed": 1581507304
        },
        {
          "status": 0,
          "executed": 1581507364
        },
        {
          "status": 0,
          "executed": 1581507424
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.25, 0.35, 0.39|load1=0.250;80.000;90.000;0; load5=0.350;80.000;90.000;0; load15=0.390;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507424,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1024",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:33:c4:b0:11:9e",
              "addresses": [
                "10.36.6.197/21",
                "fe80::833:c4ff:feb0:119e/64"
              ]
            },
            {
              "name": "virbr0",
              "mac": "52:54:00:55:c5:c8",
              "addresses": [
                "192.168.122.1/24"
              ]
            },
            {
              "name": "virbr0-nic",
              "mac": "52:54:00:55:c5:c8",
              "addresses": null
            },
            {
              "name": "br-18929e65f74d",
              "mac": "02:42:ed:b3:19:21",
              "addresses": [
                "172.22.0.1/16",
                "fe80::42:edff:feb3:1921/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:8c:f5:18:80",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-5d4d8365c8bd",
              "mac": "02:42:3b:97:d9:4b",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:3bff:fe97:d94b/64"
              ]
            },
            {
              "name": "veth648cf6b",
              "mac": "92:c0:11:a4:88:9b",
              "addresses": [
                "fe80::90c0:11ff:fea4:889b/64"
              ]
            },
            {
              "name": "veth89b7e3d",
              "mac": "c2:ef:f3:f4:cc:f4",
              "addresses": [
                "fe80::c0ef:f3ff:fef4:ccf4/64"
              ]
            },
            {
              "name": "veth0a13c86",
              "mac": "0a:98:52:b7:95:0d",
              "addresses": [
                "fe80::898:52ff:feb7:950d/64"
              ]
            },
            {
              "name": "veth6ab1155",
              "mac": "32:b5:96:92:a6:87",
              "addresses": [
                "fe80::30b5:96ff:fe92:a687/64"
              ]
            },
            {
              "name": "veth63854c2",
              "mac": "06:5a:67:d2:d7:e4",
              "addresses": [
                "fe80::45a:67ff:fed2:d7e4/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:tig01.prod.sdp.statoil.no"
      ],
      "last_seen": 1580295789,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "tig01.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004398545,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 100% free (10046 MB out of 10047 MB) |swap=10046MB;5023;2009;0;10047\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp02.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:39:69",
              "addresses": [
                "143.97.90.198/24",
                "fe80::250:56ff:fe85:3969/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm02.prod.sdp.statoil.no"
      ],
      "last_seen": 1581428320,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.007585369,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp02.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:39:69",
              "addresses": [
                "143.97.90.198/24",
                "fe80::250:56ff:fe85:3969/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm02.prod.sdp.statoil.no"
      ],
      "last_seen": 1581428320,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006623687,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 24677 MiB (88.54% inode=93%);\n /dev 15992 MiB (100.00% inode=100%);\n /boot 283 MiB (63.50% inode=100%);\n /tmp 7473 MiB (99.51% inode=100%);\n /var 12426 MiB (61.88% inode=91%);\n /data 271110 MiB (56.69% inode=97%);\n| /=3192MiB;23507;26445;0;29384 /dev=0MiB;12793;14392;0;15992 /boot=163MiB;380;428;0;476 /tmp=36MiB;6348;7141;0;7935 /var=7653MiB;16830;18934;0;21038 /data=207105MiB;403065;453448;0;503832\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18567,
      "occurrences_watermark": 18567,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506655,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp02.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:39:69",
              "addresses": [
                "143.97.90.198/24",
                "fe80::250:56ff:fe85:3969/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm02.prod.sdp.statoil.no"
      ],
      "last_seen": 1581428320,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.373929834,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (vmm02.prod.sdp.statoil.no) resolves to my IP (143.97.90.198)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507440,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp02.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:39:69",
              "addresses": [
                "143.97.90.198/24",
                "fe80::250:56ff:fe85:3969/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm02.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507440,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507440,
      "history": [
        {
          "status": 0,
          "executed": 1581507040
        },
        {
          "status": 0,
          "executed": 1581507060
        },
        {
          "status": 0,
          "executed": 1581507080
        },
        {
          "status": 0,
          "executed": 1581507100
        },
        {
          "status": 0,
          "executed": 1581507120
        },
        {
          "status": 0,
          "executed": 1581507140
        },
        {
          "status": 0,
          "executed": 1581507160
        },
        {
          "status": 0,
          "executed": 1581507180
        },
        {
          "status": 0,
          "executed": 1581507200
        },
        {
          "status": 0,
          "executed": 1581507220
        },
        {
          "status": 0,
          "executed": 1581507240
        },
        {
          "status": 0,
          "executed": 1581507260
        },
        {
          "status": 0,
          "executed": 1581507280
        },
        {
          "status": 0,
          "executed": 1581507300
        },
        {
          "status": 0,
          "executed": 1581507320
        },
        {
          "status": 0,
          "executed": 1581507340
        },
        {
          "status": 0,
          "executed": 1581507360
        },
        {
          "status": 0,
          "executed": 1581507380
        },
        {
          "status": 0,
          "executed": 1581507400
        },
        {
          "status": 0,
          "executed": 1581507420
        },
        {
          "status": 0,
          "executed": 1581507440
        }
      ],
      "issued": 1581507440,
      "output": "Keepalive last sent from vmm02.prod.sdp.statoil.no at 2020-02-12 11:37:20 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507440,
      "occurrences": 55703,
      "occurrences_watermark": 55703,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507425,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp02.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:39:69",
              "addresses": [
                "143.97.90.198/24",
                "fe80::250:56ff:fe85:3969/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm02.prod.sdp.statoil.no"
      ],
      "last_seen": 1581428320,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.007858096,
      "executed": 1581507425,
      "history": [
        {
          "status": 0,
          "executed": 1581506225
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506405
        },
        {
          "status": 0,
          "executed": 1581506465
        },
        {
          "status": 0,
          "executed": 1581506525
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506645
        },
        {
          "status": 0,
          "executed": 1581506705
        },
        {
          "status": 0,
          "executed": 1581506765
        },
        {
          "status": 0,
          "executed": 1581506825
        },
        {
          "status": 0,
          "executed": 1581506885
        },
        {
          "status": 0,
          "executed": 1581506945
        },
        {
          "status": 0,
          "executed": 1581507005
        },
        {
          "status": 0,
          "executed": 1581507065
        },
        {
          "status": 0,
          "executed": 1581507125
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507365
        },
        {
          "status": 0,
          "executed": 1581507425
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.02, 0.02, 0.05|load1=0.020;80.000;90.000;0; load5=0.020;80.000;90.000;0; load15=0.050;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507425,
      "occurrences": 18566,
      "occurrences_watermark": 18566,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp02.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:39:69",
              "addresses": [
                "143.97.90.198/24",
                "fe80::250:56ff:fe85:3969/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm02.prod.sdp.statoil.no"
      ],
      "last_seen": 1581428320,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm02.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.17.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.005344559,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 100% free (8191 MB out of 8191 MB) |swap=8191MB;4095;1638;0;8191\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18566,
      "occurrences_watermark": 18566,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp03.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:53:6f",
              "addresses": [
                "143.97.90.199/24",
                "fe80::250:56ff:fe85:536f/64"
              ]
            },
            {
              "name": "br-3eeca5dfae90",
              "mac": "02:42:78:33:17:80",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:78ff:fe33:1780/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:9f:54:03:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-26026f732c26",
              "mac": "02:42:1e:3c:63:e5",
              "addresses": [
                "192.168.64.1/20",
                "fe80::42:1eff:fe3c:63e5/64"
              ]
            },
            {
              "name": "veth317e397",
              "mac": "7e:52:21:a2:39:2d",
              "addresses": [
                "fe80::7c52:21ff:fea2:392d/64"
              ]
            },
            {
              "name": "vethf7a546f",
              "mac": "7e:d9:4e:ae:27:df",
              "addresses": [
                "fe80::7cd9:4eff:feae:27df/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm03.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386325,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm03.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.008667969,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp03.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:53:6f",
              "addresses": [
                "143.97.90.199/24",
                "fe80::250:56ff:fe85:536f/64"
              ]
            },
            {
              "name": "br-3eeca5dfae90",
              "mac": "02:42:78:33:17:80",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:78ff:fe33:1780/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:9f:54:03:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-26026f732c26",
              "mac": "02:42:1e:3c:63:e5",
              "addresses": [
                "192.168.64.1/20",
                "fe80::42:1eff:fe3c:63e5/64"
              ]
            },
            {
              "name": "veth317e397",
              "mac": "7e:52:21:a2:39:2d",
              "addresses": [
                "fe80::7c52:21ff:fea2:392d/64"
              ]
            },
            {
              "name": "vethf7a546f",
              "mac": "7e:d9:4e:ae:27:df",
              "addresses": [
                "fe80::7cd9:4eff:feae:27df/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm03.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386325,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm03.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.005699956,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n/ 22383 MB (80.31% inode=93%);\n/dev 15992 MB (100.00% inode=100%);\n/boot 284 MB (63.52% inode=100%);\n/tmp 7473 MB (99.51% inode=100%);\n/data 326159 MB (68.20% inode=90%);\n/var 19812 MB (85.42% inode=99%);\n| /=5486MB;23507;26445;0;29384 /dev=0MB;12793;14392;0;15992 /boot=163MB;380;428;0;476 /tmp=36MB;6348;7141;0;7935 /data=152056MB;403065;453448;0;503832 /var=3380MB;19425;21853;0;24282\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 17527,
      "occurrences_watermark": 17527,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506657,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp03.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:53:6f",
              "addresses": [
                "143.97.90.199/24",
                "fe80::250:56ff:fe85:536f/64"
              ]
            },
            {
              "name": "br-3eeca5dfae90",
              "mac": "02:42:78:33:17:80",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:78ff:fe33:1780/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:9f:54:03:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-26026f732c26",
              "mac": "02:42:1e:3c:63:e5",
              "addresses": [
                "192.168.64.1/20",
                "fe80::42:1eff:fe3c:63e5/64"
              ]
            },
            {
              "name": "veth317e397",
              "mac": "7e:52:21:a2:39:2d",
              "addresses": [
                "fe80::7c52:21ff:fea2:392d/64"
              ]
            },
            {
              "name": "vethf7a546f",
              "mac": "7e:d9:4e:ae:27:df",
              "addresses": [
                "fe80::7cd9:4eff:feae:27df/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm03.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386325,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm03.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 1.746954749,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (vmm03.prod.sdp.statoil.no) resolves to my IP (143.97.90.199)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507441,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp03.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:53:6f",
              "addresses": [
                "143.97.90.199/24",
                "fe80::250:56ff:fe85:536f/64"
              ]
            },
            {
              "name": "br-3eeca5dfae90",
              "mac": "02:42:78:33:17:80",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:78ff:fe33:1780/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:9f:54:03:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-26026f732c26",
              "mac": "02:42:1e:3c:63:e5",
              "addresses": [
                "192.168.64.1/20",
                "fe80::42:1eff:fe3c:63e5/64"
              ]
            },
            {
              "name": "veth317e397",
              "mac": "7e:52:21:a2:39:2d",
              "addresses": [
                "fe80::7c52:21ff:fea2:392d/64"
              ]
            },
            {
              "name": "vethf7a546f",
              "mac": "7e:d9:4e:ae:27:df",
              "addresses": [
                "fe80::7cd9:4eff:feae:27df/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm03.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507441,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm03.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507441,
      "history": [
        {
          "status": 0,
          "executed": 1581507041
        },
        {
          "status": 0,
          "executed": 1581507061
        },
        {
          "status": 0,
          "executed": 1581507081
        },
        {
          "status": 0,
          "executed": 1581507101
        },
        {
          "status": 0,
          "executed": 1581507121
        },
        {
          "status": 0,
          "executed": 1581507141
        },
        {
          "status": 0,
          "executed": 1581507161
        },
        {
          "status": 0,
          "executed": 1581507181
        },
        {
          "status": 0,
          "executed": 1581507201
        },
        {
          "status": 0,
          "executed": 1581507221
        },
        {
          "status": 0,
          "executed": 1581507241
        },
        {
          "status": 0,
          "executed": 1581507261
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507301
        },
        {
          "status": 0,
          "executed": 1581507321
        },
        {
          "status": 0,
          "executed": 1581507341
        },
        {
          "status": 0,
          "executed": 1581507361
        },
        {
          "status": 0,
          "executed": 1581507381
        },
        {
          "status": 0,
          "executed": 1581507401
        },
        {
          "status": 0,
          "executed": 1581507421
        },
        {
          "status": 0,
          "executed": 1581507441
        }
      ],
      "issued": 1581507441,
      "output": "Keepalive last sent from vmm03.prod.sdp.statoil.no at 2020-02-12 11:37:21 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507441,
      "occurrences": 55709,
      "occurrences_watermark": 55709,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507425,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp03.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:53:6f",
              "addresses": [
                "143.97.90.199/24",
                "fe80::250:56ff:fe85:536f/64"
              ]
            },
            {
              "name": "br-3eeca5dfae90",
              "mac": "02:42:78:33:17:80",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:78ff:fe33:1780/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:9f:54:03:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-26026f732c26",
              "mac": "02:42:1e:3c:63:e5",
              "addresses": [
                "192.168.64.1/20",
                "fe80::42:1eff:fe3c:63e5/64"
              ]
            },
            {
              "name": "veth317e397",
              "mac": "7e:52:21:a2:39:2d",
              "addresses": [
                "fe80::7c52:21ff:fea2:392d/64"
              ]
            },
            {
              "name": "vethf7a546f",
              "mac": "7e:d9:4e:ae:27:df",
              "addresses": [
                "fe80::7cd9:4eff:feae:27df/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm03.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386325,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm03.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.007664742,
      "executed": 1581507425,
      "history": [
        {
          "status": 0,
          "executed": 1581506225
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506405
        },
        {
          "status": 0,
          "executed": 1581506465
        },
        {
          "status": 0,
          "executed": 1581506525
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506645
        },
        {
          "status": 0,
          "executed": 1581506705
        },
        {
          "status": 0,
          "executed": 1581506765
        },
        {
          "status": 0,
          "executed": 1581506825
        },
        {
          "status": 0,
          "executed": 1581506885
        },
        {
          "status": 0,
          "executed": 1581506945
        },
        {
          "status": 0,
          "executed": 1581507005
        },
        {
          "status": 0,
          "executed": 1581507065
        },
        {
          "status": 0,
          "executed": 1581507125
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507365
        },
        {
          "status": 0,
          "executed": 1581507425
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.00, 0.01, 0.05|load1=0.000;80.000;90.000;0; load5=0.010;80.000;90.000;0; load15=0.050;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507425,
      "occurrences": 18568,
      "occurrences_watermark": 18568,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "tr-vsdp03.tr.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "ens192",
              "mac": "00:50:56:85:53:6f",
              "addresses": [
                "143.97.90.199/24",
                "fe80::250:56ff:fe85:536f/64"
              ]
            },
            {
              "name": "br-3eeca5dfae90",
              "mac": "02:42:78:33:17:80",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:78ff:fe33:1780/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:9f:54:03:9f",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-26026f732c26",
              "mac": "02:42:1e:3c:63:e5",
              "addresses": [
                "192.168.64.1/20",
                "fe80::42:1eff:fe3c:63e5/64"
              ]
            },
            {
              "name": "veth317e397",
              "mac": "7e:52:21:a2:39:2d",
              "addresses": [
                "fe80::7c52:21ff:fea2:392d/64"
              ]
            },
            {
              "name": "vethf7a546f",
              "mac": "7e:d9:4e:ae:27:df",
              "addresses": [
                "fe80::7cd9:4eff:feae:27df/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm03.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386325,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm03.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004913741,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 100% free (8190 MB out of 8191 MB) |swap=8190MB;4095;1638;0;8191\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18568,
      "occurrences_watermark": 18568,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1040.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eno16780032",
              "mac": "00:50:56:a2:ed:2e",
              "addresses": [
                "10.217.112.38/22",
                "fe80::250:56ff:fea2:ed2e/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:c5:7f:42:2b",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-87244c9fbaf1",
              "mac": "02:42:42:9b:b6:d8",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:42ff:fe9b:b6d8/64"
              ]
            },
            {
              "name": "br-c54526eb2035",
              "mac": "02:42:54:fe:bf:d5",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:54ff:fefe:bfd5/64"
              ]
            },
            {
              "name": "veth1c999d2",
              "mac": "26:f3:ae:0a:c4:80",
              "addresses": [
                "fe80::24f3:aeff:fe0a:c480/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm04.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296299,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm04.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.008058082,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1040.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eno16780032",
              "mac": "00:50:56:a2:ed:2e",
              "addresses": [
                "10.217.112.38/22",
                "fe80::250:56ff:fea2:ed2e/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:c5:7f:42:2b",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-87244c9fbaf1",
              "mac": "02:42:42:9b:b6:d8",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:42ff:fe9b:b6d8/64"
              ]
            },
            {
              "name": "br-c54526eb2035",
              "mac": "02:42:54:fe:bf:d5",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:54ff:fefe:bfd5/64"
              ]
            },
            {
              "name": "veth1c999d2",
              "mac": "26:f3:ae:0a:c4:80",
              "addresses": [
                "fe80::24f3:aeff:fe0a:c480/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm04.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296299,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm04.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004784633,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n/ 25710 MB (85.78% inode=100%);\n/dev 15992 MB (100.00% inode=100%);\n/boot 281 MB (62.99% inode=100%);\n/tmp 8149 MB (99.60% inode=100%);\n/var 5660 MB (69.17% inode=100%);\n/data 65728 MB (49.76% inode=99%);\n/prog 45104 MB (51.82% inode=98%);\n| /=4259MB;23975;26972;0;29969 /dev=0MB;12793;14392;0;15992 /boot=165MB;380;428;0;476 /tmp=32MB;6545;7363;0;8182 /var=2521MB;6545;7363;0;8182 /data=66357MB;105668;118877;0;132086 /prog=41925MB;69624;78327;0;87030\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18568,
      "occurrences_watermark": 18568,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506656,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1040.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eno16780032",
              "mac": "00:50:56:a2:ed:2e",
              "addresses": [
                "10.217.112.38/22",
                "fe80::250:56ff:fea2:ed2e/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:c5:7f:42:2b",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-87244c9fbaf1",
              "mac": "02:42:42:9b:b6:d8",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:42ff:fe9b:b6d8/64"
              ]
            },
            {
              "name": "br-c54526eb2035",
              "mac": "02:42:54:fe:bf:d5",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:54ff:fefe:bfd5/64"
              ]
            },
            {
              "name": "veth1c999d2",
              "mac": "26:f3:ae:0a:c4:80",
              "addresses": [
                "fe80::24f3:aeff:fe0a:c480/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm04.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296299,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm04.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 1.072031502,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (vmm04.prod.sdp.statoil.no) resolves to my IP (10.217.112.38)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507454,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1040.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eno16780032",
              "mac": "00:50:56:a2:ed:2e",
              "addresses": [
                "10.217.112.38/22",
                "fe80::250:56ff:fea2:ed2e/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:c5:7f:42:2b",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-87244c9fbaf1",
              "mac": "02:42:42:9b:b6:d8",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:42ff:fe9b:b6d8/64"
              ]
            },
            {
              "name": "br-c54526eb2035",
              "mac": "02:42:54:fe:bf:d5",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:54ff:fefe:bfd5/64"
              ]
            },
            {
              "name": "veth1c999d2",
              "mac": "26:f3:ae:0a:c4:80",
              "addresses": [
                "fe80::24f3:aeff:fe0a:c480/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm04.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507454,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm04.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507454,
      "history": [
        {
          "status": 0,
          "executed": 1581507054
        },
        {
          "status": 0,
          "executed": 1581507074
        },
        {
          "status": 0,
          "executed": 1581507094
        },
        {
          "status": 0,
          "executed": 1581507114
        },
        {
          "status": 0,
          "executed": 1581507134
        },
        {
          "status": 0,
          "executed": 1581507155
        },
        {
          "status": 0,
          "executed": 1581507174
        },
        {
          "status": 0,
          "executed": 1581507194
        },
        {
          "status": 0,
          "executed": 1581507214
        },
        {
          "status": 0,
          "executed": 1581507234
        },
        {
          "status": 0,
          "executed": 1581507254
        },
        {
          "status": 0,
          "executed": 1581507274
        },
        {
          "status": 0,
          "executed": 1581507295
        },
        {
          "status": 0,
          "executed": 1581507314
        },
        {
          "status": 0,
          "executed": 1581507334
        },
        {
          "status": 0,
          "executed": 1581507354
        },
        {
          "status": 0,
          "executed": 1581507374
        },
        {
          "status": 0,
          "executed": 1581507394
        },
        {
          "status": 0,
          "executed": 1581507415
        },
        {
          "status": 0,
          "executed": 1581507434
        },
        {
          "status": 0,
          "executed": 1581507454
        }
      ],
      "issued": 1581507454,
      "output": "Keepalive last sent from vmm04.prod.sdp.statoil.no at 2020-02-12 11:37:34 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507454,
      "occurrences": 55711,
      "occurrences_watermark": 55711,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507425,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1040.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eno16780032",
              "mac": "00:50:56:a2:ed:2e",
              "addresses": [
                "10.217.112.38/22",
                "fe80::250:56ff:fea2:ed2e/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:c5:7f:42:2b",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-87244c9fbaf1",
              "mac": "02:42:42:9b:b6:d8",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:42ff:fe9b:b6d8/64"
              ]
            },
            {
              "name": "br-c54526eb2035",
              "mac": "02:42:54:fe:bf:d5",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:54ff:fefe:bfd5/64"
              ]
            },
            {
              "name": "veth1c999d2",
              "mac": "26:f3:ae:0a:c4:80",
              "addresses": [
                "fe80::24f3:aeff:fe0a:c480/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm04.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296299,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm04.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006903719,
      "executed": 1581507425,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506525
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506705
        },
        {
          "status": 0,
          "executed": 1581506765
        },
        {
          "status": 0,
          "executed": 1581506825
        },
        {
          "status": 0,
          "executed": 1581506885
        },
        {
          "status": 0,
          "executed": 1581506945
        },
        {
          "status": 0,
          "executed": 1581507005
        },
        {
          "status": 0,
          "executed": 1581507065
        },
        {
          "status": 0,
          "executed": 1581507125
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507365
        },
        {
          "status": 0,
          "executed": 1581507425
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 0.01, 0.03, 0.05|load1=0.010;80.000;90.000;0; load5=0.030;80.000;90.000;0; load15=0.050;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507425,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "st-linapp1040.st.statoil.no",
        "os": "linux",
        "platform": "redhat",
        "platform_family": "rhel",
        "platform_version": "7.7",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eno16780032",
              "mac": "00:50:56:a2:ed:2e",
              "addresses": [
                "10.217.112.38/22",
                "fe80::250:56ff:fea2:ed2e/64"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:c5:7f:42:2b",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-87244c9fbaf1",
              "mac": "02:42:42:9b:b6:d8",
              "addresses": [
                "172.20.0.1/16",
                "fe80::42:42ff:fe9b:b6d8/64"
              ]
            },
            {
              "name": "br-c54526eb2035",
              "mac": "02:42:54:fe:bf:d5",
              "addresses": [
                "172.19.0.1/16",
                "fe80::42:54ff:fefe:bfd5/64"
              ]
            },
            {
              "name": "veth1c999d2",
              "mac": "26:f3:ae:0a:c4:80",
              "addresses": [
                "fe80::24f3:aeff:fe0a:c480/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "entity:vmm04.prod.sdp.statoil.no"
      ],
      "last_seen": 1580296299,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm04.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004312942,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 100% free (8191 MB out of 8191 MB) |swap=8191MB;4095;1638;0;8191\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507398,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H alertmanager.sdpaks.equinor.com -S -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.315018797,
      "executed": 1581507398,
      "history": [
        {
          "status": 0,
          "executed": 1581506198
        },
        {
          "status": 0,
          "executed": 1581506258
        },
        {
          "status": 0,
          "executed": 1581506318
        },
        {
          "status": 0,
          "executed": 1581506378
        },
        {
          "status": 0,
          "executed": 1581506438
        },
        {
          "status": 0,
          "executed": 1581506498
        },
        {
          "status": 0,
          "executed": 1581506558
        },
        {
          "status": 0,
          "executed": 1581506618
        },
        {
          "status": 0,
          "executed": 1581506678
        },
        {
          "status": 0,
          "executed": 1581506738
        },
        {
          "status": 0,
          "executed": 1581506798
        },
        {
          "status": 0,
          "executed": 1581506858
        },
        {
          "status": 0,
          "executed": 1581506918
        },
        {
          "status": 0,
          "executed": 1581506978
        },
        {
          "status": 0,
          "executed": 1581507038
        },
        {
          "status": 0,
          "executed": 1581507098
        },
        {
          "status": 0,
          "executed": 1581507158
        },
        {
          "status": 0,
          "executed": 1581507218
        },
        {
          "status": 0,
          "executed": 1581507278
        },
        {
          "status": 0,
          "executed": 1581507338
        },
        {
          "status": 0,
          "executed": 1581507398
        }
      ],
      "issued": 1581507398,
      "output": "HTTP OK: HTTP/1.1 302 Moved Temporarily - 438 bytes in 0.310 second response time |time=0.310488s;5.000000;10.000000;0.000000 size=438B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507398,
      "occurrences": 8584,
      "occurrences_watermark": 8584,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "alertmanager.sdpaks.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507446,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.equinor.com -S -u \"/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.212654856,
      "executed": 1581507446,
      "history": [
        {
          "status": 0,
          "executed": 1581506246
        },
        {
          "status": 0,
          "executed": 1581506306
        },
        {
          "status": 0,
          "executed": 1581506366
        },
        {
          "status": 0,
          "executed": 1581506426
        },
        {
          "status": 0,
          "executed": 1581506486
        },
        {
          "status": 0,
          "executed": 1581506546
        },
        {
          "status": 0,
          "executed": 1581506607
        },
        {
          "status": 0,
          "executed": 1581506667
        },
        {
          "status": 0,
          "executed": 1581506726
        },
        {
          "status": 0,
          "executed": 1581506786
        },
        {
          "status": 0,
          "executed": 1581506847
        },
        {
          "status": 0,
          "executed": 1581506906
        },
        {
          "status": 0,
          "executed": 1581506966
        },
        {
          "status": 0,
          "executed": 1581507026
        },
        {
          "status": 0,
          "executed": 1581507086
        },
        {
          "status": 0,
          "executed": 1581507146
        },
        {
          "status": 0,
          "executed": 1581507206
        },
        {
          "status": 0,
          "executed": 1581507266
        },
        {
          "status": 0,
          "executed": 1581507326
        },
        {
          "status": 0,
          "executed": 1581507386
        },
        {
          "status": 0,
          "executed": 1581507446
        }
      ],
      "issued": 1581507446,
      "output": "HTTP OK: HTTP/1.1 301 Moved Permanently - 372 bytes in 0.208 second response time |time=0.207934s;5.000000;10.000000;0.000000 size=372B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507446,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507398,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/check_certificate.sh ci.equinor.com 443 30 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.201454993,
      "executed": 1581507398,
      "history": [
        {
          "status": 0,
          "executed": 1581506198
        },
        {
          "status": 0,
          "executed": 1581506258
        },
        {
          "status": 0,
          "executed": 1581506318
        },
        {
          "status": 0,
          "executed": 1581506378
        },
        {
          "status": 0,
          "executed": 1581506438
        },
        {
          "status": 0,
          "executed": 1581506498
        },
        {
          "status": 0,
          "executed": 1581506558
        },
        {
          "status": 0,
          "executed": 1581506618
        },
        {
          "status": 0,
          "executed": 1581506678
        },
        {
          "status": 0,
          "executed": 1581506738
        },
        {
          "status": 0,
          "executed": 1581506798
        },
        {
          "status": 0,
          "executed": 1581506858
        },
        {
          "status": 0,
          "executed": 1581506918
        },
        {
          "status": 0,
          "executed": 1581506978
        },
        {
          "status": 0,
          "executed": 1581507038
        },
        {
          "status": 0,
          "executed": 1581507098
        },
        {
          "status": 0,
          "executed": 1581507158
        },
        {
          "status": 0,
          "executed": 1581507218
        },
        {
          "status": 0,
          "executed": 1581507278
        },
        {
          "status": 0,
          "executed": 1581507338
        },
        {
          "status": 0,
          "executed": 1581507398
        }
      ],
      "issued": 1581507398,
      "output": "Certificate for ci.equinor.com expires in 101 days, good time ^___^\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507398,
      "occurrences": 1318,
      "occurrences_watermark": 1318,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.equinor.com_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507436,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H ci.statoil.no -S -u \"/login?from=%2Fst%2F\" -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.213082695,
      "executed": 1581507436,
      "history": [
        {
          "status": 0,
          "executed": 1581506236
        },
        {
          "status": 0,
          "executed": 1581506296
        },
        {
          "status": 0,
          "executed": 1581506356
        },
        {
          "status": 0,
          "executed": 1581506416
        },
        {
          "status": 0,
          "executed": 1581506476
        },
        {
          "status": 0,
          "executed": 1581506536
        },
        {
          "status": 0,
          "executed": 1581506596
        },
        {
          "status": 0,
          "executed": 1581506656
        },
        {
          "status": 0,
          "executed": 1581506716
        },
        {
          "status": 0,
          "executed": 1581506776
        },
        {
          "status": 0,
          "executed": 1581506836
        },
        {
          "status": 0,
          "executed": 1581506896
        },
        {
          "status": 0,
          "executed": 1581506956
        },
        {
          "status": 0,
          "executed": 1581507016
        },
        {
          "status": 0,
          "executed": 1581507076
        },
        {
          "status": 0,
          "executed": 1581507136
        },
        {
          "status": 0,
          "executed": 1581507196
        },
        {
          "status": 0,
          "executed": 1581507256
        },
        {
          "status": 0,
          "executed": 1581507316
        },
        {
          "status": 0,
          "executed": 1581507376
        },
        {
          "status": 0,
          "executed": 1581507436
        }
      ],
      "issued": 1581507436,
      "output": "HTTP OK: HTTP/1.1 301 Moved Permanently - 383 bytes in 0.208 second response time |time=0.208355s;5.000000;10.000000;0.000000 size=383B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507436,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "ci.statoil.no",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507422,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H cosmo.equinor.com -S -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.02004078,
      "executed": 1581507422,
      "history": [
        {
          "status": 0,
          "executed": 1581506222
        },
        {
          "status": 0,
          "executed": 1581506282
        },
        {
          "status": 0,
          "executed": 1581506342
        },
        {
          "status": 0,
          "executed": 1581506402
        },
        {
          "status": 0,
          "executed": 1581506462
        },
        {
          "status": 0,
          "executed": 1581506522
        },
        {
          "status": 0,
          "executed": 1581506582
        },
        {
          "status": 0,
          "executed": 1581506642
        },
        {
          "status": 0,
          "executed": 1581506702
        },
        {
          "status": 0,
          "executed": 1581506762
        },
        {
          "status": 0,
          "executed": 1581506822
        },
        {
          "status": 0,
          "executed": 1581506882
        },
        {
          "status": 0,
          "executed": 1581506942
        },
        {
          "status": 0,
          "executed": 1581507002
        },
        {
          "status": 0,
          "executed": 1581507062
        },
        {
          "status": 0,
          "executed": 1581507122
        },
        {
          "status": 0,
          "executed": 1581507182
        },
        {
          "status": 0,
          "executed": 1581507242
        },
        {
          "status": 0,
          "executed": 1581507302
        },
        {
          "status": 0,
          "executed": 1581507362
        },
        {
          "status": 0,
          "executed": 1581507422
        }
      ],
      "issued": 1581507422,
      "output": "HTTP OK: HTTP/1.1 302 Found - 228 bytes in 0.015 second response time |time=0.015142s;5.000000;10.000000;0.000000 size=228B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507422,
      "occurrences": 17418,
      "occurrences_watermark": 17418,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "cosmo.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507432,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/check_certificate.sh cosmo.equinor.com 443 30 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.051474129,
      "executed": 1581507432,
      "history": [
        {
          "status": 0,
          "executed": 1581506232
        },
        {
          "status": 0,
          "executed": 1581506292
        },
        {
          "status": 0,
          "executed": 1581506352
        },
        {
          "status": 0,
          "executed": 1581506412
        },
        {
          "status": 0,
          "executed": 1581506472
        },
        {
          "status": 0,
          "executed": 1581506532
        },
        {
          "status": 0,
          "executed": 1581506592
        },
        {
          "status": 0,
          "executed": 1581506652
        },
        {
          "status": 0,
          "executed": 1581506712
        },
        {
          "status": 0,
          "executed": 1581506772
        },
        {
          "status": 0,
          "executed": 1581506832
        },
        {
          "status": 0,
          "executed": 1581506892
        },
        {
          "status": 0,
          "executed": 1581506952
        },
        {
          "status": 0,
          "executed": 1581507012
        },
        {
          "status": 0,
          "executed": 1581507072
        },
        {
          "status": 0,
          "executed": 1581507132
        },
        {
          "status": 0,
          "executed": 1581507192
        },
        {
          "status": 0,
          "executed": 1581507252
        },
        {
          "status": 0,
          "executed": 1581507312
        },
        {
          "status": 0,
          "executed": 1581507372
        },
        {
          "status": 0,
          "executed": 1581507432
        }
      ],
      "issued": 1581507432,
      "output": "Certificate for cosmo.equinor.com expires in 705 days, good time ^___^\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507432,
      "occurrences": 17418,
      "occurrences_watermark": 17418,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "cosmo.equinor.com_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506410,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/description.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 1800,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.006553337,
      "executed": 1581506410,
      "history": [
        {
          "status": 0,
          "executed": 1581470409
        },
        {
          "status": 0,
          "executed": 1581472209
        },
        {
          "status": 0,
          "executed": 1581474009
        },
        {
          "status": 0,
          "executed": 1581475809
        },
        {
          "status": 0,
          "executed": 1581477609
        },
        {
          "status": 0,
          "executed": 1581479409
        },
        {
          "status": 0,
          "executed": 1581481209
        },
        {
          "status": 0,
          "executed": 1581483009
        },
        {
          "status": 0,
          "executed": 1581484809
        },
        {
          "status": 0,
          "executed": 1581486609
        },
        {
          "status": 0,
          "executed": 1581488409
        },
        {
          "status": 0,
          "executed": 1581490209
        },
        {
          "status": 0,
          "executed": 1581492009
        },
        {
          "status": 0,
          "executed": 1581493809
        },
        {
          "status": 0,
          "executed": 1581495609
        },
        {
          "status": 0,
          "executed": 1581497409
        },
        {
          "status": 0,
          "executed": 1581499209
        },
        {
          "status": 0,
          "executed": 1581501009
        },
        {
          "status": 0,
          "executed": 1581502809
        },
        {
          "status": 0,
          "executed": 1581504609
        },
        {
          "status": 0,
          "executed": 1581506410
        }
      ],
      "issued": 1581506410,
      "output": "Found host description file with valid content\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506410,
      "occurrences": 618,
      "occurrences_watermark": 618,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "description",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507402,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_disk -n -w20% -c 10% -W 20% -K 10% -X nfs -X shm -X tmpfs -X overlay -A -i /data/dockerroot/* -i /run/docker/netns",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.005109388,
      "executed": 1581507402,
      "history": [
        {
          "status": 0,
          "executed": 1581506202
        },
        {
          "status": 0,
          "executed": 1581506262
        },
        {
          "status": 0,
          "executed": 1581506322
        },
        {
          "status": 0,
          "executed": 1581506382
        },
        {
          "status": 0,
          "executed": 1581506442
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506562
        },
        {
          "status": 0,
          "executed": 1581506622
        },
        {
          "status": 0,
          "executed": 1581506682
        },
        {
          "status": 0,
          "executed": 1581506742
        },
        {
          "status": 0,
          "executed": 1581506802
        },
        {
          "status": 0,
          "executed": 1581506862
        },
        {
          "status": 0,
          "executed": 1581506922
        },
        {
          "status": 0,
          "executed": 1581506982
        },
        {
          "status": 0,
          "executed": 1581507042
        },
        {
          "status": 0,
          "executed": 1581507102
        },
        {
          "status": 0,
          "executed": 1581507162
        },
        {
          "status": 0,
          "executed": 1581507222
        },
        {
          "status": 0,
          "executed": 1581507282
        },
        {
          "status": 0,
          "executed": 1581507342
        },
        {
          "status": 0,
          "executed": 1581507402
        }
      ],
      "issued": 1581507402,
      "output": "DISK OK - free space:\n / 45119 MiB (88.14% inode=99%);\n /dev 7916 MiB (100.00% inode=100%);\n /data 143333 MiB (93.26% inode=100%);\n| /=6068MiB;40950;46069;0;51188 /dev=0MiB;6332;7124;0;7916 /data=10342MiB;122940;138308;0;153676\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507402,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "disk",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507418,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H git.equinor.com -S -u /users/sign_in -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.236212708,
      "executed": 1581507418,
      "history": [
        {
          "status": 0,
          "executed": 1581506218
        },
        {
          "status": 0,
          "executed": 1581506278
        },
        {
          "status": 0,
          "executed": 1581506338
        },
        {
          "status": 0,
          "executed": 1581506398
        },
        {
          "status": 0,
          "executed": 1581506458
        },
        {
          "status": 0,
          "executed": 1581506518
        },
        {
          "status": 0,
          "executed": 1581506578
        },
        {
          "status": 0,
          "executed": 1581506638
        },
        {
          "status": 0,
          "executed": 1581506698
        },
        {
          "status": 0,
          "executed": 1581506758
        },
        {
          "status": 0,
          "executed": 1581506818
        },
        {
          "status": 0,
          "executed": 1581506878
        },
        {
          "status": 0,
          "executed": 1581506938
        },
        {
          "status": 0,
          "executed": 1581506998
        },
        {
          "status": 0,
          "executed": 1581507058
        },
        {
          "status": 0,
          "executed": 1581507118
        },
        {
          "status": 0,
          "executed": 1581507178
        },
        {
          "status": 0,
          "executed": 1581507238
        },
        {
          "status": 0,
          "executed": 1581507298
        },
        {
          "status": 0,
          "executed": 1581507358
        },
        {
          "status": 0,
          "executed": 1581507418
        }
      ],
      "issued": 1581507418,
      "output": "HTTP OK: HTTP/1.1 200 OK - 11324 bytes in 0.232 second response time |time=0.231591s;5.000000;10.000000;0.000000 size=11324B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507418,
      "occurrences": 4371,
      "occurrences_watermark": 4371,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "git.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507427,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/check_certificate.sh git.equinor.com 443 30 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.212613777,
      "executed": 1581507427,
      "history": [
        {
          "status": 0,
          "executed": 1581506226
        },
        {
          "status": 0,
          "executed": 1581506286
        },
        {
          "status": 0,
          "executed": 1581506346
        },
        {
          "status": 0,
          "executed": 1581506406
        },
        {
          "status": 0,
          "executed": 1581506467
        },
        {
          "status": 0,
          "executed": 1581506527
        },
        {
          "status": 0,
          "executed": 1581506586
        },
        {
          "status": 0,
          "executed": 1581506647
        },
        {
          "status": 0,
          "executed": 1581506706
        },
        {
          "status": 0,
          "executed": 1581506766
        },
        {
          "status": 0,
          "executed": 1581506826
        },
        {
          "status": 0,
          "executed": 1581506886
        },
        {
          "status": 0,
          "executed": 1581506946
        },
        {
          "status": 0,
          "executed": 1581507006
        },
        {
          "status": 0,
          "executed": 1581507067
        },
        {
          "status": 0,
          "executed": 1581507126
        },
        {
          "status": 0,
          "executed": 1581507187
        },
        {
          "status": 0,
          "executed": 1581507247
        },
        {
          "status": 0,
          "executed": 1581507306
        },
        {
          "status": 0,
          "executed": 1581507366
        },
        {
          "status": 0,
          "executed": 1581507427
        }
      ],
      "issued": 1581507427,
      "output": "Certificate for git.equinor.com expires in 101 days, good time ^___^\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507427,
      "occurrences": 17499,
      "occurrences_watermark": 17499,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "git.equinor.com_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507446,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H git.statoil.no -S -u /users/sign_in -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.245361677,
      "executed": 1581507446,
      "history": [
        {
          "status": 0,
          "executed": 1581506246
        },
        {
          "status": 0,
          "executed": 1581506306
        },
        {
          "status": 0,
          "executed": 1581506366
        },
        {
          "status": 0,
          "executed": 1581506426
        },
        {
          "status": 0,
          "executed": 1581506486
        },
        {
          "status": 0,
          "executed": 1581506546
        },
        {
          "status": 0,
          "executed": 1581506606
        },
        {
          "status": 0,
          "executed": 1581506666
        },
        {
          "status": 0,
          "executed": 1581506726
        },
        {
          "status": 0,
          "executed": 1581506786
        },
        {
          "status": 0,
          "executed": 1581506846
        },
        {
          "status": 0,
          "executed": 1581506906
        },
        {
          "status": 0,
          "executed": 1581506966
        },
        {
          "status": 0,
          "executed": 1581507026
        },
        {
          "status": 0,
          "executed": 1581507086
        },
        {
          "status": 0,
          "executed": 1581507146
        },
        {
          "status": 0,
          "executed": 1581507206
        },
        {
          "status": 0,
          "executed": 1581507266
        },
        {
          "status": 0,
          "executed": 1581507326
        },
        {
          "status": 0,
          "executed": 1581507386
        },
        {
          "status": 0,
          "executed": 1581507446
        }
      ],
      "issued": 1581507446,
      "output": "HTTP OK: HTTP/1.1 200 OK - 11312 bytes in 0.241 second response time |time=0.240656s;5.000000;10.000000;0.000000 size=11312B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507446,
      "occurrences": 4456,
      "occurrences_watermark": 4456,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "git.statoil.no",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507456,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/check_certificate.sh git.statoil.no 443 30 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.204376228,
      "executed": 1581507456,
      "history": [
        {
          "status": 0,
          "executed": 1581506256
        },
        {
          "status": 0,
          "executed": 1581506316
        },
        {
          "status": 0,
          "executed": 1581506376
        },
        {
          "status": 0,
          "executed": 1581506436
        },
        {
          "status": 0,
          "executed": 1581506496
        },
        {
          "status": 0,
          "executed": 1581506556
        },
        {
          "status": 0,
          "executed": 1581506616
        },
        {
          "status": 0,
          "executed": 1581506676
        },
        {
          "status": 0,
          "executed": 1581506736
        },
        {
          "status": 0,
          "executed": 1581506796
        },
        {
          "status": 0,
          "executed": 1581506856
        },
        {
          "status": 0,
          "executed": 1581506916
        },
        {
          "status": 0,
          "executed": 1581506976
        },
        {
          "status": 0,
          "executed": 1581507036
        },
        {
          "status": 0,
          "executed": 1581507096
        },
        {
          "status": 0,
          "executed": 1581507156
        },
        {
          "status": 0,
          "executed": 1581507216
        },
        {
          "status": 0,
          "executed": 1581507276
        },
        {
          "status": 0,
          "executed": 1581507336
        },
        {
          "status": 0,
          "executed": 1581507396
        },
        {
          "status": 0,
          "executed": 1581507456
        }
      ],
      "issued": 1581507456,
      "output": "Certificate for git.statoil.no expires in 101 days, good time ^___^\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507456,
      "occurrences": 18566,
      "occurrences_watermark": 18566,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "git.statoil.no_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507405,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "sudo /opt/sensu/embedded/bin/check-container.rb -N gitstats",
      "handlers": [
        "slack"
      ],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.065844865,
      "executed": 1581507405,
      "history": [
        {
          "status": 1,
          "executed": 1581506205
        },
        {
          "status": 1,
          "executed": 1581506265
        },
        {
          "status": 1,
          "executed": 1581506325
        },
        {
          "status": 1,
          "executed": 1581506385
        },
        {
          "status": 1,
          "executed": 1581506445
        },
        {
          "status": 1,
          "executed": 1581506505
        },
        {
          "status": 1,
          "executed": 1581506565
        },
        {
          "status": 1,
          "executed": 1581506625
        },
        {
          "status": 1,
          "executed": 1581506685
        },
        {
          "status": 1,
          "executed": 1581506745
        },
        {
          "status": 1,
          "executed": 1581506805
        },
        {
          "status": 1,
          "executed": 1581506865
        },
        {
          "status": 1,
          "executed": 1581506925
        },
        {
          "status": 1,
          "executed": 1581506985
        },
        {
          "status": 1,
          "executed": 1581507045
        },
        {
          "status": 1,
          "executed": 1581507105
        },
        {
          "status": 1,
          "executed": 1581507165
        },
        {
          "status": 1,
          "executed": 1581507225
        },
        {
          "status": 1,
          "executed": 1581507285
        },
        {
          "status": 1,
          "executed": 1581507345
        },
        {
          "status": 1,
          "executed": 1581507405
        }
      ],
      "issued": 1581507405,
      "output": "/usr/share/rubygems/rubygems/core_ext/kernel_require.rb:55:in `require': cannot load such file -- sensu-plugin/check/cli (LoadError)\n\tfrom /usr/share/rubygems/rubygems/core_ext/kernel_require.rb:55:in `require'\n\tfrom /opt/sensu/embedded/bin/check-container.rb:38:in `<main>'\n",
      "state": "failing",
      "status": 1,
      "total_state_change": 0,
      "last_ok": 0,
      "occurrences": 18570,
      "occurrences_watermark": 18570,
      "silenced": [
        "entity:vmm05.prod.sdp.statoil.no:gitstats"
      ],
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "gitstats",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507433,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H grafana.sdpaks.equinor.com -S -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.30299687,
      "executed": 1581507433,
      "history": [
        {
          "status": 0,
          "executed": 1581506233
        },
        {
          "status": 0,
          "executed": 1581506293
        },
        {
          "status": 0,
          "executed": 1581506353
        },
        {
          "status": 0,
          "executed": 1581506413
        },
        {
          "status": 0,
          "executed": 1581506473
        },
        {
          "status": 0,
          "executed": 1581506533
        },
        {
          "status": 0,
          "executed": 1581506593
        },
        {
          "status": 0,
          "executed": 1581506653
        },
        {
          "status": 0,
          "executed": 1581506713
        },
        {
          "status": 0,
          "executed": 1581506773
        },
        {
          "status": 0,
          "executed": 1581506833
        },
        {
          "status": 0,
          "executed": 1581506893
        },
        {
          "status": 0,
          "executed": 1581506953
        },
        {
          "status": 0,
          "executed": 1581507013
        },
        {
          "status": 0,
          "executed": 1581507073
        },
        {
          "status": 0,
          "executed": 1581507133
        },
        {
          "status": 0,
          "executed": 1581507193
        },
        {
          "status": 0,
          "executed": 1581507253
        },
        {
          "status": 0,
          "executed": 1581507313
        },
        {
          "status": 0,
          "executed": 1581507373
        },
        {
          "status": 0,
          "executed": 1581507433
        }
      ],
      "issued": 1581507433,
      "output": "HTTP OK: HTTP/1.1 302 Found - 320 bytes in 0.298 second response time |time=0.298220s;5.000000;10.000000;0.000000 size=320B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507433,
      "occurrences": 6874,
      "occurrences_watermark": 6874,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "grafana.sdpaks.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581096259,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/check_certificate.sh grafana.sdpaks.equinor.com 443 30 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.25835288,
      "executed": 1581096258,
      "history": [
        {
          "status": 0,
          "executed": 1581095058
        },
        {
          "status": 0,
          "executed": 1581095118
        },
        {
          "status": 0,
          "executed": 1581095178
        },
        {
          "status": 0,
          "executed": 1581095238
        },
        {
          "status": 0,
          "executed": 1581095298
        },
        {
          "status": 0,
          "executed": 1581095358
        },
        {
          "status": 0,
          "executed": 1581095418
        },
        {
          "status": 0,
          "executed": 1581095478
        },
        {
          "status": 0,
          "executed": 1581095538
        },
        {
          "status": 0,
          "executed": 1581095598
        },
        {
          "status": 0,
          "executed": 1581095658
        },
        {
          "status": 0,
          "executed": 1581095718
        },
        {
          "status": 0,
          "executed": 1581095778
        },
        {
          "status": 0,
          "executed": 1581095838
        },
        {
          "status": 0,
          "executed": 1581095898
        },
        {
          "status": 0,
          "executed": 1581095958
        },
        {
          "status": 0,
          "executed": 1581096018
        },
        {
          "status": 0,
          "executed": 1581096078
        },
        {
          "status": 0,
          "executed": 1581096138
        },
        {
          "status": 0,
          "executed": 1581096198
        },
        {
          "status": 0,
          "executed": 1581096258
        }
      ],
      "issued": 1581096258,
      "output": "Certificate for grafana.sdpaks.equinor.com expires in 51 days, good time ^___^\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581096258,
      "occurrences": 3155,
      "occurrences_watermark": 3155,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "grafana.sdpaks.equinor.com_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581506655,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/hostname.sh",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 3600,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.348616564,
      "executed": 1581506655,
      "history": [
        {
          "status": 0,
          "executed": 1581434655
        },
        {
          "status": 0,
          "executed": 1581438255
        },
        {
          "status": 0,
          "executed": 1581441855
        },
        {
          "status": 0,
          "executed": 1581445455
        },
        {
          "status": 0,
          "executed": 1581449055
        },
        {
          "status": 0,
          "executed": 1581452655
        },
        {
          "status": 0,
          "executed": 1581456255
        },
        {
          "status": 0,
          "executed": 1581459855
        },
        {
          "status": 0,
          "executed": 1581463455
        },
        {
          "status": 0,
          "executed": 1581467055
        },
        {
          "status": 0,
          "executed": 1581470655
        },
        {
          "status": 0,
          "executed": 1581474255
        },
        {
          "status": 0,
          "executed": 1581477855
        },
        {
          "status": 0,
          "executed": 1581481455
        },
        {
          "status": 0,
          "executed": 1581485055
        },
        {
          "status": 0,
          "executed": 1581488655
        },
        {
          "status": 0,
          "executed": 1581492255
        },
        {
          "status": 0,
          "executed": 1581495855
        },
        {
          "status": 0,
          "executed": 1581499455
        },
        {
          "status": 0,
          "executed": 1581503055
        },
        {
          "status": 0,
          "executed": 1581506655
        }
      ],
      "issued": 1581506655,
      "output": "My certname (vmm05.prod.sdp.statoil.no) resolves to my IP (10.36.1.220)\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581506655,
      "occurrences": 309,
      "occurrences_watermark": 309,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "hostname",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507451,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H inventory.sdp.equinor.com -S -u / -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.721213787,
      "executed": 1581507450,
      "history": [
        {
          "status": 0,
          "executed": 1581506250
        },
        {
          "status": 0,
          "executed": 1581506310
        },
        {
          "status": 0,
          "executed": 1581506370
        },
        {
          "status": 0,
          "executed": 1581506430
        },
        {
          "status": 0,
          "executed": 1581506490
        },
        {
          "status": 0,
          "executed": 1581506550
        },
        {
          "status": 0,
          "executed": 1581506610
        },
        {
          "status": 0,
          "executed": 1581506670
        },
        {
          "status": 0,
          "executed": 1581506730
        },
        {
          "status": 0,
          "executed": 1581506790
        },
        {
          "status": 0,
          "executed": 1581506850
        },
        {
          "status": 0,
          "executed": 1581506910
        },
        {
          "status": 0,
          "executed": 1581506970
        },
        {
          "status": 0,
          "executed": 1581507030
        },
        {
          "status": 0,
          "executed": 1581507090
        },
        {
          "status": 0,
          "executed": 1581507150
        },
        {
          "status": 0,
          "executed": 1581507210
        },
        {
          "status": 0,
          "executed": 1581507270
        },
        {
          "status": 0,
          "executed": 1581507330
        },
        {
          "status": 0,
          "executed": 1581507390
        },
        {
          "status": 0,
          "executed": 1581507450
        }
      ],
      "issued": 1581507450,
      "output": "HTTP OK: HTTP/1.1 200 OK - 45446 bytes in 0.716 second response time |time=0.716464s;5.000000;10.000000;0.000000 size=45446B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507450,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "inventory.sdp.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507413,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/check_certificate.sh inventory.sdp.equinor.com 443 30 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.199162361,
      "executed": 1581507413,
      "history": [
        {
          "status": 0,
          "executed": 1581506213
        },
        {
          "status": 0,
          "executed": 1581506273
        },
        {
          "status": 0,
          "executed": 1581506333
        },
        {
          "status": 0,
          "executed": 1581506393
        },
        {
          "status": 0,
          "executed": 1581506453
        },
        {
          "status": 0,
          "executed": 1581506513
        },
        {
          "status": 0,
          "executed": 1581506573
        },
        {
          "status": 0,
          "executed": 1581506633
        },
        {
          "status": 0,
          "executed": 1581506693
        },
        {
          "status": 0,
          "executed": 1581506753
        },
        {
          "status": 0,
          "executed": 1581506813
        },
        {
          "status": 0,
          "executed": 1581506873
        },
        {
          "status": 0,
          "executed": 1581506933
        },
        {
          "status": 0,
          "executed": 1581506993
        },
        {
          "status": 0,
          "executed": 1581507053
        },
        {
          "status": 0,
          "executed": 1581507113
        },
        {
          "status": 0,
          "executed": 1581507173
        },
        {
          "status": 0,
          "executed": 1581507234
        },
        {
          "status": 0,
          "executed": 1581507293
        },
        {
          "status": 0,
          "executed": 1581507353
        },
        {
          "status": 0,
          "executed": 1581507413
        }
      ],
      "issued": 1581507413,
      "output": "Certificate for inventory.sdp.equinor.com expires in 101 days, good time ^___^\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507413,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "inventory.sdp.equinor.com_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507437,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H jetbrainsls.equinor.com -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.074390378,
      "executed": 1581507437,
      "history": [
        {
          "status": 0,
          "executed": 1581506237
        },
        {
          "status": 0,
          "executed": 1581506297
        },
        {
          "status": 0,
          "executed": 1581506357
        },
        {
          "status": 0,
          "executed": 1581506417
        },
        {
          "status": 0,
          "executed": 1581506477
        },
        {
          "status": 0,
          "executed": 1581506537
        },
        {
          "status": 0,
          "executed": 1581506597
        },
        {
          "status": 0,
          "executed": 1581506657
        },
        {
          "status": 0,
          "executed": 1581506717
        },
        {
          "status": 0,
          "executed": 1581506778
        },
        {
          "status": 0,
          "executed": 1581506837
        },
        {
          "status": 0,
          "executed": 1581506897
        },
        {
          "status": 0,
          "executed": 1581506957
        },
        {
          "status": 0,
          "executed": 1581507017
        },
        {
          "status": 0,
          "executed": 1581507077
        },
        {
          "status": 0,
          "executed": 1581507137
        },
        {
          "status": 0,
          "executed": 1581507197
        },
        {
          "status": 0,
          "executed": 1581507257
        },
        {
          "status": 0,
          "executed": 1581507317
        },
        {
          "status": 0,
          "executed": 1581507377
        },
        {
          "status": 0,
          "executed": 1581507437
        }
      ],
      "issued": 1581507437,
      "output": "HTTP OK: HTTP/1.1 302 Found - 338 bytes in 0.070 second response time |time=0.069558s;5.000000;10.000000;0.000000 size=338B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507437,
      "occurrences": 17292,
      "occurrences_watermark": 17292,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "jetbrainsls.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507450,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1581507450,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "handlers": [
        "keepalive"
      ],
      "high_flap_threshold": 0,
      "interval": 20,
      "low_flap_threshold": 0,
      "publish": false,
      "runtime_assets": null,
      "subscriptions": [],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 120,
      "round_robin": false,
      "executed": 1581507450,
      "history": [
        {
          "status": 0,
          "executed": 1581507050
        },
        {
          "status": 0,
          "executed": 1581507070
        },
        {
          "status": 0,
          "executed": 1581507092
        },
        {
          "status": 0,
          "executed": 1581507110
        },
        {
          "status": 0,
          "executed": 1581507130
        },
        {
          "status": 0,
          "executed": 1581507150
        },
        {
          "status": 0,
          "executed": 1581507170
        },
        {
          "status": 0,
          "executed": 1581507190
        },
        {
          "status": 0,
          "executed": 1581507210
        },
        {
          "status": 0,
          "executed": 1581507230
        },
        {
          "status": 0,
          "executed": 1581507250
        },
        {
          "status": 0,
          "executed": 1581507270
        },
        {
          "status": 0,
          "executed": 1581507290
        },
        {
          "status": 0,
          "executed": 1581507310
        },
        {
          "status": 0,
          "executed": 1581507330
        },
        {
          "status": 0,
          "executed": 1581507350
        },
        {
          "status": 0,
          "executed": 1581507370
        },
        {
          "status": 0,
          "executed": 1581507391
        },
        {
          "status": 0,
          "executed": 1581507410
        },
        {
          "status": 0,
          "executed": 1581507430
        },
        {
          "status": 0,
          "executed": 1581507450
        }
      ],
      "issued": 1581507450,
      "output": "Keepalive last sent from vmm05.prod.sdp.statoil.no at 2020-02-12 11:37:30 +0000 UTC",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507450,
      "occurrences": 55710,
      "occurrences_watermark": 55710,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "keepalive",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507424,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_load -w 80% -c 90%",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.007161618,
      "executed": 1581507424,
      "history": [
        {
          "status": 0,
          "executed": 1581506224
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506345
        },
        {
          "status": 0,
          "executed": 1581506404
        },
        {
          "status": 0,
          "executed": 1581506464
        },
        {
          "status": 0,
          "executed": 1581506524
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506644
        },
        {
          "status": 0,
          "executed": 1581506704
        },
        {
          "status": 0,
          "executed": 1581506764
        },
        {
          "status": 0,
          "executed": 1581506824
        },
        {
          "status": 0,
          "executed": 1581506884
        },
        {
          "status": 0,
          "executed": 1581506944
        },
        {
          "status": 0,
          "executed": 1581507004
        },
        {
          "status": 0,
          "executed": 1581507064
        },
        {
          "status": 0,
          "executed": 1581507124
        },
        {
          "status": 0,
          "executed": 1581507184
        },
        {
          "status": 0,
          "executed": 1581507244
        },
        {
          "status": 0,
          "executed": 1581507304
        },
        {
          "status": 0,
          "executed": 1581507364
        },
        {
          "status": 0,
          "executed": 1581507424
        }
      ],
      "issued": 1581507424,
      "output": "OK - load average: 1.00, 0.90, 0.80|load1=1.000;80.000;90.000;0; load5=0.900;80.000;90.000;0; load15=0.800;80.000;90.000;0; \n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507424,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "load",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507432,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H npm.equinor.com -S -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.365914405,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507012
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "HTTP OK: HTTP/1.1 200 OK - 1927 bytes in 0.361 second response time |time=0.361140s;5.000000;10.000000;0.000000 size=1927B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 3302,
      "occurrences_watermark": 3302,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "npm.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581096173,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/check_certificate.sh npm.equinor.com 443 30 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.505343646,
      "executed": 1581096173,
      "history": [
        {
          "status": 0,
          "executed": 1581094853
        },
        {
          "status": 0,
          "executed": 1581094913
        },
        {
          "status": 2,
          "executed": 1581094973
        },
        {
          "status": 0,
          "executed": 1581095153
        },
        {
          "status": 0,
          "executed": 1581095213
        },
        {
          "status": 0,
          "executed": 1581095273
        },
        {
          "status": 0,
          "executed": 1581095333
        },
        {
          "status": 0,
          "executed": 1581095393
        },
        {
          "status": 0,
          "executed": 1581095453
        },
        {
          "status": 0,
          "executed": 1581095513
        },
        {
          "status": 0,
          "executed": 1581095573
        },
        {
          "status": 0,
          "executed": 1581095633
        },
        {
          "status": 0,
          "executed": 1581095693
        },
        {
          "status": 0,
          "executed": 1581095753
        },
        {
          "status": 0,
          "executed": 1581095813
        },
        {
          "status": 0,
          "executed": 1581095873
        },
        {
          "status": 0,
          "executed": 1581095933
        },
        {
          "status": 0,
          "executed": 1581095993
        },
        {
          "status": 0,
          "executed": 1581096053
        },
        {
          "status": 0,
          "executed": 1581096113
        },
        {
          "status": 0,
          "executed": 1581096173
        }
      ],
      "issued": 1581096173,
      "output": "Certificate for npm.equinor.com expires in 347 days, good time ^___^\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 8,
      "last_ok": 1581096173,
      "occurrences": 18,
      "occurrences_watermark": 18,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "npm.equinor.com_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507427,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H prometheus.sdpaks.equinor.com -S -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.308880516,
      "executed": 1581507427,
      "history": [
        {
          "status": 0,
          "executed": 1581506226
        },
        {
          "status": 0,
          "executed": 1581506286
        },
        {
          "status": 0,
          "executed": 1581506346
        },
        {
          "status": 0,
          "executed": 1581506406
        },
        {
          "status": 0,
          "executed": 1581506466
        },
        {
          "status": 0,
          "executed": 1581506526
        },
        {
          "status": 0,
          "executed": 1581506586
        },
        {
          "status": 0,
          "executed": 1581506647
        },
        {
          "status": 0,
          "executed": 1581506706
        },
        {
          "status": 0,
          "executed": 1581506766
        },
        {
          "status": 0,
          "executed": 1581506826
        },
        {
          "status": 0,
          "executed": 1581506886
        },
        {
          "status": 0,
          "executed": 1581506946
        },
        {
          "status": 0,
          "executed": 1581507006
        },
        {
          "status": 0,
          "executed": 1581507066
        },
        {
          "status": 0,
          "executed": 1581507126
        },
        {
          "status": 0,
          "executed": 1581507186
        },
        {
          "status": 0,
          "executed": 1581507246
        },
        {
          "status": 0,
          "executed": 1581507306
        },
        {
          "status": 0,
          "executed": 1581507366
        },
        {
          "status": 0,
          "executed": 1581507427
        }
      ],
      "issued": 1581507427,
      "output": "HTTP OK: HTTP/1.1 302 Moved Temporarily - 436 bytes in 0.304 second response time |time=0.304103s;5.000000;10.000000;0.000000 size=436B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507427,
      "occurrences": 7222,
      "occurrences_watermark": 7222,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "prometheus.sdpaks.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507412,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H scrubberweb.equinor.com -S -w 5 -c 10 -e 401",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.212267009,
      "executed": 1581507412,
      "history": [
        {
          "status": 0,
          "executed": 1581506212
        },
        {
          "status": 0,
          "executed": 1581506272
        },
        {
          "status": 0,
          "executed": 1581506332
        },
        {
          "status": 0,
          "executed": 1581506392
        },
        {
          "status": 0,
          "executed": 1581506453
        },
        {
          "status": 0,
          "executed": 1581506512
        },
        {
          "status": 0,
          "executed": 1581506572
        },
        {
          "status": 0,
          "executed": 1581506632
        },
        {
          "status": 0,
          "executed": 1581506692
        },
        {
          "status": 0,
          "executed": 1581506752
        },
        {
          "status": 0,
          "executed": 1581506812
        },
        {
          "status": 0,
          "executed": 1581506872
        },
        {
          "status": 0,
          "executed": 1581506932
        },
        {
          "status": 0,
          "executed": 1581506992
        },
        {
          "status": 0,
          "executed": 1581507052
        },
        {
          "status": 0,
          "executed": 1581507112
        },
        {
          "status": 0,
          "executed": 1581507172
        },
        {
          "status": 0,
          "executed": 1581507232
        },
        {
          "status": 0,
          "executed": 1581507292
        },
        {
          "status": 0,
          "executed": 1581507352
        },
        {
          "status": 0,
          "executed": 1581507412
        }
      ],
      "issued": 1581507412,
      "output": "HTTP OK: Status line output matched \"401\" - 391 bytes in 0.207 second response time |time=0.207488s;5.000000;10.000000;0.000000 size=391B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507412,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "scrubberweb.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507398,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/check_certificate.sh scrubberweb.equinor.com 443 30 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.201281199,
      "executed": 1581507398,
      "history": [
        {
          "status": 0,
          "executed": 1581506198
        },
        {
          "status": 0,
          "executed": 1581506258
        },
        {
          "status": 0,
          "executed": 1581506318
        },
        {
          "status": 0,
          "executed": 1581506378
        },
        {
          "status": 0,
          "executed": 1581506438
        },
        {
          "status": 0,
          "executed": 1581506498
        },
        {
          "status": 0,
          "executed": 1581506558
        },
        {
          "status": 0,
          "executed": 1581506618
        },
        {
          "status": 0,
          "executed": 1581506678
        },
        {
          "status": 0,
          "executed": 1581506738
        },
        {
          "status": 0,
          "executed": 1581506798
        },
        {
          "status": 0,
          "executed": 1581506858
        },
        {
          "status": 0,
          "executed": 1581506918
        },
        {
          "status": 0,
          "executed": 1581506978
        },
        {
          "status": 0,
          "executed": 1581507038
        },
        {
          "status": 0,
          "executed": 1581507098
        },
        {
          "status": 0,
          "executed": 1581507158
        },
        {
          "status": 0,
          "executed": 1581507218
        },
        {
          "status": 0,
          "executed": 1581507278
        },
        {
          "status": 0,
          "executed": 1581507338
        },
        {
          "status": 0,
          "executed": 1581507398
        }
      ],
      "issued": 1581507398,
      "output": "Certificate for scrubberweb.equinor.com expires in 101 days, good time ^___^\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507398,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "scrubberweb.equinor.com_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507438,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H scrubberweb.statoil.no -S -w 5 -c 10 -e 401",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.211220841,
      "executed": 1581507437,
      "history": [
        {
          "status": 0,
          "executed": 1581506237
        },
        {
          "status": 0,
          "executed": 1581506297
        },
        {
          "status": 0,
          "executed": 1581506357
        },
        {
          "status": 0,
          "executed": 1581506417
        },
        {
          "status": 0,
          "executed": 1581506477
        },
        {
          "status": 0,
          "executed": 1581506537
        },
        {
          "status": 0,
          "executed": 1581506597
        },
        {
          "status": 0,
          "executed": 1581506657
        },
        {
          "status": 0,
          "executed": 1581506717
        },
        {
          "status": 0,
          "executed": 1581506778
        },
        {
          "status": 0,
          "executed": 1581506837
        },
        {
          "status": 0,
          "executed": 1581506897
        },
        {
          "status": 0,
          "executed": 1581506957
        },
        {
          "status": 0,
          "executed": 1581507018
        },
        {
          "status": 0,
          "executed": 1581507077
        },
        {
          "status": 0,
          "executed": 1581507137
        },
        {
          "status": 0,
          "executed": 1581507197
        },
        {
          "status": 0,
          "executed": 1581507257
        },
        {
          "status": 0,
          "executed": 1581507317
        },
        {
          "status": 0,
          "executed": 1581507377
        },
        {
          "status": 0,
          "executed": 1581507437
        }
      ],
      "issued": 1581507437,
      "output": "HTTP OK: Status line output matched \"401\" - 391 bytes in 0.206 second response time |time=0.206438s;5.000000;10.000000;0.000000 size=391B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507437,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "scrubberweb.statoil.no",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507432,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H sdp.equinor.com -S -u / -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.393460174,
      "executed": 1581507432,
      "history": [
        {
          "status": 0,
          "executed": 1581506232
        },
        {
          "status": 0,
          "executed": 1581506292
        },
        {
          "status": 0,
          "executed": 1581506352
        },
        {
          "status": 0,
          "executed": 1581506412
        },
        {
          "status": 0,
          "executed": 1581506472
        },
        {
          "status": 0,
          "executed": 1581506532
        },
        {
          "status": 0,
          "executed": 1581506592
        },
        {
          "status": 0,
          "executed": 1581506652
        },
        {
          "status": 0,
          "executed": 1581506712
        },
        {
          "status": 0,
          "executed": 1581506772
        },
        {
          "status": 0,
          "executed": 1581506832
        },
        {
          "status": 0,
          "executed": 1581506892
        },
        {
          "status": 0,
          "executed": 1581506952
        },
        {
          "status": 0,
          "executed": 1581507012
        },
        {
          "status": 0,
          "executed": 1581507072
        },
        {
          "status": 0,
          "executed": 1581507132
        },
        {
          "status": 0,
          "executed": 1581507192
        },
        {
          "status": 0,
          "executed": 1581507252
        },
        {
          "status": 0,
          "executed": 1581507312
        },
        {
          "status": 0,
          "executed": 1581507372
        },
        {
          "status": 0,
          "executed": 1581507432
        }
      ],
      "issued": 1581507432,
      "output": "HTTP OK: HTTP/1.1 200 OK - 8893 bytes in 0.389 second response time |time=0.388739s;5.000000;10.000000;0.000000 size=8893B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507432,
      "occurrences": 218,
      "occurrences_watermark": 218,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "sdp.equinor.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507417,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H sdp.equinor.com -S -u /artifactory/ -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.251224516,
      "executed": 1581507417,
      "history": [
        {
          "status": 0,
          "executed": 1581506217
        },
        {
          "status": 0,
          "executed": 1581506277
        },
        {
          "status": 0,
          "executed": 1581506337
        },
        {
          "status": 0,
          "executed": 1581506397
        },
        {
          "status": 0,
          "executed": 1581506457
        },
        {
          "status": 0,
          "executed": 1581506517
        },
        {
          "status": 0,
          "executed": 1581506577
        },
        {
          "status": 0,
          "executed": 1581506637
        },
        {
          "status": 0,
          "executed": 1581506697
        },
        {
          "status": 0,
          "executed": 1581506757
        },
        {
          "status": 0,
          "executed": 1581506817
        },
        {
          "status": 0,
          "executed": 1581506877
        },
        {
          "status": 0,
          "executed": 1581506937
        },
        {
          "status": 0,
          "executed": 1581506997
        },
        {
          "status": 0,
          "executed": 1581507057
        },
        {
          "status": 0,
          "executed": 1581507117
        },
        {
          "status": 0,
          "executed": 1581507177
        },
        {
          "status": 0,
          "executed": 1581507237
        },
        {
          "status": 0,
          "executed": 1581507297
        },
        {
          "status": 0,
          "executed": 1581507357
        },
        {
          "status": 0,
          "executed": 1581507417
        }
      ],
      "issued": 1581507417,
      "output": "HTTP OK: HTTP/1.1 302 Found - 229 bytes in 0.246 second response time |time=0.246498s;5.000000;10.000000;0.000000 size=229B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507417,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "sdp.equinor.com_artifactory",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507407,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/check_certificate.sh sdp.equinor.com 443 30 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.201586115,
      "executed": 1581507406,
      "history": [
        {
          "status": 0,
          "executed": 1581506206
        },
        {
          "status": 0,
          "executed": 1581506266
        },
        {
          "status": 0,
          "executed": 1581506326
        },
        {
          "status": 0,
          "executed": 1581506386
        },
        {
          "status": 0,
          "executed": 1581506446
        },
        {
          "status": 0,
          "executed": 1581506506
        },
        {
          "status": 0,
          "executed": 1581506566
        },
        {
          "status": 0,
          "executed": 1581506626
        },
        {
          "status": 0,
          "executed": 1581506686
        },
        {
          "status": 0,
          "executed": 1581506746
        },
        {
          "status": 0,
          "executed": 1581506806
        },
        {
          "status": 0,
          "executed": 1581506866
        },
        {
          "status": 0,
          "executed": 1581506926
        },
        {
          "status": 0,
          "executed": 1581506986
        },
        {
          "status": 0,
          "executed": 1581507046
        },
        {
          "status": 0,
          "executed": 1581507106
        },
        {
          "status": 0,
          "executed": 1581507166
        },
        {
          "status": 0,
          "executed": 1581507226
        },
        {
          "status": 0,
          "executed": 1581507286
        },
        {
          "status": 0,
          "executed": 1581507346
        },
        {
          "status": 0,
          "executed": 1581507406
        }
      ],
      "issued": 1581507406,
      "output": "Certificate for sdp.equinor.com expires in 101 days, good time ^___^\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507406,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "sdp.equinor.com_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507439,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H sdp.equinor.com -S -u /trac/ -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.213898169,
      "executed": 1581507439,
      "history": [
        {
          "status": 0,
          "executed": 1581506239
        },
        {
          "status": 0,
          "executed": 1581506299
        },
        {
          "status": 0,
          "executed": 1581506359
        },
        {
          "status": 0,
          "executed": 1581506419
        },
        {
          "status": 0,
          "executed": 1581506479
        },
        {
          "status": 0,
          "executed": 1581506539
        },
        {
          "status": 0,
          "executed": 1581506599
        },
        {
          "status": 0,
          "executed": 1581506659
        },
        {
          "status": 0,
          "executed": 1581506719
        },
        {
          "status": 0,
          "executed": 1581506779
        },
        {
          "status": 0,
          "executed": 1581506839
        },
        {
          "status": 0,
          "executed": 1581506899
        },
        {
          "status": 0,
          "executed": 1581506959
        },
        {
          "status": 0,
          "executed": 1581507019
        },
        {
          "status": 0,
          "executed": 1581507079
        },
        {
          "status": 0,
          "executed": 1581507139
        },
        {
          "status": 0,
          "executed": 1581507199
        },
        {
          "status": 0,
          "executed": 1581507259
        },
        {
          "status": 0,
          "executed": 1581507319
        },
        {
          "status": 0,
          "executed": 1581507379
        },
        {
          "status": 0,
          "executed": 1581507439
        }
      ],
      "issued": 1581507439,
      "output": "HTTP OK: HTTP/1.1 200 OK - 859 bytes in 0.209 second response time |time=0.209197s;5.000000;10.000000;0.000000 size=859B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507439,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "sdp.equinor.com_trac",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507419,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H sdp.equinor.com -S -u /wikidocs/ -w 10 -c 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.215621618,
      "executed": 1581507419,
      "history": [
        {
          "status": 2,
          "executed": 1581506219
        },
        {
          "status": 2,
          "executed": 1581506279
        },
        {
          "status": 2,
          "executed": 1581506339
        },
        {
          "status": 2,
          "executed": 1581506399
        },
        {
          "status": 2,
          "executed": 1581506459
        },
        {
          "status": 2,
          "executed": 1581506519
        },
        {
          "status": 2,
          "executed": 1581506579
        },
        {
          "status": 2,
          "executed": 1581506639
        },
        {
          "status": 2,
          "executed": 1581506699
        },
        {
          "status": 2,
          "executed": 1581506759
        },
        {
          "status": 2,
          "executed": 1581506819
        },
        {
          "status": 2,
          "executed": 1581506879
        },
        {
          "status": 2,
          "executed": 1581506939
        },
        {
          "status": 2,
          "executed": 1581506999
        },
        {
          "status": 2,
          "executed": 1581507059
        },
        {
          "status": 2,
          "executed": 1581507119
        },
        {
          "status": 2,
          "executed": 1581507179
        },
        {
          "status": 2,
          "executed": 1581507239
        },
        {
          "status": 2,
          "executed": 1581507299
        },
        {
          "status": 2,
          "executed": 1581507359
        },
        {
          "status": 2,
          "executed": 1581507419
        }
      ],
      "issued": 1581507419,
      "output": "HTTP CRITICAL: HTTP/1.1 502 Bad Gateway - 311 bytes in 0.211 second response time |time=0.210987s;10.000000;15.000000;0.000000 size=311B;;;0\n",
      "state": "failing",
      "status": 2,
      "total_state_change": 0,
      "last_ok": 0,
      "occurrences": 1343,
      "occurrences_watermark": 1343,
      "silenced": [
        "entity:vmm05.prod.sdp.statoil.no:sdp.equinor.com_wikidocs"
      ],
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "sdp.equinor.com_wikidocs",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507409,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H sdp.statoil.no -S -u /artifactory/ -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.252456544,
      "executed": 1581507408,
      "history": [
        {
          "status": 0,
          "executed": 1581506208
        },
        {
          "status": 0,
          "executed": 1581506268
        },
        {
          "status": 0,
          "executed": 1581506328
        },
        {
          "status": 0,
          "executed": 1581506388
        },
        {
          "status": 0,
          "executed": 1581506448
        },
        {
          "status": 0,
          "executed": 1581506508
        },
        {
          "status": 0,
          "executed": 1581506568
        },
        {
          "status": 0,
          "executed": 1581506628
        },
        {
          "status": 0,
          "executed": 1581506688
        },
        {
          "status": 0,
          "executed": 1581506748
        },
        {
          "status": 0,
          "executed": 1581506808
        },
        {
          "status": 0,
          "executed": 1581506868
        },
        {
          "status": 0,
          "executed": 1581506928
        },
        {
          "status": 0,
          "executed": 1581506988
        },
        {
          "status": 0,
          "executed": 1581507048
        },
        {
          "status": 0,
          "executed": 1581507108
        },
        {
          "status": 0,
          "executed": 1581507168
        },
        {
          "status": 0,
          "executed": 1581507228
        },
        {
          "status": 0,
          "executed": 1581507288
        },
        {
          "status": 0,
          "executed": 1581507348
        },
        {
          "status": 0,
          "executed": 1581507408
        }
      ],
      "issued": 1581507408,
      "output": "HTTP OK: HTTP/1.1 302 Found - 228 bytes in 0.248 second response time |time=0.247748s;5.000000;10.000000;0.000000 size=228B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507408,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "sdp.statoil.no_artifactory",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507425,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H sdp.statoil.no -S -u /trac/ -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.212865214,
      "executed": 1581507425,
      "history": [
        {
          "status": 0,
          "executed": 1581506225
        },
        {
          "status": 0,
          "executed": 1581506285
        },
        {
          "status": 0,
          "executed": 1581506346
        },
        {
          "status": 0,
          "executed": 1581506405
        },
        {
          "status": 0,
          "executed": 1581506465
        },
        {
          "status": 0,
          "executed": 1581506525
        },
        {
          "status": 0,
          "executed": 1581506585
        },
        {
          "status": 0,
          "executed": 1581506645
        },
        {
          "status": 0,
          "executed": 1581506705
        },
        {
          "status": 0,
          "executed": 1581506765
        },
        {
          "status": 0,
          "executed": 1581506825
        },
        {
          "status": 0,
          "executed": 1581506886
        },
        {
          "status": 0,
          "executed": 1581506945
        },
        {
          "status": 0,
          "executed": 1581507005
        },
        {
          "status": 0,
          "executed": 1581507065
        },
        {
          "status": 0,
          "executed": 1581507125
        },
        {
          "status": 0,
          "executed": 1581507185
        },
        {
          "status": 0,
          "executed": 1581507245
        },
        {
          "status": 0,
          "executed": 1581507305
        },
        {
          "status": 0,
          "executed": 1581507365
        },
        {
          "status": 0,
          "executed": 1581507425
        }
      ],
      "issued": 1581507425,
      "output": "HTTP OK: HTTP/1.1 301 Moved Permanently - 370 bytes in 0.208 second response time |time=0.208107s;5.000000;10.000000;0.000000 size=370B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507425,
      "occurrences": 1319,
      "occurrences_watermark": 1319,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "sdp.statoil.no_trac",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507412,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H sdp.statoil.no -S -u /wikidocs/ -w 10 -c 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.212484127,
      "executed": 1581507412,
      "history": [
        {
          "status": 0,
          "executed": 1581506212
        },
        {
          "status": 0,
          "executed": 1581506272
        },
        {
          "status": 0,
          "executed": 1581506332
        },
        {
          "status": 0,
          "executed": 1581506392
        },
        {
          "status": 0,
          "executed": 1581506453
        },
        {
          "status": 0,
          "executed": 1581506512
        },
        {
          "status": 0,
          "executed": 1581506572
        },
        {
          "status": 0,
          "executed": 1581506632
        },
        {
          "status": 0,
          "executed": 1581506692
        },
        {
          "status": 0,
          "executed": 1581506752
        },
        {
          "status": 0,
          "executed": 1581506812
        },
        {
          "status": 0,
          "executed": 1581506872
        },
        {
          "status": 0,
          "executed": 1581506932
        },
        {
          "status": 0,
          "executed": 1581506992
        },
        {
          "status": 0,
          "executed": 1581507053
        },
        {
          "status": 0,
          "executed": 1581507112
        },
        {
          "status": 0,
          "executed": 1581507172
        },
        {
          "status": 0,
          "executed": 1581507232
        },
        {
          "status": 0,
          "executed": 1581507292
        },
        {
          "status": 0,
          "executed": 1581507352
        },
        {
          "status": 0,
          "executed": 1581507412
        }
      ],
      "issued": 1581507412,
      "output": "HTTP OK: HTTP/1.1 301 Moved Permanently - 374 bytes in 0.208 second response time |time=0.207781s;10.000000;15.000000;0.000000 size=374B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507412,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "sdp.statoil.no_wikidocs",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507418,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H sustainability.equinor.com -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.192991361,
      "executed": 1581507418,
      "history": [
        {
          "status": 0,
          "executed": 1581506218
        },
        {
          "status": 0,
          "executed": 1581506278
        },
        {
          "status": 0,
          "executed": 1581506338
        },
        {
          "status": 0,
          "executed": 1581506398
        },
        {
          "status": 0,
          "executed": 1581506458
        },
        {
          "status": 0,
          "executed": 1581506518
        },
        {
          "status": 0,
          "executed": 1581506578
        },
        {
          "status": 0,
          "executed": 1581506638
        },
        {
          "status": 0,
          "executed": 1581506698
        },
        {
          "status": 0,
          "executed": 1581506758
        },
        {
          "status": 0,
          "executed": 1581506818
        },
        {
          "status": 0,
          "executed": 1581506878
        },
        {
          "status": 0,
          "executed": 1581506938
        },
        {
          "status": 0,
          "executed": 1581506998
        },
        {
          "status": 0,
          "executed": 1581507058
        },
        {
          "status": 0,
          "executed": 1581507118
        },
        {
          "status": 0,
          "executed": 1581507178
        },
        {
          "status": 0,
          "executed": 1581507238
        },
        {
          "status": 0,
          "executed": 1581507298
        },
        {
          "status": 0,
          "executed": 1581507358
        },
        {
          "status": 0,
          "executed": 1581507418
        }
      ],
      "issued": 1581507418,
      "output": "HTTP OK: HTTP/1.1 301 Moved Permanently - 224 bytes in 0.188 second response time |time=0.188292s;5.000000;10.000000;0.000000 size=224B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507418,
      "occurrences": 8801,
      "occurrences_watermark": 8801,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "sustainability.statoil.com",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507442,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H sustainability.equinor.com --sni -C 90,45",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.241538561,
      "executed": 1581507441,
      "history": [
        {
          "status": 0,
          "executed": 1581506241
        },
        {
          "status": 0,
          "executed": 1581506301
        },
        {
          "status": 0,
          "executed": 1581506361
        },
        {
          "status": 0,
          "executed": 1581506421
        },
        {
          "status": 0,
          "executed": 1581506481
        },
        {
          "status": 0,
          "executed": 1581506541
        },
        {
          "status": 0,
          "executed": 1581506601
        },
        {
          "status": 0,
          "executed": 1581506661
        },
        {
          "status": 0,
          "executed": 1581506721
        },
        {
          "status": 0,
          "executed": 1581506781
        },
        {
          "status": 0,
          "executed": 1581506841
        },
        {
          "status": 0,
          "executed": 1581506901
        },
        {
          "status": 0,
          "executed": 1581506962
        },
        {
          "status": 0,
          "executed": 1581507022
        },
        {
          "status": 0,
          "executed": 1581507081
        },
        {
          "status": 0,
          "executed": 1581507141
        },
        {
          "status": 0,
          "executed": 1581507201
        },
        {
          "status": 0,
          "executed": 1581507261
        },
        {
          "status": 0,
          "executed": 1581507321
        },
        {
          "status": 0,
          "executed": 1581507381
        },
        {
          "status": 0,
          "executed": 1581507441
        }
      ],
      "issued": 1581507441,
      "output": "SSL OK - Certificate 'sustainability.equinor.com' will expire in 364 days on 2021-02-10 12:00 +0000/UTC.\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507441,
      "occurrences": 4325,
      "occurrences_watermark": 4325,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "sustainability.statoil.com_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507401,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_http -H svn.statoil.no -w 5 -c 10",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.108131977,
      "executed": 1581507401,
      "history": [
        {
          "status": 0,
          "executed": 1581506201
        },
        {
          "status": 0,
          "executed": 1581506261
        },
        {
          "status": 0,
          "executed": 1581506321
        },
        {
          "status": 0,
          "executed": 1581506381
        },
        {
          "status": 0,
          "executed": 1581506441
        },
        {
          "status": 0,
          "executed": 1581506502
        },
        {
          "status": 0,
          "executed": 1581506561
        },
        {
          "status": 0,
          "executed": 1581506621
        },
        {
          "status": 0,
          "executed": 1581506681
        },
        {
          "status": 0,
          "executed": 1581506741
        },
        {
          "status": 0,
          "executed": 1581506801
        },
        {
          "status": 0,
          "executed": 1581506861
        },
        {
          "status": 0,
          "executed": 1581506921
        },
        {
          "status": 0,
          "executed": 1581506981
        },
        {
          "status": 0,
          "executed": 1581507041
        },
        {
          "status": 0,
          "executed": 1581507101
        },
        {
          "status": 0,
          "executed": 1581507161
        },
        {
          "status": 0,
          "executed": 1581507221
        },
        {
          "status": 0,
          "executed": 1581507281
        },
        {
          "status": 0,
          "executed": 1581507341
        },
        {
          "status": 0,
          "executed": 1581507401
        }
      ],
      "issued": 1581507401,
      "output": "HTTP OK: HTTP/1.1 200 OK - 12527 bytes in 0.103 second response time |time=0.103445s;5.000000;10.000000;0.000000 size=12527B;;;0\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507401,
      "occurrences": 1318,
      "occurrences_watermark": 1318,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "svn.statoil.no",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507409,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/local/bin/check_certificate.sh svn.statoil.no 443 30 15",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "external"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.208876013,
      "executed": 1581507409,
      "history": [
        {
          "status": 0,
          "executed": 1581506209
        },
        {
          "status": 0,
          "executed": 1581506269
        },
        {
          "status": 0,
          "executed": 1581506329
        },
        {
          "status": 0,
          "executed": 1581506389
        },
        {
          "status": 0,
          "executed": 1581506449
        },
        {
          "status": 0,
          "executed": 1581506509
        },
        {
          "status": 0,
          "executed": 1581506569
        },
        {
          "status": 0,
          "executed": 1581506629
        },
        {
          "status": 0,
          "executed": 1581506689
        },
        {
          "status": 0,
          "executed": 1581506749
        },
        {
          "status": 0,
          "executed": 1581506809
        },
        {
          "status": 0,
          "executed": 1581506869
        },
        {
          "status": 0,
          "executed": 1581506929
        },
        {
          "status": 0,
          "executed": 1581506989
        },
        {
          "status": 0,
          "executed": 1581507049
        },
        {
          "status": 0,
          "executed": 1581507109
        },
        {
          "status": 0,
          "executed": 1581507169
        },
        {
          "status": 0,
          "executed": 1581507229
        },
        {
          "status": 0,
          "executed": 1581507289
        },
        {
          "status": 0,
          "executed": 1581507349
        },
        {
          "status": 0,
          "executed": 1581507409
        }
      ],
      "issued": 1581507409,
      "output": "Certificate for svn.statoil.no expires in 101 days, good time ^___^\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507409,
      "occurrences": 1320,
      "occurrences_watermark": 1320,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "svn.statoil.no_certificate",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  },
  {
    "timestamp": 1581507431,
    "entity": {
      "entity_class": "agent",
      "system": {
        "hostname": "ai-linapp1112",
        "os": "linux",
        "platform": "centos",
        "platform_family": "rhel",
        "platform_version": "7.7.1908",
        "network": {
          "interfaces": [
            {
              "name": "lo",
              "addresses": [
                "127.0.0.1/8",
                "::1/128"
              ]
            },
            {
              "name": "eth0",
              "mac": "0a:3f:c1:cd:cb:02",
              "addresses": [
                "10.36.1.220/21",
                "fe80::83f:c1ff:fecd:cb02/64"
              ]
            },
            {
              "name": "br-10a6dab0ab87",
              "mac": "02:42:7f:c9:5a:ba",
              "addresses": [
                "172.20.0.1/16"
              ]
            },
            {
              "name": "docker0",
              "mac": "02:42:08:e2:b8:18",
              "addresses": [
                "172.17.0.1/16"
              ]
            },
            {
              "name": "br-b0b15503308f",
              "mac": "02:42:e1:12:d0:16",
              "addresses": [
                "172.24.0.1/16",
                "fe80::42:e1ff:fe12:d016/64"
              ]
            },
            {
              "name": "br-b1997b3adf37",
              "mac": "02:42:6f:c8:8b:a1",
              "addresses": [
                "172.18.0.1/16",
                "fe80::42:6fff:fec8:8ba1/64"
              ]
            },
            {
              "name": "br-b3ecd7c4d878",
              "mac": "02:42:31:a4:6b:28",
              "addresses": [
                "172.23.0.1/16",
                "fe80::42:31ff:fea4:6b28/64"
              ]
            },
            {
              "name": "br-d8bb21ed7a68",
              "mac": "02:42:ee:f6:46:bf",
              "addresses": [
                "172.21.0.1/16",
                "fe80::42:eeff:fef6:46bf/64"
              ]
            },
            {
              "name": "veth1e963be",
              "mac": "fa:fc:22:67:f4:79",
              "addresses": [
                "fe80::f8fc:22ff:fe67:f479/64"
              ]
            },
            {
              "name": "veth0efb82e",
              "mac": "3a:c7:58:48:3a:36",
              "addresses": [
                "fe80::38c7:58ff:fe48:3a36/64"
              ]
            },
            {
              "name": "vethbde48d9",
              "mac": "6e:e4:6d:b4:a8:b8",
              "addresses": [
                "fe80::6ce4:6dff:feb4:a8b8/64"
              ]
            },
            {
              "name": "veth2fff23a",
              "mac": "8a:07:51:e7:67:24",
              "addresses": [
                "fe80::8807:51ff:fee7:6724/64"
              ]
            },
            {
              "name": "vethd011bc8",
              "mac": "36:8e:90:9b:1e:a0",
              "addresses": [
                "fe80::348e:90ff:fe9b:1ea0/64"
              ]
            }
          ]
        },
        "arch": "amd64"
      },
      "subscriptions": [
        "base",
        "external",
        "entity:vmm05.prod.sdp.statoil.no"
      ],
      "last_seen": 1580386490,
      "deregister": false,
      "deregistration": {},
      "user": "agent",
      "redact": [
        "password",
        "passwd",
        "pass",
        "api_key",
        "api_token",
        "access_key",
        "secret_key",
        "private_key",
        "secret"
      ],
      "metadata": {
        "name": "vmm05.prod.sdp.statoil.no",
        "namespace": "default"
      },
      "sensu_agent_version": "5.16.1"
    },
    "check": {
      "command": "/usr/lib64/nagios/plugins/check_swap -w 50% -c 20% --no-swap=ok",
      "handlers": [],
      "high_flap_threshold": 0,
      "interval": 60,
      "low_flap_threshold": 0,
      "publish": true,
      "runtime_assets": null,
      "subscriptions": [
        "base"
      ],
      "proxy_entity_name": "",
      "check_hooks": null,
      "stdin": false,
      "subdue": null,
      "ttl": 0,
      "timeout": 0,
      "round_robin": false,
      "duration": 0.004524876,
      "executed": 1581507431,
      "history": [
        {
          "status": 0,
          "executed": 1581506231
        },
        {
          "status": 0,
          "executed": 1581506291
        },
        {
          "status": 0,
          "executed": 1581506351
        },
        {
          "status": 0,
          "executed": 1581506411
        },
        {
          "status": 0,
          "executed": 1581506471
        },
        {
          "status": 0,
          "executed": 1581506531
        },
        {
          "status": 0,
          "executed": 1581506591
        },
        {
          "status": 0,
          "executed": 1581506651
        },
        {
          "status": 0,
          "executed": 1581506711
        },
        {
          "status": 0,
          "executed": 1581506771
        },
        {
          "status": 0,
          "executed": 1581506831
        },
        {
          "status": 0,
          "executed": 1581506891
        },
        {
          "status": 0,
          "executed": 1581506951
        },
        {
          "status": 0,
          "executed": 1581507011
        },
        {
          "status": 0,
          "executed": 1581507071
        },
        {
          "status": 0,
          "executed": 1581507131
        },
        {
          "status": 0,
          "executed": 1581507191
        },
        {
          "status": 0,
          "executed": 1581507251
        },
        {
          "status": 0,
          "executed": 1581507311
        },
        {
          "status": 0,
          "executed": 1581507371
        },
        {
          "status": 0,
          "executed": 1581507431
        }
      ],
      "issued": 1581507431,
      "output": "SWAP OK - 100% free (2047 MB out of 2047 MB) |swap=2047MB;1023;409;0;2047\n",
      "state": "passing",
      "status": 0,
      "total_state_change": 0,
      "last_ok": 1581507431,
      "occurrences": 18569,
      "occurrences_watermark": 18569,
      "output_metric_format": "",
      "output_metric_handlers": null,
      "env_vars": null,
      "metadata": {
        "name": "swap",
        "namespace": "default"
      }
    },
    "metadata": {
      "namespace": "default"
    }
  }
]
'''
