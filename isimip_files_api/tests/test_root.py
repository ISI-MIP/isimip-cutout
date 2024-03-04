def test_success(client, mocker):
    mocker.patch('isimip_files_api.app.count_jobs', mocker.Mock(return_value={}))

    response = client.get('/')

    assert response.status_code == 200
    assert response.json.get('status') == 'ok'
    assert response.json.get('commands') == [
        'cdo',
        'create_mask',
        'ncks'
    ]
    assert response.json.get('operations') == [
        'select_bbox',
        'select_point',
        'mask_bbox',
        'mask_mask',
        'mask_country',
        'mask_landonly',
        'compute_mean',
        'output_csv',
        'create_mask',
        'cutout_bbox'
    ]
