
from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),

    path("logout/", views.cerrar_sesion, name="logout"),

    # Módulo de contabilidad
    path('contabilidad/', views.contabilidad, name='contabilidad'),

    # Módulo de facturación
    path('facturacioncxc/', views.facturacioncxc, name='facturacioncxc'),

    # Módulo de terceros
    path('terceros/', views.listar_terceros, name='listar_terceros'),
    path('terceros/registrar/', views.registrar_tercero, name='registrar_tercero'),
    path('terceros/editar/<int:id>/', views.editar_tercero, name='editar_tercero'), 
    path('terceros/eliminar/<int:id>/', views.eliminar_tercero, name='eliminar_tercero'),

    # botones del menu configuraciones
    path('contabilidad/configuracion/', views.configuracion, name='configuracion'),

    # Secciones de Configuración
    path('contabilidad/configuracion/plan-cuentas/', views.plan_cuentas, name='plan_cuentas'),
    path('contabilidad/configuracion/centros-costos/', views.centros_costos, name='centros_costos'),
    path('contabilidad/configuracion/criterios/', views.criterios, name='criterios'),
    path('contabilidad/configuracion/tablas-impuestos/', views.tablas_impuestos, name='tablas_impuestos'),
    path('contabilidad/configuracion/sucursales/', views.sucursales, name='sucursales'),
    path('contabilidad/configuracion/usuarios-permisos/', views.usuarios_permisos, name='usuarios_permisos'),

    # plan de cuentas
    path('contabilidad/configuracion/plan-cuentas/crear/', views.cuenta_crear, name='cuenta_crear'),
    path('contabilidad/configuracion/plan-cuentas/editar/<int:id>/', views.cuenta_editar, name='cuenta_editar'),
    path('contabilidad/configuracion/plan-cuentas/eliminar/<int:id>/', views.cuenta_eliminar, name='cuenta_eliminar'),


    #__________________insertar csv plan de cuentas
    path('contabilidad/configuracion/plan-cuentas/export/csv/', views.cuentas_export_csv, name='cuentas_export_csv'),
    path('contabilidad/configuracion/plan-cuentas/import/csv/', views.cuentas_import_csv, name='cuentas_import_csv'),
    path('contabilidad/configuracion/plan-cuentas/plantilla/csv/', views.cuentas_plantilla_csv, name='cuentas_plantilla_csv'),

    #__________________formulario crear documento contable
    path('contabilidad/configuracion/documentos-contables/', views.documentos_contables, name='documentos_contables'),

    #____________Api autocomplete paths del formulario registros contables
    path('api/cuentas/', views.api_cuentas_movimiento, name='api_cuentas'),
    path('api/terceros/', views.api_terceros, name='api_terceros'),
    path('contabilidad/registros/nuevo/', views.asiento_crear_ui, name='asiento_crear'),
    
    # path('contabilidad/registros/editar/<int:id>/', views.asiento_editar, name='asiento_editar'),
    path('api/asiento/get/', views.api_asiento_get, name='api_asiento_get'),
    path('api/asiento/delete/', views.api_asiento_delete, name='api_asiento_delete'),
    path('api/documentos/next-number/', views.api_documento_next_number, name='api_documento_next_number'),
    
    path('contabilidad/registros/', views.asientos_listar, name='asientos_listar'),
    path('contabilidad/registros/importar-csv/', views.asiento_importar_csv, name='asiento_importar_csv'),
    # modulo de reportes________________
    path('contabilidad/reportes/', views.reportes_movimientos, name='reportes_movimientos'),
    path('contabilidad/reportes/export/csv/', views.reportes_export_csv, name='reportes_export_csv'),


    # Botones de la interfaz principal de facturacion
    path('facturacion/facturar/', views.fv_crear, name='fv_crear'),
    path('facturacion/nota-credito/', views.nc_crear, name='nc_crear'),
    
    path('facturacion/inventarios/', views.inventarios, name='inventarios'),
    path('facturacion/inventarios/guardar/', views.inventarios_guardar, name='inventarios_guardar'),

    path('facturacion/reportes/', views.fact_reportes, name='fact_reportes'),
    path('facturacion/tesoreria/', views.tesoreria, name='tesoreria'),
    path('facturacion/parametros/', views.parametros, name='fact_parametros'),
    
    
    path("facturacion/datos-facturacion/", views.datos_facturacion, name="datos_facturacion"),
    path('facturacion/inventarios/eliminar/', views.inventarios_eliminar, name='inventarios_eliminar'),
    path('api/terceros/por-identificacion/', views.tercero_por_identificacion, name='tercero_por_identificacion'), 
    path('facturacion/facturar/guardar/', views.fv_guardar, name='fv_guardar'),
    path("facturacion/fv/buscar/", views.fv_por_consecutivo, name="fv_por_consecutivo"),
    # path('factura/pdf/<int:factura_id>/', views.fv_pdf, name='fv_pdf'),
    path("factura/pdf/<int:id>/", views.factura_pdf, name="factura_pdf"),



    # nota credito
    path("nota-credito/crear/", views.nc_crear, name="nc_crear"),
    path("nota-credito/guardar/", views.nc_guardar, name="nc_guardar"),
    path("nota-credito/pdf/<int:pk>/", views.nc_pdf, name="nc_pdf"),
    path("factura-venta/por-consecutivo/", views.fv_por_consecutivo, name="fv_por_consecutivo"),
    path("nota-credito/por-consecutivo/", views.nc_por_consecutivo, name="nc_por_consecutivo"),



    # rutas para guardar en param_medios_pago.html
    path('facturacion/medios-pago/', views.param_medios_pago, name='param_medios_pago'),
    path("medios-pago/guardar/", views.mp_guardar, name="mp_guardar"),
    path("medios-pago/eliminar/", views.mp_eliminar, name="mp_eliminar"),


    # rutas para guardar en recibo_caja.html
    path('facturacion/tesoreria/recibo-caja/', views.recibo_caja, name='recibo_caja'),
    path("recibo-caja/guardar/", views.rc_guardar, name="rc_guardar"),
    path("recibo-caja/buscar/", views.rc_buscar, name="rc_buscar"),
    path( "facturacion/reporte-cartera/", views.reporte_cartera, name="reporte_cartera"),
    path("facturacion/reporte-cartera/nc/<int:factura_id>/", views.cartera_detalle_nc, name="cartera_detalle_nc"),
    path("facturacion/reporte-cartera/pagos/<str:consecutivo>/", views.cartera_detalle_pagos, name="cartera_detalle_pagos"),


    # automatizacion del recibo de caja
    path("terceros/validar-nit/", views.validar_nit, name="validar_nit"),

    # contabilizacion del recibo de caja
    path("tesoreria/rc/contabilizar/", views.rc_contabilizar, name="rc_contabilizar"),



   # modulo de Nomina
   path("nomina/", views.nomina_panel, name="nomina_panel"),
   path("nomina/personal/ingreso/", views.ingreso_personal, name="nomina_ingreso_personal"),
   path("nomina/conceptos/", views.nomina_conceptos, name="nomina_conceptos"),
   path("nomina/conceptos/crear/", views.nomina_concepto_crear, name="nomina_concepto_crear"),
   path("nomina/conceptos/eliminar/", views.nomina_concepto_eliminar, name="nomina_concepto_eliminar"),
   path("nomina/conceptos/modificar/", views.nomina_concepto_modificar, name="nomina_concepto_modificar"),
   path("nomina/parametrizar-asociar/", views.nomina_parametrizacion_asociacion, name="nomina_parametrizar_asociar"),
   
   path("nomina/parametros/", views.nomina_parametros, name="nomina_parametros"),

   path("nomina/parametros/api/guardar/", views.nomina_parametro_guardar, name="nomina_parametro_guardar"),
   path("nomina/parametros/api/modificar/", views.nomina_parametro_modificar, name="nomina_parametro_modificar"),
   path("nomina/parametros/api/eliminar/", views.nomina_parametro_eliminar, name="nomina_parametro_eliminar"),

   # novedades de ingreso de nomina
   
   path("nomina/ingreso-novedades/", views.ingreso_novedades, name="ingreso_novedades"),

   path("nomina/ingreso-personal/", views.ingreso_personal, name="ingreso_personal"),
   path("nomina/personal/buscar/", views.empleado_por_cedula, name="empleado_por_cedula"),

    path("nomina/novedades/ingreso/", views.ingreso_novedades, name="ingreso_novedades"),
    path("nomina/novedades/crear/", views.novedad_crear, name="novedad_crear"),
    path("nomina/novedades/eliminar/", views.novedad_eliminar, name="novedad_eliminar"),


    path("nomina/subpanel/", views.nomina_subpanel, name="nomina_subpanel"),
    # path("nomina/cargue/", views.nomina_cargue, name="nomina_cargue"),
    path("nomina/cargue/", views.nomina_cargue_formulario, name="nomina_cargue"),
    path("nomina/cargue/remove-line/", views.nomina_cargue_remove_line, name="nomina_cargue_remove_line"),

    path("nomina/auxilio-info/", views.nomina_auxilio_info, name="nomina_auxilio_info"),
    path("nomina/param-calc/", views.nomina_param_calc_data, name="nomina_param_calc_data"),
    path("nomina/novedades/data/", views.nomina_novedades_data, name="nomina_novedades_data"),

    path("nomina/cargue/guardar/", views.nomina_cargue_guardar, name="nomina_cargue_guardar"),
    path("nomina/cargue/eliminar/", views.nomina_cargue_eliminar, name="nomina_cargue_eliminar"),
    path("nomina/cargue/exportar/", views.nomina_cargue_exportar_excel, name="nomina_cargue_exportar_excel"),
    path("nomina/historial/", views.historial_nominas, name="historial_nominas"),
    
    path("nomina/ver/", views.nomina_ver, name="nomina_ver"),
    path("nomina/cargue-contable/", views.nomina_cargue_contable, name="nomina_cargue_contable"),
    path("nomina/contabilizar/", views.ContabilizarNomina, name="contabilizar_nomina"),

    path("nomina/eliminar/", views.nomina_eliminar, name="nomina_eliminar"),


    path("nomina/pago/", views.pago_nomina, name="pago_nomina"),
    path("nomina/pago/contabilizar/", views.Contabilizar_guardar_nominapago, name="Contabilizar_guardar_nominapago"),


    path("nomina/Nomina-desprendibles/", views.nomina_cargue_desprendibles, name="nomina_cargue_desprendibles"),


    path("nomina/certificados/", views.certificados_subpanel, name="certificados_subpanel"),

    path("nomina/parametros-desprendibles/", views.parametros_desprendibles, name="parametros_desprendibles"),

    path("nomina/desprendible-pdf/<str:no_nomina>/<str:cedula>/", views.ver_desprendible_pdf, name="ver_desprendible_pdf"),
    
    path("nomina/enviar-desprendible/<str:no_nomina>/<str:cedula>/", views.enviar_desprendible_email, name="enviar_desprendible_email"),
    

    path("nomina/reportes/acumulados/", views.reportes_acumulados, name="reportes_acumulados"),

    path("nomina/reportes/graficas/", views.graficas_nomina, name="graficas_nomina"),



    # balances_contables.html
    path("contabilidad/balances/", views.balances_contables, name="balances_contables"),

    path("contabilidad/balances/exportar-excel/", views.exportar_balance_mensualizado_excel, name="exportar_balance_mensualizado_excel"),
   
    path("contabilidad/reportes-subpanel-cont/", views.reportes_subpanel_contabilidad, name="reportes_subpanel_contabilidad"),

]



    
    


