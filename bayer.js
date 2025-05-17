function bayerDither(g){
  g.loadPixels();
  const M=[0,8,2,10,12,4,14,6,3,11,1,9,15,7,13,5];
  for(let y=0;y<g.height;y++){
    for(let x=0;x<g.width;x++){
      const idx=4*(y*g.width+x);
      for(let c=0;c<3;c++){
        const old=g.pixels[idx+c];
        const thresh=M[(y&3)*4+(x&3)]*16;
        g.pixels[idx+c]=old<thresh?0:255;
      }
    }
  }
  g.updatePixels();
}
