<template>
  <q-page class="column">
    <q-toolbar class="toolbar q-py-sm text-white row justify-between">
      <div>
        <q-btn
          flat
          round
          dense
          icon="fas fa-mouse-pointer"
          @click="cursorMode"
        />
        <q-btn flat round dense icon="fas fa-pencil-alt" @click="drawingMode" />
        <q-btn flat round dense icon="title" @click="addText" />
        <q-btn flat round dense icon="far fa-square" @click="addSquare" />
        <q-btn flat round dense icon="far fa-circle" @click="addCircle" />
        <q-btn flat round dense icon="details" @click="addTriangle" />
        <q-btn flat round dense icon="horizontal_rule" @click="addLine" />
        <q-btn flat round dense icon="far fa-image" @click="chooseImage" />
      </div>
      <div>
        <q-btn flat round dense icon="fas fa-trash-alt" @click="deteleObject" />
        <q-btn
          flat
          color="red-6"
          label="Clear Canvas"
          class="no-border-radius"
          @click="clearCanvas"
        />
      </div>

      <input
        ref="imageInput"
        type="file"
        accept="image/*"
        v-on:change="addImage"
        style="display: none"
      />
    </q-toolbar>
    <div class="row justify-between editDiv">
      <div class="col-2 column items-center">
        <q-list bordered style="width: 100%">
          <q-item-label
            v-if="cursor"
            header
            class="q-pa-xs editTitle text-subtitle1"
            >Edit Object</q-item-label
          >

          <div v-if="cursor" class="row items-center justify-around">
            <q-btn
              flat
              size="md"
              class="q-pa-xs"
              icon="vertical_align_top"
              @click="alignVerticalTop"
            />
            <q-btn
              flat
              size="md"
              class="q-pa-xs"
              icon="vertical_align_center"
              @click="alignVerticalCenter"
            />
            <q-btn
              flat
              size="md"
              class="q-pa-xs"
              icon="vertical_align_bottom"
              @click="alignVerticalBottom"
            />
            <q-btn
              flat
              size="md"
              class="q-pa-xs"
              icon="align_horizontal_left"
              @click="alignHorizontalLeft"
            />
            <q-btn
              flat
              size="md"
              class="q-pa-xs"
              icon="align_horizontal_center"
              @click="aligHorizontalCenter"
            />
            <q-btn
              flat
              size="md"
              class="q-pa-xs"
              icon="align_horizontal_right"
              @click="alignHorizontalRight"
            />
          </div>
          <q-separator v-if="cursor" class="q-my-sm" />
          <q-item v-if="cursor" class="column q-pa-none">
            <q-item-label header class="editTitle q-pt-none">Fill</q-item-label>
            <q-item-section>
              <q-input
                class="q-mx-xl"
                v-model="activeObjectColor"
                dense
                color="accent"
                :disable="isActiveObjectTypeGroup"
              >
                <template v-slot:append>
                  <q-icon
                    name="fas fa-square"
                    :style="{ color: activeObjectColor }"
                    class="cursor-pointer"
                  >
                    <q-popup-proxy
                      transition-show="scale"
                      transition-hide="scale"
                    >
                      <q-color v-model="activeObjectColor" />
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>

              <q-separator class="q-mx-none q-my-md" />
              <q-item-label header class="editTitle q-pt-none"
                >Stroke</q-item-label
              >
              <div class="row justify-around">
                <q-input
                  class="col-7"
                  v-model="activeObjectStrokeColor"
                  dense
                  color="accent"
                  :disable="isActiveObjectTypeGroup"
                >
                  <template v-slot:append>
                    <q-icon
                      name="fas fa-square"
                      :style="{ color: activeObjectStrokeColor }"
                      class="cursor-pointer"
                    >
                      <q-popup-proxy
                        transition-show="scale"
                        transition-hide="scale"
                      >
                        <q-color v-model="activeObjectStrokeColor" />
                      </q-popup-proxy>
                    </q-icon>
                  </template>
                </q-input>

                <q-input
                  v-model.number="activeObjectStrokeWidth"
                  type="number"
                  class="col-3"
                  dense
                  color="accent"
                  min="0"
                  :disable="isActiveObjectTypeGroup"
                />
              </div>
              <q-separator class="q-mx-none q-my-md" />
              <q-item-label header class="editTitle q-pt-none"
                >Order</q-item-label
              >
              <div class="column">
                <div class="row justify-around q-mb-sm">
                  <q-btn
                    outline
                    rounded
                    dense
                    no-caps
                    size="md"
                    text-color="black"
                    class="q-px-md"
                    label="send backward"
                    @click="sendBackward"
                  />
                  <q-btn
                    outline
                    rounded
                    dense
                    no-caps
                    size="md"
                    text-color="black"
                    class="q-px-md"
                    label="send to back"
                    @click="sendToBack"
                  />
                </div>
                <div class="row justify-around">
                  <q-btn
                    outline
                    rounded
                    dense
                    no-caps
                    size="md"
                    text-color="black"
                    class="q-px-md"
                    label="bring forward"
                    @click="bringForward"
                  />
                  <q-btn
                    outline
                    rounded
                    dense
                    no-caps
                    size="md"
                    text-color="black"
                    class="q-px-md"
                    label="bring to front"
                    @click="bringToFront"
                  />
                </div>
              </div>
              <q-separator class="q-mx-none q-my-md" />
              <q-item-label header class="editTitle q-pt-none"
                >Group</q-item-label
              >
              <div class="row justify-around q-mb-sm">
                <q-btn
                  outline
                  rounded
                  dense
                  no-caps
                  size="md"
                  text-color="black"
                  class="q-px-md"
                  label="Group"
                  @click="group"
                />
                <q-btn
                  outline
                  rounded
                  dense
                  no-caps
                  size="md"
                  text-color="black"
                  class="q-px-md"
                  label="Ungroup"
                  @click="ungroup"
                />
              </div>
            </q-item-section>
          </q-item>
          <q-separator
            v-if="isActiveObjectTypeText && cursor"
            class="q-my-sm"
            size="2px"
          />
          <q-item-label
            key="label"
            v-if="isActiveObjectTypeText && cursor"
            header
            class="q-pa-xs editTitle text-subtitle1"
            >Edit Text</q-item-label
          >

          <q-item
            key="item"
            v-if="isActiveObjectTypeText && cursor"
            class="q-pa-none"
          >
            <q-item-section>
              <div>
                <q-select
                  color="accent"
                  class="q-mx-md"
                  v-model="textFont"
                  :options="textFontOptions"
                  dense
                  options-dense
                  fill-input
                  :popup-content-style="{ height: '150px' }"
                >
                </q-select>
              </div>
              <div class="row justify-between q-px-md q-py-sm">
                <div class="row items-center">
                  <q-btn
                    size="sm"
                    flat
                    round
                    dense
                    class="no-border-radius"
                    icon="remove"
                    @click="textSize -= 1"
                  />
                  <q-select
                    color="accent"
                    v-model="textSize"
                    :options="textSizeOptions"
                    dense
                    options-dense
                    fill-input
                    :popup-content-style="{ height: '250px' }"
                  >
                  </q-select>
                  <q-btn
                    size="sm"
                    flat
                    round
                    dense
                    class="no-border-radius"
                    icon="add"
                    @click="textSize += 1"
                  />
                </div>
                <div>
                  <q-btn
                    size="md"
                    padding="sm"
                    flat
                    icon="format_bold"
                    @click="toggleBold"
                  />
                  <q-btn
                    size="md"
                    padding="sm"
                    flat
                    icon="format_italic"
                    @click="toggleItalic"
                  />
                  <q-btn
                    size="md"
                    padding="sm"
                    flat
                    icon="format_underline"
                    @click="toggleUnderline"
                  />
                </div>
              </div>
              <div class="row justify-between q-px-md">
                <div class="row items-center q-py-xs">
                  <q-btn size="md" padding="sm" flat icon="format_line_spacing">
                    <q-menu anchor="bottom middle" self="top middle">
                      <div class="q-py-xs q-px-lg" style="width: 200px">
                        <q-slider
                          v-model="textLineHeight"
                          :min="1"
                          :max="4"
                          :step="0.01"
                          color="secondary"
                        />
                      </div>
                    </q-menu>
                  </q-btn>

                  <q-btn size="md" padding="sm" flat icon="settings_ethernet">
                    <q-menu anchor="bottom middle" self="top middle">
                      <div class="q-py-xs q-px-lg" style="width: 200px">
                        <q-slider
                          v-model="textCharSpacing"
                          :min="0"
                          :max="1500"
                          color="secondary"
                        />
                      </div>
                    </q-menu>
                  </q-btn>
                </div>
                <div class="row items-center">
                  <q-btn
                    size="md"
                    padding="sm"
                    flat
                    icon="format_align_left"
                    @click="textAlignLeft"
                  />
                  <q-btn
                    size="md"
                    padding="sm"
                    flat
                    icon="format_align_center"
                    @click="textAlignCenter"
                  />
                  <q-btn
                    size="md"
                    padding="sm"
                    flat
                    icon="format_align_right"
                    @click="textAlignRight"
                  />
                  <q-btn
                    size="md"
                    padding="sm"
                    flat
                    icon="format_align_justify"
                    @click="textAlignJustify"
                  />
                </div>
              </div>
            </q-item-section>
          </q-item>
          <q-item-label
            v-if="!cursor"
            header
            class="q-pa-xs editTitle text-subtitle1"
            >Edit Freehand</q-item-label
          >
          <q-item v-if="!cursor" class="q-py-none">
            <q-item-section>
              <div class="row justify-around q-mb-md">
              <q-input  v-model="penToolColor" dense color="accent" class="col-7">
                <template v-slot:append>
                  <q-icon
                    name="fas fa-square"
                    :style="{ color: penToolColor }"
                    class="cursor-pointer"
                  >
                    <q-popup-proxy
                      transition-show="scale"
                      transition-hide="scale"
                    >
                      <q-color v-model="penToolColor" />
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
              <q-input
                v-model.number="penToolWidth"
                type="number"
                class="col-3"
      
                dense
                color="accent"
              />
              </div>
            </q-item-section>
          </q-item>
        </q-list>
      </div>
      <div class="col-8 canvas-container row items-center justify-center">
        <q-scroll-area class="fit">
          <div class="row justify-center">
            <canvas
              id="canvas"
              width="496"
              height="701.6"
              tabindex="0"
              class="canvas"
            ></canvas>
          </div>
        </q-scroll-area>
      </div>
      <div class="col-2 column items-center justify-between borderRightDiv">
        <div class="column">
          <q-btn
            no-caps
            flat
            color="black"
            icon="fas fa-eye"
            class="no-border-radius buttonAspect q-pa-md q-my-md"
            text-color="black"
            label="PREVIEW"
            @click="drawOnPreview"
          />

          <canvas
            ref="previewCanvas"
            width="200"
            height="282.84"
            tabindex="0"
            class="canvas"
          ></canvas>
        </div>
        <div class="column">
          <q-btn
            no-caps
            flat
            color="black"
            class="no-border-radius buttonAspect q-px-xl q-py-md"
            text-color="black"
            icon="file_download"
            label="DOWNLOAD DESIGN"
            @click="downloadDesign"
          />

          <q-btn
            label="FINISH"
            no-caps
            flat
            color="black"
            class="no-border-radius buttonFinish q-px-xl q-py-md"
            text-color="black"
          />
        </div>
        <q-btn
          color="white"
          text-color="black"
          label="Buton de teste"
          @click="functieDeTest"
        />
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
import { fabric } from "fabric";
import { defineComponent, onMounted, ref, watch } from "vue";

