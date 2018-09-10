import boto3

s3 = boto3.client('s3')

argo_carrier_visit = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/argo_carrier_visit/'
        )

argo_chargeable_unit_events = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/argo_chargeable_unit_events/'
        )

argo_visit_details = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/argo_visit_details/'
    )

argo_yard = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/argo_yard/'
    )

crg_bills_of_lading = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/crg_bills_of_lading/'
    )

crg_bl_goods = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/crg_bl_goods/'
    )

inv_goods = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/inv_goods/'
    )

inv_move_event = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/inv_move_event/'
    )

inv_unit = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/inv_unit/'
    )

inv_unit_fcy_visit = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/inv_unit_fcy_visit/'
    )

inv_unit_yrd_visit = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/inv_unit_yrd_visit/'
    )

inv_wi = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/inv_wi/'
    )

inv_wi_tracking = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/inv_wi_tracking/'
    )

inv_wq = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/inv_wq/'
    )

mns_che_move_statistics = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/mns_che_move_statistics/'
    )

mns_che_operator_statistics = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/mns_che_operator_statistics/'
    )

mns_che_session = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/mns_che_session/'
    )

mns_che_session_period = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/mns_che_session_period/'
    )

mns_che_status = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/mns_che_status/'
    )

mns_che_trip_statistics = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/mns_che_trip_statistics/'
    )

xps_che = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/xps_che/'
    )

xps_ecevent = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/xps_ecevent/'
    )

xps_ecuser = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/xps_ecuser/'
    )

ref_bizunit_scoped= s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/ref_bizunit_scoped/'
    )

ref_carrier_itinerary= s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/ref_carrier_itinerary/'
    )

ref_carrier_service= s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/ref_carrier_service/'
    )

ref_country= s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/ref_country/'
    )

ref_equip_type = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/ref_equip_type/'
    )

ref_equipment= s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/ref_equipment/'
    )

ref_line_operator = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/ref_line_operator/'
    )

ref_routing_point = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/ref_routing_point/'
    )

ref_unloc_code = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/ref_unloc_code/'
    )

srv_event = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/srv_event/'
    )

srv_event_types = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/srv_event_types/'
    )

road_truck_actions = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/road_truck_actions/'
    )

road_truck_company_drivers = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/road_truck_company_drivers/'
    )

road_truck_drivers = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/road_truck_drivers/'
    )

road_truck_transaction_stages = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/road_truck_transaction_stages/'
    )

road_truck_transactions = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/road_truck_transactions/'
    )

road_truck_visit_details = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/road_truck_visit_details/'
    )

road_truck_visit_stages = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/road_truck_visit_stages/'
    )

road_truck_visit_stats = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/road_truck_visit_stats/'
    )

vsl_vessel_classes = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/vsl_vessel_classes/'
    )

vsl_vessel_visit_details = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/vsl_vessel_visit_details/'
    )

vsl_vessel_visit_lines = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/vsl_vessel_visit_lines/'
    )

vsl_vessels = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/vsl_vessels/'
    )


