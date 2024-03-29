import json

data = """
[
    {
        "id": 1,
        "interfaces": [
            {
                "id": 1,
                "traffic_data": [
                    {
                        "id": 1,
                        "timestamp": "2024-03-15T12:50:09Z",
                        "inbound_traffic": 1460.0,
                        "outbound_traffic": 1390.0,
                        "time_start": "2024-03-15T09:50:15Z",
                        "interfacesTrafficData": 1
                    },
                    {
                        "id": 2,
                        "timestamp": "2024-03-06T16:53:35Z",
                        "inbound_traffic": 5609.0,
                        "outbound_traffic": 6042.0,
                        "time_start": "2024-03-06T10:54:00Z",
                        "interfacesTrafficData": 1
                    },
                    {
                        "id": 3,
                        "timestamp": "2024-03-12T08:22:09Z",
                        "inbound_traffic": 7603.0,
                        "outbound_traffic": 6738.0,
                        "time_start": "2024-03-11T13:22:28Z",
                        "interfacesTrafficData": 1
                    }
                ],
                "Bandwidth_Usage": [
                    {
                        "id": 1,
                        "timestamp": "2024-03-15T13:22:57Z",
                        "bandwidth_usage": 100.0,
                        "interfacesBandwidthUsage": 1
                    }
                ],
                "name": "Ethernet 1",
                "speed": 1000.0,
                "status": "подключено",
                "duplex_mode": "полный",
                "deviceInterface": 1
            }
        ],
        "Network_Events": [
            {
                "id": 1,
                "timestamp": "2024-03-15T13:28:29Z",
                "event_type": "Включение",
                "severity_level": "0",
                "deviceNetworkEvents": 1
            }
        ],
        "Device_Temperature": [
            {
                "id": 1,
                "timestamp": "2024-03-15T12:50:26Z",
                "temperature": 65.0,
                "deviceDeviceTemperature": 1
            },
            {
                "id": 2,
                "timestamp": "2024-03-15T13:28:52Z",
                "temperature": 33.0,
                "deviceDeviceTemperature": 1
            }
        ],
        "Power_Consumption": [
            {
                "id": 1,
                "timestamp": "2024-03-15T13:27:14Z",
                "power_consumption": 431.0,
                "devicePowerConsumption": 1
            },
            {
                "id": 2,
                "timestamp": "2024-03-09T12:00:00Z",
                "power_consumption": 389.0,
                "devicePowerConsumption": 1
            },
            {
                "id": 3,
                "timestamp": "2024-03-05T19:00:00Z",
                "power_consumption": 455.0,
                "devicePowerConsumption": 1
            },
            {
                "id": 4,
                "timestamp": "2024-03-17T13:27:57Z",
                "power_consumption": 378.0,
                "devicePowerConsumption": 1
            },
            {
                "id": 5,
                "timestamp": "2024-02-21T18:00:00Z",
                "power_consumption": 285.0,
                "devicePowerConsumption": 1
            }
        ],
        "Device_Configuration": [
            {
                "id": 1,
                "timestamp": "2024-03-15T13:23:03Z",
                "configuration_details": "***Код конфигурации***",
                "deviceDeviceConfiguration": 1
            }
        ],
        "Performance_Metrics": [
            {
                "id": 1,
                "timestamp": "2024-03-15T13:23:35Z",
                "cpu_usage": 50.0,
                "memory_usage": 55.0,
                "storage_ussage": 61.0,
                "devicePerformanceMetrics": 1
            },
            {
                "id": 2,
                "timestamp": "2024-03-07T12:00:00Z",
                "cpu_usage": 37.0,
                "memory_usage": 45.0,
                "storage_ussage": 66.0,
                "devicePerformanceMetrics": 1
            },
            {
                "id": 3,
                "timestamp": "2024-03-11T12:20:31Z",
                "cpu_usage": 56.0,
                "memory_usage": 88.0,
                "storage_ussage": 90.0,
                "devicePerformanceMetrics": 1
            },
            {
                "id": 4,
                "timestamp": "2024-03-01T17:42:49Z",
                "cpu_usage": 64.0,
                "memory_usage": 78.0,
                "storage_ussage": 82.0,
                "devicePerformanceMetrics": 1
            }
        ],
        "PacketLoss_Data": [
            {
                "id": 1,
                "timestamp": "2024-03-15T12:52:50Z",
                "packet_loss": 2.4,
                "devicePacketLossData": 1
            },
            {
                "id": 2,
                "timestamp": "2024-03-15T13:26:01Z",
                "packet_loss": 13.0,
                "devicePacketLossData": 1
            },
            {
                "id": 3,
                "timestamp": "2024-03-13T12:00:00Z",
                "packet_loss": 2.4,
                "devicePacketLossData": 1
            },
            {
                "id": 4,
                "timestamp": "2024-03-02T16:26:24Z",
                "packet_loss": 4.0,
                "devicePacketLossData": 1
            },
            {
                "id": 5,
                "timestamp": "2024-03-09T13:26:41Z",
                "packet_loss": 1.0,
                "devicePacketLossData": 1
            },
            {
                "id": 6,
                "timestamp": "2024-03-13T22:00:00Z",
                "packet_loss": 1.2,
                "devicePacketLossData": 1
            },
            {
                "id": 7,
                "timestamp": "2024-03-15T13:27:06Z",
                "packet_loss": 0.0,
                "devicePacketLossData": 1
            }
        ],
        "purpose": "Пересылка файлов",
        "location": "Москва",
        "typeNetworkDevice": 1,
        "IPAddressNetworkDevice": 1
    }
]
"""
data = """{ "NetworkDevices" : """ + data + "}"
data = json.loads(data)
print(type(data))