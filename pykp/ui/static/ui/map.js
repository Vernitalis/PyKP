import { createTooltip } from "./components.js";

const zoomButtonsClasses = "btn-sm btn-ghost join-item";

const zoomControl = new ol.control.Zoom({
	className: "absolute bg-base-100 bottom-4 left-4 join join-vertical shadow-xl",
	zoomInClassName: zoomButtonsClasses,
	zoomOutClassName: zoomButtonsClasses
});

const countryOutlineStyle = new ol.style.Style({
	fill: undefined,
	stroke: new ol.style.Stroke({
		color: [0, 0, 255],
		width: 3
	})
});

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
		url: "/static/ui/poland.geojson"
	}),
	style: countryOutlineStyle
});

const stationsPointsLayer = new ol.layer.Vector({
	source: new ol.source.Cluster({
		source: new ol.source.Vector({
			format: new ol.format.GeoJSON,
			url: "/geo/GetLocations"
		})
	})
});

const tooltip = createTooltip("");
tooltip.id = "map-tooltip";

const tooltipOverlay = new ol.Overlay({
	element: tooltip,
	positioning: 'bottom-center',
	stopEvent: false
});

export class PykpMap extends ol.Map {
	constructor(target) {
		super({
			target: target,
			layers: [osmLayer, railwayLayer, countryOutlineLayer, stationsPointsLayer],
			controls: [zoomControl],
			view: new ol.View({
				center: ol.proj.fromLonLat([19, 52]),
				zoom: 6,
				constrainResolution: true
			}),
			overlays: [ tooltipOverlay ]
		});

		this.on("click", (evt) => {
			const clusterFeature = this.forEachFeatureAtPixel(evt.pixel, (feature, layer) => {
				if (layer == stationsPointsLayer) {
					return feature;
				}
			});

			if (!clusterFeature) {
				tooltip.close();
				return;
			}
			const pointFeatures = clusterFeature.get("features");
			const featuresNames = pointFeatures.map((feature) => feature.get("name"));

			let tip;
			if (featuresNames.length == 1) {
				tip = featuresNames[0];
			}
			else if (featuresNames.length > 1 && featuresNames.length < 5) {
				tip = `${featuresNames.length} stacje`;
			}
			else {
				tip = `${featuresNames.length} stacji`;
			}

			tooltipOverlay.setPosition(clusterFeature.getGeometry().getCoordinates());
			tooltip.setDataTip(tip);
			tooltip.open()
		});

		this.on("movestart", (evt) => tooltip.close());
	}
}