export default defineComponent({
  name: "DesignStep3",

  setup() {
    window.addEventListener("keydown", (e) => {
      if (e.key === "Delete") {
        deteleObject();
      }
    });
    let ctx: CanvasRenderingContext2D | null;
    const previewCanvas = ref<HTMLCanvasElement>();
    let canvas: any;
    let imageInput = ref<HTMLInputElement>();
    let cursor = ref(true);
    let isActiveObjectTypeText = ref(false);
    let isActiveObjectTypeGroup = ref(false);
    let penToolWidth = ref(5);
    let penToolColor = ref("#000000");
    let activeObjectColor = ref("#000000");
    let activeObjectStrokeColor = ref("#000000");
    let activeObjectStrokeWidth = ref(1);
    let textSize = ref(12);
    let textSizeOptions = [
      6, 8, 10, 12, 14, 16, 18, 21, 24, 28, 32, 36, 42, 48, 56, 64, 72, 80, 88,
      96, 104,
    ];
    let textFont = ref("Arial");
    let textFontOptions = [
      "Arial",
      "Calibri",
      "Courier",
      "Impact",
      "Verdana",
      "Times New Roman",
      "Comic Sans MS",
    ];
    let textLineHeight = ref(1);
    let textCharSpacing = ref(0);

    let functieDeTest = function () {
      console.log("ai apelat functia de test");
      console.log(canvas.getActiveObject().get("type"));
    };

    let cursorMode = function () {
      canvas.isDrawingMode = false;
      cursor.value = true;
    };
    let drawingMode = function () {
      canvas.isDrawingMode = true;
      updatePenTool();
      cursor.value = false;
    };
    let updatePenTool = function () {
      canvas.freeDrawingBrush.width = penToolWidth.value;
      canvas.freeDrawingBrush.color = penToolColor.value;
    };
    watch(penToolWidth, updatePenTool);
    watch(penToolColor, updatePenTool);

    let updateActiveObject = function () {
      if (canvas.getActiveObject()) {
        canvas
          .getActiveObject()
          .set("fill", activeObjectColor.value)
          .set("stroke", activeObjectStrokeColor.value)
          .set("strokeWidth", activeObjectStrokeWidth.value)
          .set("strokeUniform", true);
      }
      canvas.renderAll();
    };
    watch(activeObjectColor, updateActiveObject);
    watch(activeObjectStrokeColor, updateActiveObject);
    watch(activeObjectStrokeWidth, updateActiveObject);

    let alignVerticalTop = function () {
      if (canvas.getActiveObject()) {
        canvas.getActiveObject().set("top", 0);
        canvas.renderAll();
      }
    };
    let alignVerticalCenter = function () {
      if (canvas.getActiveObject()) {
        canvas
          .getActiveObject()
          .set(
            "top",
            canvas.height / 2 -
              (canvas.getActiveObject().get("height") / 2) *
                canvas.getActiveObject().get("scaleX") -
              canvas.getActiveObject().get("strokeWidth") / 2
          );

        canvas.renderAll();
      }
    };
    let alignVerticalBottom = function () {
      if (canvas.getActiveObject()) {
        canvas
          .getActiveObject()
          .set(
            "top",
            canvas.height -
              canvas.getActiveObject().get("height") *
                canvas.getActiveObject().get("scaleX") -
              canvas.getActiveObject().get("strokeWidth")
          );

        canvas.renderAll();
      }
    };
    let alignHorizontalLeft = function () {
      if (canvas.getActiveObject()) {
        canvas.getActiveObject().set("left", 0);
        canvas.renderAll();
      }
    };
    let aligHorizontalCenter = function () {
      if (canvas.getActiveObject()) {
        canvas
          .getActiveObject()
          .set(
            "left",
            canvas.width / 2 -
              (canvas.getActiveObject().get("width") / 2) *
                canvas.getActiveObject().get("scaleY") -
              canvas.getActiveObject().get("strokeWidth") / 2
          );

        canvas.renderAll();
      }
    };
    let alignHorizontalRight = function () {
      if (canvas.getActiveObject()) {
        canvas
          .getActiveObject()
          .set(
            "left",
            canvas.width -
              canvas.getActiveObject().get("width") *
                canvas.getActiveObject().get("scaleY") -
              canvas.getActiveObject().get("strokeWidth")
          );
        canvas.renderAll();
      }
    };
    let sendToBack = function () {
      let activeObject = canvas.getActiveObject();
      if (activeObject) {
        canvas.sendToBack(activeObject);
      }
    };
    let sendBackward = function () {
      let activeObject = canvas.getActiveObject();
      if (activeObject) {
        canvas.sendBackwards(activeObject);
      }
    };
    let bringToFront = function () {
      let activeObject = canvas.getActiveObject();
      if (activeObject) {
        canvas.bringToFront(activeObject);
      }
    };
    let bringForward = function () {
      let activeObject = canvas.getActiveObject();
      if (activeObject) {
        canvas.bringForward(activeObject);
      }
    };
    let group = function () {
      if (!canvas.getActiveObject()) {
        return;
      }
      if (canvas.getActiveObject().type !== "activeSelection") {
        return;
      }
      canvas.getActiveObject().toGroup();
      canvas.requestRenderAll();
    };
    let ungroup = function () {
      if (!canvas.getActiveObject()) {
        return;
      }
      if (canvas.getActiveObject().type !== "group") {
        return;
      }
      canvas.getActiveObject().toActiveSelection();
      canvas.requestRenderAll();
    };
    //TEXT
    let updateFontSize = function () {
      canvas
        .getActiveObject()
        .set(
          "fontSize",
          textSize.value / canvas.getActiveObject().get("scaleX")
        );
      canvas.renderAll();
    };
    watch(textSize, updateFontSize);
    let updateFont = function () {
      canvas.getActiveObject().set("fontFamily", textFont.value.toLowerCase());
      canvas.renderAll();
    };
    watch(textFont, updateFont);
    let toggleBold = function () {
      canvas
        .getActiveObject()
        .set(
          "fontWeight",
          canvas.getActiveObject().get("fontWeight") === "bold" ? "" : "bold"
        );
      canvas.renderAll();
    };
    let toggleItalic = function () {
      canvas
        .getActiveObject()
        .set(
          "fontStyle",
          canvas.getActiveObject().get("fontStyle") === "italic" ? "" : "italic"
        );
      canvas.renderAll();
    };
    let toggleUnderline = function () {
      let val = canvas.getActiveObject().get("underline");
      canvas.getActiveObject().set("textDecoration", val);
      canvas
        .getActiveObject()
        .set("underline", !canvas.getActiveObject().get("underline"));
      canvas.renderAll();
    };
    let updateTextLineHeight = function () {
      canvas.getActiveObject().set("lineHeight", textLineHeight.value);
      canvas.renderAll();
    };
    watch(textLineHeight, updateTextLineHeight);
    let updatetextCharSpacing = function () {
      canvas.getActiveObject().set("charSpacing", textCharSpacing.value);
      canvas.renderAll();
    };
    watch(textCharSpacing, updatetextCharSpacing);
    let textAlignLeft = function () {
      canvas.getActiveObject().set("textAlign", "left");
      canvas.renderAll();
    };
    let textAlignCenter = function () {
      canvas.getActiveObject().set("textAlign", "center");
      canvas.renderAll();
    };
    let textAlignRight = function () {
      canvas.getActiveObject().set("textAlign", "right");
      canvas.renderAll();
    };
    let textAlignJustify = function () {
      canvas.getActiveObject().set("textAlign", "justify");
      canvas.renderAll();
    };

    //DRAWING FUNCTIONS
    let addText = function () {
      let textSample = new fabric.Textbox("Add Your Text Here", {
        top: canvas.height / 2 - 10,
        left: canvas.width / 2 - 90,
        fontFamily: "helvetica",
        angle: 0,
        scaleX: 0.5,
        scaleY: 0.5,
        fontWeight: "",
        originX: "left",
        width: 360,
        hasRotatingPoint: true,
        centerTransform: true,
      });

      canvas.add(textSample);
    };
    let addSquare = function () {
      let rect = new fabric.Rect({
        top: canvas.height / 2 - 50,
        left: canvas.width / 2 - 50,
        width: 100,
        height: 100,
        fill: "",
        stroke: "#000000",
      });
      canvas.add(rect);
    };
    let addCircle = function () {
      let circle = new fabric.Circle({
        left: canvas.width / 2 - 50,
        top: canvas.height / 2 - 50,
        radius: 50,
        fill: "",
        stroke: "#000000",
      });
      canvas.add(circle);
    };
    let addTriangle = function () {
      let triangle = new fabric.Triangle({
        left: canvas.width / 2 - 50,
        top: canvas.height / 2 - 50,
        fill: "",
        stroke: "#000000",
        width: 100,
        height: 100,
      });
      canvas.add(triangle);
    };
    let addLine = function () {
      let line = new fabric.Line([50, 100, 200, 200], {
        left: canvas.width / 2 - 75,
        top: canvas.height / 2 - 50,
        fill: "",
        stroke: "#000000",
      });
      canvas.add(line);
    };
    let addImage = function () {
      console.log("fuck");
      let url;
      if (imageInput.value?.files && imageInput.value?.files[0]) {
        url = URL.createObjectURL(imageInput.value?.files[0]);
      }
      fabric.Image.fromURL(url, function (image: any) {
        image
          .set({
            left: 0,
            top: 0,
          })
          .scale(0.2)
          .setCoords();

        canvas.add(image);
      });
      canvas.renderAll();
    };
    let deteleObject = function () {
      var activeObjects = canvas.getActiveObjects();
      canvas.discardActiveObject();
      if (activeObjects.length) {
        canvas.remove.apply(canvas, activeObjects);
      }
    };
    let clearCanvas = function () {
      canvas.clear();
    };
    let downloadDesign = function () {
      let data = canvas.toDataURL({ multiplier: 5, format: "png" });
      fetch(data)
        .then((response) => response.blob())
        .then((blob) => {
          const link = document.createElement("a");
          link.href = URL.createObjectURL(blob);
          link.download = "ideeaprintDesigns";
          link.click();
          URL.revokeObjectURL(link.href);
        });
    };
    let chooseImage = function () {
      imageInput.value?.click();
    };
    let drawOnPreview = function () {
      //  console.log(data);
      console.log(ctx);
      ctx?.clearRect(0, 0, 200, 282.84);
      var image = new Image();
      image.onload = function () {
        ctx?.drawImage(image, 0, 0, 200, 282.84);
      };
      image.src = require("../assets/white-tshirt-background.png");
      let data = canvas.toDataURL({ multiplier: 3, format: "png" });
      var img = new Image();
      img.onload = function () {
        let fct = function () {
          ctx?.drawImage(img, 63, 90.272, 80, 113.136);
        }; // Or at whatever offset you like
        setTimeout(fct, 200);
      };
      img.src = data;
    };
    onMounted(() => {
      //de aici incepe fabric
      canvas = new fabric.Canvas("canvas");
      canvas.on("mouse:down", function (options: any) {
        if (options.target) {
          console.log("an object was clicked! ");
          activeObjectColor.value = options.target.get("fill");
          activeObjectStrokeColor.value = options.target.get("stroke");
          activeObjectStrokeWidth.value = options.target.get("strokeWidth");
          if (options.target.get("type") === "textbox") {
            isActiveObjectTypeText.value = true;
            textSize.value =
              options.target.get("fontSize") * options.target.get("scaleX");
            options.target.on("event:scale", function () {
              console.log("scale");
            });
          } else {
            isActiveObjectTypeText.value = false;
          }
          if (options.target.get("type") === "group") {
            isActiveObjectTypeGroup.value = true;
          } else {
            isActiveObjectTypeGroup.value = false;
          }
        }
      });

      canvas.on("mouse:move", function () {
        let updateTextFontSizeOnMouseMove = function () {
          if (canvas.getActiveObject()?.get("type") === "textbox") {
            textSize.value =
              canvas.getActiveObject()?.get("fontSize") *
              canvas.getActiveObject()?.get("scaleX");
          }
        };
        setTimeout(updateTextFontSizeOnMouseMove, 500);
      });
      if (previewCanvas.value?.getContext("2d")) {
        ctx = previewCanvas.value?.getContext("2d");
        ctx?.clearRect(0, 0, 200, 282.84);
        var image = new Image();
        image.onload = function () {
          ctx?.drawImage(image, 0, 0, 200, 282.84);
        };
        image.src = require("../assets/white-tshirt-background.png");
      }
    });

    return {
      previewCanvas,
      functieDeTest,
      cursorMode,
      drawingMode,
      toggleBold,
      toggleItalic,
      toggleUnderline,
      textAlignLeft,
      textAlignCenter,
      textAlignRight,
      textAlignJustify,
      addText,
      addSquare,
      addCircle,
      addTriangle,
      addLine,
      addImage,
      deteleObject,
      clearCanvas,
      downloadDesign,
      chooseImage,
      drawOnPreview,
      imageInput,
      textSize,
      textSizeOptions,
      textFont,
      textFontOptions,
      textLineHeight,
      textCharSpacing,
      penToolWidth,
      penToolColor,
      cursor,
      updatePenTool,
      activeObjectColor,
      activeObjectStrokeColor,
      activeObjectStrokeWidth,
      alignVerticalTop,
      alignVerticalCenter,
      alignVerticalBottom,
      alignHorizontalLeft,
      aligHorizontalCenter,
      alignHorizontalRight,
      sendToBack,
      sendBackward,
      bringToFront,
      bringForward,
      group,
      ungroup,
      isActiveObjectTypeText,
      isActiveObjectTypeGroup,
    };
  },
});
</script>

<style lang="scss" scoped>
.toolbar {
  background-color: #3d3d3d;
}
.canvas-container {
  background-color: #f3f3f3;
}
.canvas {
  border: 6px solid;
  background: white;
}
.buttonAspect {
  border-style: solid;
  border-width: 4px;
  background-color: $accent;
}
.buttonFinish {
  border-style: solid;
  border-width: 4px;
  background-color: $info;
}
.borderRightDiv {
  border-left: 4px solid;
}
.buttonSendCanvas {
  border-style: solid;
  border-width: 3px;
  background-color: white;
}
.editTitle {
  color: black;
  font-family: raleway;
}
.editDiv {
  font-family: raleway;
}
</style>