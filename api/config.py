import os


class Config:
    export_secret = os.getenv("EXPORT_SECRET")
    deployment_name = os.getenv("DEPLOYMENT_NAME", "none")
    _ignore_alert_list_ = os.getenv('IGNORE_PROMETHEUS_ALERTS')
    ignore_alert_list = _ignore_alert_list_.split(',') if _ignore_alert_list_ else []
    _import_urls_list_ = os.getenv("IMPORT_URLS")
    import_urls_list = _import_urls_list_.split(";") if _import_urls_list_ else []
    flask_debug = os.getenv('FLASK_DEBUG', False)
    prometheus_api = os.getenv('PROMETHEUS_API')
    sensu_api = os.getenv('SENSU_API')
    sensu_key = os.getenv("SENSU_KEY")


    mockdata2 = r'''{"status":"success","data":{"alerts":[{"labels":{"alertname":"Watchdog","severity":"none"},"annotations":{"message":"This is an alert meant to ensure that the entire alerting pipeline is functional.This alert is always firing, therefore it should always be firing in Alertmanagerand always fire against a receiver. There are integrations with various notificationmechanisms that send a notification when this alert is not firing. For example the\"DeadMansSnitch\" integration in PagerDuty."},"state":"firing","activeAt":"2019-04-07T05:52:15.470372903Z","value":1}]}}
    '''
    mock_data = '''
    {"status":"success","data":{"alerts":[{"labels":{"alertname":"TargetDown","job":"apiserver","severity":"warning"},"annotations":{"message":"100% of the apiserver targets are down."},"state":"firing","activeAt":"2019-03-14T01:12:15.470372903Z","value":100},{"labels":{"alertname":"TargetDown","job":"kube-dns","severity":"warning"},"annotations":{"message":"100% of the kube-dns targets are down."},"state":"firing","activeAt":"2019-03-14T01:12:15.470372903Z","value":100},{"labels":{"alertname":"DeadMansSwitch","severity":"none"},"annotations":{"message":"This is a DeadMansSwitch meant to ensure that the entire alerting pipeline is functional."},"state":"firing","activeAt":"2019-03-14T01:12:15.470372903Z","value":1},{"labels":{"alertname":"KubePodCrashLooping","container":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"filebeat-hllqh","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Pod monitoring/filebeat-hllqh (filebeat) is restarting 0.00 times / second.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodcrashlooping"},"state":"firing","activeAt":"2019-03-14T01:14:49.362790506Z","value":0.003448275862068966},{"labels":{"alertname":"KubePodCrashLooping","container":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"filebeat-bg5hb","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Pod monitoring/filebeat-bg5hb (filebeat) is restarting 0.00 times / second.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodcrashlooping"},"state":"firing","activeAt":"2019-03-14T01:15:19.362790506Z","value":0.0022988505747126436},{"labels":{"alertname":"KubePodNotReady","namespace":"kube-system","pod":"oauth2-proxy-ks-6b9dd85456-s6dsg","severity":"critical"},"annotations":{"message":"Pod kube-system/oauth2-proxy-ks-6b9dd85456-s6dsg has been in a non-ready state for longer than an hour.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodnotready"},"state":"firing","activeAt":"2019-03-14T01:12:49.362790506Z","value":1},{"labels":{"alertname":"KubeDeploymentReplicasMismatch","deployment":"oauth2-proxy-ks","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"kube-system","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Deployment kube-system/oauth2-proxy-ks has not matched the expected number of replicas for longer than an hour.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedeploymentreplicasmismatch"},"state":"firing","activeAt":"2019-03-14T01:12:49.362790506Z","value":1},{"labels":{"alertname":"KubeDaemonSetRolloutStuck","daemonset":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Only 0% of the desired Pods of DaemonSet monitoring/filebeat are scheduled and ready.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedaemonsetrolloutstuck"},"state":"firing","activeAt":"2019-03-14T01:12:49.362790506Z","value":0},{"labels":{"alertname":"KubeJobCompletion","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","job_name":"elasticsearch-curator-1552611600","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"warning"},"annotations":{"message":"Job monitoring/elasticsearch-curator-1552611600 is taking more than one hour to complete.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubejobcompletion"},"state":"firing","activeAt":"2019-03-15T01:00:49.362790506Z","value":1},{"labels":{"alertname":"KubeJobFailed","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","job_name":"elasticsearch-curator-1552611600","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"warning"},"annotations":{"message":"Job monitoring/elasticsearch-curator-1552611600 failed to complete.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubejobfailed"},"state":"firing","activeAt":"2019-03-15T01:00:49.362790506Z","value":6},{"labels":{"alertname":"CPUThrottlingHigh","container_name":"config-reloader","namespace":"monitoring","pod_name":"alertmanager-prometheus-operator-alertmanager-0","severity":"warning"},"annotations":{"message":"33% throttling of CPU in namespace monitoring for container config-reloader in pod alertmanager-prometheus-operator-alertmanager-0.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh"},"state":"firing","activeAt":"2019-03-15T11:07:34.559334876Z","value":33.333333333333336},{"labels":{"alertname":"CPUThrottlingHigh","container_name":"rules-configmap-reloader","namespace":"monitoring","pod_name":"prometheus-prometheus-operator-prometheus-0","severity":"warning"},"annotations":{"message":"33% throttling of CPU in namespace monitoring for container rules-configmap-reloader in pod prometheus-prometheus-operator-prometheus-0.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh"},"state":"pending","activeAt":"2019-03-15T11:12:34.559334876Z","value":33.333333333333336},{"labels":{"alertname":"CPUThrottlingHigh","container_name":"prometheus-config-reloader","namespace":"monitoring","pod_name":"prometheus-prometheus-operator-prometheus-0","severity":"warning"},"annotations":{"message":"33% throttling of CPU in namespace monitoring for container prometheus-config-reloader in pod prometheus-prometheus-operator-prometheus-0.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh"},"state":"firing","activeAt":"2019-03-15T10:56:34.559334876Z","value":33.333333333333336},{"labels":{"alertname":"CPUThrottlingHigh","container_name":"heapster-nanny","namespace":"kube-system","pod_name":"heapster-5fb7488d97-l5mtl","severity":"warning"},"annotations":{"message":"25% throttling of CPU in namespace kube-system for container heapster-nanny in pod heapster-5fb7488d97-l5mtl.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh"},"state":"pending","activeAt":"2019-03-15T11:25:34.559334876Z","value":25.2},{"labels":{"alertname":"KubeAPIDown","severity":"critical"},"annotations":{"message":"KubeAPI has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapidown"},"state":"firing","activeAt":"2019-03-14T01:12:24.667662181Z","value":1},{"labels":{"alertname":"KubeControllerManagerDown","severity":"critical"},"annotations":{"message":"KubeControllerManager has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubecontrollermanagerdown"},"state":"firing","activeAt":"2019-03-14T01:12:24.667662181Z","value":1},{"labels":{"alertname":"KubeSchedulerDown","severity":"critical"},"annotations":{"message":"KubeScheduler has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeschedulerdown"},"state":"firing","activeAt":"2019-03-14T01:12:24.667662181Z","value":1},{"labels":{"alertname":"TargetDown","job":"apiserver","severity":"warning"},"annotations":{"description":"100% of apiserver targets are down.","summary":"Targets are down"},"state":"firing","activeAt":"2019-03-14T01:12:08.503964295Z","value":100},{"labels":{"alertname":"TargetDown","job":"kube-dns","severity":"warning"},"annotations":{"description":"100% of kube-dns targets are down.","summary":"Targets are down"},"state":"firing","activeAt":"2019-03-14T01:12:08.503964295Z","value":100},{"labels":{"alertname":"DeadMansSwitch","severity":"none"},"annotations":{"description":"This is a DeadMansSwitch meant to ensure that the entire Alerting pipeline is functional.","summary":"Alerting DeadMansSwitch"},"state":"firing","activeAt":"2019-03-14T01:12:08.503964295Z","value":1},{"labels":{"alertname":"CoreDNSDown","severity":"critical"},"annotations":{"message":"CoreDNS has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-corednsdown"},"state":"firing","activeAt":"2019-03-14T01:12:22.392757395Z","value":1},{"labels":{"alertname":"KubeAPIDown","severity":"critical"},"annotations":{"message":"KubeAPI has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapidown"},"state":"firing","activeAt":"2019-03-14T01:12:22.392757395Z","value":1},{"labels":{"alertname":"KubeControllerManagerDown","severity":"critical"},"annotations":{"message":"KubeControllerManager has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubecontrollermanagerdown"},"state":"firing","activeAt":"2019-03-14T01:12:22.392757395Z","value":1},{"labels":{"alertname":"KubeSchedulerDown","severity":"critical"},"annotations":{"message":"KubeScheduler has disappeared from Prometheus target discovery.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeschedulerdown"},"state":"firing","activeAt":"2019-03-14T01:12:22.392757395Z","value":1},{"labels":{"alertname":"KubePodCrashLooping","container":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"filebeat-hllqh","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Pod monitoring/filebeat-hllqh (filebeat) is restarting 1.03 times / 5 minutes.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodcrashlooping"},"state":"firing","activeAt":"2019-03-14T01:14:47.743318242Z","value":1.0344827586206897},{"labels":{"alertname":"KubePodCrashLooping","container":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"filebeat-bg5hb","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Pod monitoring/filebeat-bg5hb (filebeat) is restarting 0.69 times / 5 minutes.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodcrashlooping"},"state":"firing","activeAt":"2019-03-14T01:15:17.743318242Z","value":0.6896551724137931},{"labels":{"alertname":"KubePodNotReady","namespace":"kube-system","pod":"oauth2-proxy-ks-6b9dd85456-s6dsg","severity":"critical"},"annotations":{"message":"Pod kube-system/oauth2-proxy-ks-6b9dd85456-s6dsg has been in a non-ready state for longer than an hour.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodnotready"},"state":"firing","activeAt":"2019-03-14T01:12:47.743318242Z","value":1},{"labels":{"alertname":"KubeDeploymentReplicasMismatch","deployment":"oauth2-proxy-ks","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"kube-system","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Deployment kube-system/oauth2-proxy-ks has not matched the expected number of replicas for longer than an hour.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedeploymentreplicasmismatch"},"state":"firing","activeAt":"2019-03-14T01:12:47.743318242Z","value":1},{"labels":{"alertname":"KubeDaemonSetRolloutStuck","daemonset":"filebeat","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"critical"},"annotations":{"message":"Only 0% of the desired Pods of DaemonSet monitoring/filebeat are scheduled and ready.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedaemonsetrolloutstuck"},"state":"firing","activeAt":"2019-03-14T01:12:47.743318242Z","value":0},{"labels":{"alertname":"KubeJobCompletion","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","job_name":"elasticsearch-curator-1552611600","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"warning"},"annotations":{"message":"Job monitoring/elasticsearch-curator-1552611600 is taking more than one hour to complete.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubejobcompletion"},"state":"firing","activeAt":"2019-03-15T01:00:47.743318242Z","value":1},{"labels":{"alertname":"KubeJobFailed","endpoint":"http","instance":"10.244.1.78:8080","job":"kube-state-metrics","job_name":"elasticsearch-curator-1552611600","namespace":"monitoring","pod":"prometheus-operator-kube-state-metrics-54c7c9fd77-m49s4","service":"prometheus-operator-kube-state-metrics","severity":"warning"},"annotations":{"message":"Job monitoring/elasticsearch-curator-1552611600 failed to complete.","runbook_url":"https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubejobfailed"},"state":"firing","activeAt":"2019-03-15T01:00:47.743318242Z","value":6}]}}
'''
    sensu_mock_data = '''[
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
      "output": "SWAP OK - 100% free (11981 MB out of 11999 MB) |swap=11981MB;5999;2399;0;11999",
      "state": "error",
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
      "output": "Found host description file with valid content",
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
      "output": "DISK OK - free space: / 178252 MiB (64.64% inode=99%); /dev 3896 MiB (100.00% inode=100%); /boot 281 MiB (62.93% inode=100%); /tmp 8149 MiB (99.60% inode=100%); /var 5091 MiB (62.22% inode=100%);| /=97476MiB;220583;248156;0;275729 /dev=0MiB;3116;3506;0;3896 /boot=165MiB;380;428;0;476 /tmp=32MiB;6545;7363;0;8182 /var=3090MiB;6545;7363;0;8182",
      "state": "failing",
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
      "output": "My certname (bld01.prod.sdp.statoil.no) resolves to my IP (10.217.112.50)",
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
      "output": "OK - load average: 0.04, 0.08, 0.16|load1=0.040;80.000;90.000;0; load5=0.080;80.000;90.000;0; load15=0.160;80.000;90.000;0; ",
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
  }
]
'''
