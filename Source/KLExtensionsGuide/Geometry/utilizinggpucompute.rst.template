.. _polygonmeshstructure:

Utilizing GPU commpute with Geometries
======================================



Introduction
------------

GPU Compute can now be used to compute Geometry deformations with relative ease. 

The InlineDrawing system has been updated to support rendering of geometries that are already on the GPU.

Objects are not yet supported on the GPU, only simple tupes, structs and arrays can be used in GPU compute kernels.

.. _polygonmeshcomponents:

PolygonMesh
----------------------

The :kl-ref:`PolygonMesh` owns a member called 'topology' of type :kl-ref:`PolygonMeshTopology` that can be moved onto the GPU and passed into GPU compute kernels.

Before a :kl-ref:`PolygonMesh` can be used in a GPU kernel, its topology data must be moved to the GPU. Each 
:kl-ref:`GeometryAttribute' owned by a Geometry must also be individually moved to the GPU before it can be used. 

GPU Compute kernels do not support objects, meaning that it is not possible to pass into a GPU kernel the PolygonMesh, Lines, Points, or any of the various attribute types. Instead, the data contained within these object can be passed into GPU kernels.

Each of the GeometryAttrbiutes owns data that can be passed into GPU Compute kernels. Most attributes have a member called 'values' which is an array of the data type supported by the :kl-ref:`GeometryAttribute`.


.. kl-example:: Moving a polygonMesh to the GPU

require Geometry;

  operator meshDataOnGPU<<<index>>>(io PolygonMeshTopology meshData){
    report(meshData);
  }

  operator entry() {

    PolygonMesh mesh = PolygonMesh();
    Scalar length = 12.0;
    Scalar width = 4.0;
    Integer lengthSections = 3;
    Integer widthSections = 4;

    mesh.addPlane(Xfo(), length, width, lengthSections, widthSections, true, true);

    mesh.convertToGPU();
    meshDataOnGPU<<<1@true>>>(mesh.topology);

    mesh.convertToCPU();
    report(mesh.getDesc(true, true));
  }


Once the data is on the GPU, the same kernels that would normally be used on the CPU can now be run on the GPU.

.. kl-example:: Performing a smooth mesh using the CPU and then again using the GPU

  require Geometry;

  operator noiseOp<<<index>>>(io Vec3 positions[], Scalar height){
    positions[index].y = mathRandomFloat32(54775, index) * height;
  }

  operator smoothMesh<<<index>>>(io PolygonMeshTopology mesh, io Vec3 positions[], Vec3 positionsDoubleBuffer[]) {

    //Pseudo-gaussian: center weight = 0.5, neighbor weights sum = 0.5
    Vec3 position = positionsDoubleBuffer[ index ];

    LocalL16UInt32Array surroundingPoints;
    mesh.getPointSurroundingPoints( index, false, surroundingPoints );
    UInt32 nbNei = surroundingPoints.size();
    if( nbNei ) {
      Vec3 neiSum = Vec3(0,0,0);
      for( UInt32 i = 0; i < nbNei; ++i ) {
        UInt32 neiPt = surroundingPoints.get(i);
        neiSum += positionsDoubleBuffer[neiPt];
      }
      neiSum /= Scalar(nbNei);
      position = ( position + neiSum ) * 0.5;
      mesh.setPointAttribute(index, positions, position );
    }
  }

  operator entry() {

    UInt32 iterations = 40;
    Scalar length = 120.0;
    Scalar width = 40.0;
    Integer lengthSections = 1400;
    Integer widthSections = 900;
    Scalar height = 10.0;

    // first smooth on the CPU.
    {

      PolygonMesh mesh = PolygonMesh();
      mesh.addPlane(Xfo(), length, width, lengthSections, widthSections, true, true);
      Ref<Vec3Attribute> positionsAttr = mesh.getAttributes().getPositions();

      Vec3 positionsDoubleBuffer[];
      positionsDoubleBuffer.resize(positionsAttr.values.size);

      noiseOp<<<positionsAttr.values.size@false>>>(positionsAttr.values, height);
      
      UInt64 start = getCurrentTicks();
      for(UInt32 i=0; i<iterations; i++){
        smoothMesh<<<mesh.pointCount()@false>>>(mesh.topology, positionsDoubleBuffer, positionsAttr.values);

        Vec3 tmp[] = positionsAttr.values;
        positionsAttr.values = positionsDoubleBuffer;
        positionsAttr.values = tmp;
      }
      UInt64 end = getCurrentTicks(); 
      report("pointCount: " + mesh.pointCount() + " CPU Time: " + getSecondsBetweenTicks(start, end));
    }

    // then use the same code to smooth on the GPU.
    {

      PolygonMesh mesh = PolygonMesh();
      mesh.addPlane(Xfo(), length, width, lengthSections, widthSections, true, true);
      Ref<Vec3Attribute> positionsAttr = mesh.getAttributes().getPositions();

      Vec3 positionsDoubleBuffer[];
      positionsDoubleBuffer.resize(positionsAttr.values.size);

      mesh.convertToGPU();
      positionsAttr.convertToGPU();
      positionsDoubleBuffer.convertToGPU();

      noiseOp<<<positionsAttr.values.size@true>>>(positionsAttr.values, height);

      UInt64 start = getCurrentTicks();
      for(UInt32 i=0; i<iterations; i++){
        smoothMesh<<<mesh.pointCount()@true>>>(mesh.topology, positionsDoubleBuffer, positionsAttr.values);

        Vec3 tmp[] = positionsAttr.values;
        positionsAttr.values = positionsDoubleBuffer;
        positionsAttr.values = tmp;
      }
      UInt64 end = getCurrentTicks(); 
      report("pointCount: " + mesh.pointCount() + " GPU Time: " + getSecondsBetweenTicks(start, end));
    }

  }


Setting Attribute Values
........................

Normally when setting attribute values on the CPU, you can use the PolygonMesh helper method 'setPointAttribute'. 
The PolygonMeshTopology structure supports a similar set of methods tht take instead of the attribute object, the values 
of the attribute.

.. kl-example:: Setting Attribute values using setPointAttribute on the PolygonMeshTopology struct.

  require Geometry;

  operator randomizeMesh<<<index>>>(io PolygonMeshTopology mesh, io Vec3 positions[]) {
    Vec3 position = positionsDoubleBuffer[ index ];
    positions[index].y = mathRandomFloat32(54775, index) * height;
    mesh.setPointAttribute(index, positions, position );
  }

  operator entry() {

    PolygonMesh mesh();
    mesh.addPlane(Xfo(), 120.0, 40.0, 1400, 900, true, true);
    Ref<Vec3Attribute> positionsAttr = mesh.getAttributes().getPositions();
    mesh.convertToGPU();
    positionsAttr.convertToGPU();

    randomizeMesh<<<mesh.pointCount()@true>>>(mesh.topology, positionsAttr.values);
  }



Skinning Attribute
..................

The :kl-ref:`SkinningAttribute` has a member struct called 'data' or type :kl-ref:`SkinningAttributeData` that is passed into GPU compute kernels.

.. kl-example:: Using the SkinningAttribute in a GPU compute kernel.

  require Geometry;

  operator skinMeshPositions<<<index>>>(
    io PolygonMeshTopology mesh,
    io Vec3 positions[],
    io SkinningAttributeData skinningAttr,
    Mat44 skinningMatrices[]
  ){
    Vec3 srcPos = positions[index];

    LocalL16UInt32Array indices;
    LocalL16ScalarArray weights;
    skinningAttr.getPairs(index, indices, weights);
    Scalar weighSum = 0.0;
    Vec3 position(0,0,0);
    for( UInt32 i = 0; i < indices.size(); ++i ) {
      Scalar boneWeight = weights.get(i);
      if( boneWeight == 0.0 )
        break;
      UInt32 boneId = indices.get(i);
      position += (skinningMatrices[boneId] * srcPos) * boneWeight;
      weighSum += boneWeight;
    }

    mesh.setPointAttribute( index, positions, position );
  }


  operator entry() {

    PolygonMesh mesh = PolygonMesh();
    mesh.addCuboid(Xfo(), 2.0, 2.0, 2.0);
    Ref<Vec3Attribute> positionsAttribute = mesh.getAttributes().positionsAttribute;

    Ref<SkinningAttribute> skinningAttribute = mesh.getOrCreateAttribute("skinningData", SkinningAttribute);

    // Generate a random set of id/weight pairs per vertex in the mesh. 
    UInt32 numJoints = 5;
    UInt32 maxNumJointerPerVertex = 3;
    UInt32 seed = 8516;
    UInt32 offset = 0;
    for(Integer i=0; i<skinningAttribute.size; i++){
      UInt16 numItems = mathRandomFloat32(seed, ++offset) * maxNumJointerPerVertex;
      skinningAttribute.setPairCount( i, numItems );
      for(Integer j=0; j<numItems; j++){
        UInt16 index = mathRandomFloat32(seed, ++offset) * numJoints;
        Float32 weight = mathRandomFloat32(seed, ++offset);
        skinningAttribute.setPair( i, j, index, weight );
      }
    }
    Mat44 skinningMatrices[];
    skinningMatrices.resize(numJoints);

    mesh.convertToGPU();
    positionsAttribute.convertToGPU();
    skinningAttribute.convertToGPU();
    skinningMatrices.convertToGPU();

    skinMeshPositions<<<mesh.pointCount()@true>>>(
      mesh.topology,
      positionsAttribute.values,
      skinningAttribute.data,
      skinningMatrices
    );

    positionsAttribute.convertToCPU();
    skinningAttribute.convertToCPU();
    mesh.convertToCPU();
    report(mesh.getDesc(true, true));
  }



Current limitations
------------------

The GPU compute infrustructure currently has the following limitations:

 - Attribute sizes cannot change during GPU compute operations. The only supported methods on the PolygonMeshTopology modify values, but do not modify attribute sharing information.
 - Objects are not yet supported on the GPU, only simple types, structs and arrays can be used in GPU compute kernels.