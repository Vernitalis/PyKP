const zoomButtonsClasses = "btn-sm btn-ghost join-item"

const zoomControl = new ol.control.Zoom({
	className: "absolute bg-base-100 bottom-4 left-4 join join-vertical shadow-xl",
	zoomInClassName: zoomButtonsClasses,
	zoomOutClassName: zoomButtonsClasses
})

const countryOutlineStyle = new ol.style.Style({
	fill: undefined,
	stroke: new ol.style.Stroke({
		color: [0, 0, 255],
		width: 3
	})
})

const osmLayer = new ol.layer.Tile({
	source: new ol.source.OSM()
});

const railwayLayer = new ol.layer.Tile({
	source: new ol.source.OSM({
		url: "http://tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png",
		crossOrigin: null,
		opaque: false
	})
});

const countryOutlineLayer = new ol.layer.Vector({
	source: new ol.source.Vector({
		format: new ol.format.GeoJSON(),
		url: "/static/map/poland.geojson"
	}),
	style: countryOutlineStyle
})

const stationsPointsLayer = new ol.layer.Vector({
	source: new ol.source.Cluster({
  		source: new ol.source.Vector({
			format: new ol.format.GeoJSON,
			url: "/geo/GetLocations"
		})
	})
})


const homeMap = new ol.Map({
	target: 'map-container',
	layers: [osmLayer, railwayLayer, countryOutlineLayer, stationsPointsLayer],
	controls: [zoomControl],
	view: new ol.View({
		center: ol.proj.fromLonLat([19, 52]),
		zoom: 6,
		constrainResolution: true
	})
});
