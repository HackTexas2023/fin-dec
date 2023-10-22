jQuery(document).ready(function() {
  var debug = document.get.debug === '1';
  function duplicateCanvas(canvas, width, height) {
    var tempCanvas = document.createElement('canvas');
    var tempContext = tempCanvas.getContext('2d');

    tempCanvas.width = width;
    tempCanvas.height = height;
    tempContext.drawImage(canvas, 0, 0);
    return tempCanvas;
  }

  function updateWrapperWidth(el, delay, pagebreakCheck, forceReinitialize, noCallReset) {
    if (pagebreakCheck === undefined) {
      pagebreakCheck = false;
    }

    if (forceReinitialize === undefined) {
      forceReinitialize = false;
    }

    var qid = el.readAttribute('data-id');
    var pad = jQuery(el);

    setTimeout(function() {
      var newWrapperWidth = jQuery('#signature_pad_' + qid).width();
      var newWrapperHeight = jQuery('#signature_pad_' + qid).height();
      var signatureClickPoint = 2; // it is necessary for the signature to start from the clicked point in the signature field
      if (newWrapperWidth > 0) {
        var newwidth = newWrapperWidth + 'px';
        var newHeight = newWrapperHeight + 'px';
        // if wrapper width is not higher than newwidth 
        // and page break is used in mobile
        // set newwidth
        if(pagebreakCheck && el.select('canvas.jSignature').first().style.width > newwidth ){
          newwidth = el.select('canvas.jSignature').first().style.width;
        }
        el.setStyle({
          'width': newwidth
        })
          .select('canvas.jSignature').first()
          .setStyle({
            'width': newwidth
          })
          .writeAttribute('width', newWrapperWidth - signatureClickPoint)
        if(!pagebreakCheck){
          var duplicate = duplicateCanvas(el.select('canvas.jSignature').first(), newWrapperWidth, newWrapperHeight);
          el.select('canvas.jSignature').first()
            .writeAttribute('width', newwidth)
            .writeAttribute('height', newHeight)
            .getContext('2d')
            .drawImage(duplicate, 0, 0);
        }else if(forceReinitialize) {
          el.select('canvas.jSignature').first()
              .writeAttribute('width', newWrapperWidth)
              .writeAttribute('height', newWrapperHeight);
        }
        // calling reset triggers validateAll method, we want to avoid this in this case
        // therefore we added noCallReset in sigresize
        if (!noCallReset && (!pagebreakCheck && JotForm.clearFieldOnHide == 'enable')) {
          // use jquery to reset jSignature
          pad.jSignature('reset');
        }

        debug && console.log('Pad on:sigresize event', qid, pad, newwidth);
      }  
    }, delay ? 100 : 0);
  }

  jQuery('.pad').each(function(idx, el) {
    var pad = jQuery(el);
    var qid = pad.data('id');
    var pwidth = pad.data('width');
    var pheight = pad.data('height');
    var signatureLine = pad.data('signature-line') == '1';
    var isJotFormNext = JotForm.isJotFormNext || /jotformNext=1/.test(window.location.href);

    // if main wrapper size is not zero use it
    // we maybe on the mobile version of the form
    var wrapperEl = jQuery('#signature_pad_' + qid);
    var wrapperWidth = wrapperEl.width();
    if (JotForm.isVisible(wrapperEl[0]) && wrapperWidth > 0) {
      pwidth = wrapperWidth;
      debug && console.log('Wrapper is visible and has a width', wrapperEl, pwidth);
    }
    // set widths to pad and signature canvas
    pad.width(pwidth).height(pheight);
    pad.jSignature({
      width: isJotFormNext ? pwidth + 40 : pwidth,
      height: pheight,
      signatureLine: signatureLine
    });

    // debug signature pad
    debug && console.log('Pad info', qid, pad, pwidth, pheight);

    // bind changes - emits 'change' event immediately after a stroke
    pad.bind('change', function() {
      var focusedElement = document.querySelector(':focus');
      if (focusedElement) {
        focusedElement.blur();
      }
      var thispad = jQuery(this);
      var qid = thispad.attr('data-id');
      if (thispad && typeof thispad.jSignature !== 'undefined' && thispad.jSignature('getData', 'base30')[1].length > 0) {
        var sigdata = thispad.jSignature('getData');
        jQuery('#input_' + qid).val(sigdata);
        JotForm.triggerWidgetCondition(qid);
      }
    });

    // a prototype event that will resize canvas onresize
    el.observe('on:sigresize', function(event) {
      updateWrapperWidth(el, 0, undefined, undefined, true);
    });
    // update wrapped width when orientation changes on mobile devices
    jQuery(window).bind('orientationchange', function() {
      updateWrapperWidth(el, true);
    });
    //update wrapped width onyl not visible field when click the next button for mobile devices
    window.addEventListener('message', function(event) {
      // We should remove messages coming from jotform.js
      try {
        if (event.data) {
          var eventData = JSON.parse(event.data);
          if (typeof eventData === typeof {} && typeof eventData.messageType === 'string') {
            var messageType = eventData.messageType;
            switch (messageType) {
              case 'buttonClick':
                var wrapperEl = jQuery('#signature_pad_' + qid);
                var wrapperWidth = wrapperEl[0].select('canvas.jSignature').first().width;
                if (!(wrapperWidth > 0)) {
                  updateWrapperWidth(el, true, true, true);
                }
                break;
            }
          }
        }
      } catch (error) {
        console.log('Error at signature listener:', error);
      }
    });
    jQuery('.form-pagebreak-next').bind('click keypress', function(e) {
      if (e.type === 'click' || e.keyCode === 13) {
        var wrapperEl = jQuery('#signature_pad_' + qid);
        if (!JotForm.isVisible(wrapperEl[0])){
          // update wrapped but add additional check 
          updateWrapperWidth(el,true,true);
        }
      }
    });
  });

  jQuery('.clear-pad').bind('click keypress', function(e) {
    if (e.type === 'click' || e.keyCode === 13) {
      var pad = jQuery(this).parent().find('.pad');

      if (!pad.jSignature('getSettings').readOnly) {
        pad.jSignature('reset');

        // clear input field as well
        var qid = pad.attr('data-id');
        jQuery('#input_' + qid).val('');
        JotForm.triggerWidgetCondition(qid);
      }
    }
  });

  jQuery('.jotform-form').submit(function(e) {
    jQuery('.pad').each(function(idx, el) {
      var pad = jQuery(el);
      if (!pad.hasClass('edit-signature') && pad.jSignature('getData', 'base30')[1].length > 0) {
        var id = pad.attr('data-id');
        jQuery('#input_' + id).val(pad.jSignature('getData'));
      }
    });
  });

  //@diki
  //edit mode
  if (JotForm.isEditMode() || typeof document.get.session !== 'undefined' || (window.JFForm && window.JFForm.draftID) || document.location.href.match(/\/edit\//) || /offline_forms=true/.test(window.location.href)) {
    jQuery('.jotform-form').on('click keypress', '.edit-signature-pad', function(e) {
      if (e.type === 'click' || e.keyCode === 13) {
        // get pad and the pad id
        var sigId = jQuery(this).attr('data-id');
        var pad = jQuery('.pad#sig_pad_' + sigId);

        // if there's a sig image and want to clear it
        if (jQuery('img.signature-image-' + sigId).length > 0) {
          if (!pad.jSignature('getSettings').readOnly) {
            // show the pad and hide flag class
            pad.removeClass('edit-signature').show();

            // remove value from the input
            jQuery('#input_' + sigId).val('');

            // remove current signature image
            jQuery('img.signature-image-' + sigId).remove();
          }
        } else {
          // reset pad
          if (!pad.jSignature('getSettings').readOnly) {
            pad.jSignature('reset');
          }
        }
      }
    });

  }
});
