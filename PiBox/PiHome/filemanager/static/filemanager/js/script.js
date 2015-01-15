var action,type;
var selected_dir_id,selected_file;
var zclip = false;

function get_human_string(val)
{
  var denominations = ['B', 'KB', 'MB', 'GB', 'TB'];
  var i = 0;
  while(val > 1024)
  {
    ++i;
    val = val/1024;
  }
  val = val.toString();
  if(val.indexOf('.') != -1)
    val = val.substr(0,val.indexOf('.')+3);
  return val + denominations[i];
}

function size(){
  $('#main').height($(window).height()-47);
  $('#left').height($(window).height()-69);
  $('#right').height($(window).height()-49);
  $('#content').height($(window).height()-100);
}

function onload(){
  size();
  refresh_dirs();
  show_files(dir_id);
  $('body').bind('click',function(e){$('#dir-menu').hide();$('#file-menu').hide();});
  if(messages.length>0){
    $('#message').html(messages[0]);
    setTimeout("$('#message').html('Hint : Use right click to add, rename or delete files and folders');",10000);
  }
  else
     $('#message').html('Hint : Use right click to add,rename or delete files and folders');
  $('#ufile').change(function(){form_submit('upload','file');});
  if($.browser.mozilla) {
    moz_major_ver = (+($.browser.version.split(".")[0]))
    if(moz_major_ver < 23){
      // https://bugzilla.mozilla.org/show_bug.cgi?id=701353 should be fixed in 23
      $('#upload-label').click(function(){
        $('#ufile').click();
      });
    }
  }
  $('#space_quota').width(((space_consumed*100)/max_space).toString()+'%');
  $('#space_quota_string').html(get_human_string(space_consumed) + ' of ' + get_human_string(max_space) + ' used');
}

$('body').ready(onload);
$(window).resize(size);

function refresh_dirs()
{
 $('#left').html(show_directories(dir_structure));
}

function get_dir(id,ds)
{if(!ds)ds=dir_structure;
 dir = null;
 for(d in ds)
 { if(ds[d]['id']==id)
   { dir = ds[d];
     break;
   }
   var dq = get_dir(id,ds[d]['dirs']);
   if(dq != null)
   { dir =dq;
     break;
   }
 }
 return dir;
}

function get_path(id,ds,basepath)
{if(!ds)ds=dir_structure;
 if(!basepath)basepath='';
 path = null;
 for(d in ds)
 { if(ds[d]['id']==id)
   { path=d+'/';
     break
   }
   var pq = get_path(id,ds[d]['dirs'],d+'/');
   if(pq != null)
   { path=pq;
     break;
   }
 }
 if(path) return basepath+path;
 else return null;
}

function change_sign(id)
{d = get_dir(id);
 if(d['open']=='yes')d['open']='no';
 else d['open']='yes';
 refresh_dirs();
}

function CKEditorRepy(filename)
{ var filepath = ckeditor_baseurl+get_path(dir_id)+filename;
  window.opener.CKEDITOR.tools.callFunction(CKEditorFuncNum,filepath);
  window.close();
}

function show_files(id)
{ dir_id = id;
  var dirs = [];
  var dir_list = get_dir(id)['dirs'];
  for(var a in dir_list)
    dirs.push({'name':a,'id':dir_list[a]['id']});
  dirs = dirs.sort(function(a,b){
      if(a['name'].toLowerCase() < b['name'].toLowerCase())return -1;
      if(a['name'].toLowerCase() > b['name'].toLowerCase())return 1;
      return 0;
  });
  files = get_dir(id)['files'].sort(
          function(a, b) {
            if (a.toLowerCase() < b.toLowerCase()) return -1;
            if (a.toLowerCase() > b.toLowerCase()) return 1;
            return 0;
          });
  $('#content').html('');
  for(d in dirs)
  {
    $('#content').append("<div class='file' title='"+dirs[d]['name']+"'"+
       "onmousedown='rightclick_handle(event,\""+dirs[d]['id']+"\",\"dir\");' ondblclick=\"show_files("+dirs[d]['id']+")\"><div class='thumbnail'>"+
       "<div style=\"background-image:url('"+static_url+"filemanager/images/folder_big.png');\" width='100%' height='100%' ></div></div>"+
       "<div class='filename'>"+dirs[d]['name']+"</div></div>\n");
  }
  for(f in files)
  { var ext = files[f].split('.')[(files[f].split('.').length-1)];
    $('#content').append("<div class='file' title='"+files[f]+"'"+
       "onmousedown='rightclick_handle(event,\""+files[f]+"\",\"file\");'><div class='thumbnail'>"+
       "<div style=\"background-image:url('"+get_path(id).substr(1)+files[f]+"');\" width='100%' height='100%' ></div></div>"+
       "<div class='filename'>"+files[f]+"</div></div>\n");
  }
  $('#status').html(get_path(id))
  $('.current_directory').removeClass('current_directory');
  $('#'+dir_id).addClass('current_directory');
}

function show_directories(ds)
{ var html = "";
  for(d in ds)
  {  var image = (ds[d]['open']=='yes'?'opened_folder.png':'folder.png');
     if(d=='')image = 'home_folder.png';
     var id = ds[d]['id'];
     var sign;
     sign = (ds[d]['open']=='yes'?'[-]':'[+]');
     var empty = true;
     for(i in ds[d]['dirs']){empty=false;break;}
     if(empty)sign = '';
     html+="<div class='directory "+(id==dir_id?'current_directory':'')+"' id='"+id+"'><div class='directory-sign' onclick='change_sign("+id+")'>"+sign+"</div>"+
           "<div class='directory-image-name' onclick='show_files("+id+")' onmousedown='rightclick_handle(event,"+id+",\"dir\");'>"+
           "<img class='directory-image' src='"+static_url+"filemanager/images/"+image+"'/>"+
           "<div class='directory-name' >"+(d==''?'root':d)+"</div></div></div>\n";
     if(ds[d]['open']=='yes')
       html+="<div style='padding-left:15px'>"+show_directories(ds[d]['dirs'])+"</div>\n";
  }
  return html;
}

function getPosition(e) {
   e = e || window.event;
   var cursor = {x:0, y:0};
   if (e.pageX || e.pageY) {
       cursor.x = e.pageX;
       cursor.y = e.pageY;
   }
   else {
       var de = document.documentElement;
       var b = document.body;
       cursor.x = e.clientX +
           (de.scrollLeft || b.scrollLeft) - (de.clientLeft || 0);
       cursor.y = e.clientY +
           (de.scrollTop || b.scrollTop) - (de.clientTop || 0);
   }
   return cursor;
}

function rightclick_handle(e,id,type)
{ var c = getPosition(e);
  if(type == 'dir'){
    if(e.button==2){
    selected_dir_id = id;
    $('#dir-menu').css('left',c.x+8);
    $('#dir-menu').css('top',c.y+2);
    if(clipboard['empty'])
    {
      $('#paste-dir').hide();
      $('#paste-dir').next().hide();
    }
    else
    {
      $('#paste-dir').show();
      $('#paste-dir').next().show();
    }
    $('#dir-menu').show();
    }
  }
  else if(type == 'file'){
    if(e.button==2){
    selected_file = id;
    $('#file-menu').css('left',c.x+8);
    $('#file-menu').css('top',c.y+2);
    $('#file-menu').show();
    if(!zclip){
      zclip = true;
      $('#copy-public-link-file').zclip({
        path: static_url+'filemanager/js/jquery/zclip/ZeroClipboard.swf',
        copy: function(){
          var public_link = public_url_base+get_path(dir_id)+selected_file;
          return public_link;
        },
        clickAfter: false,
        beforeCopy: function(){},
        afterCopy: function(){
          $('#file-menu').hide();
        }
      });
    }
    }
    if(e.button==0 && e.detail>=2 && CKEditorFuncNum){
      CKEditorRepy(id);
    }
  }
}

function do_action(act,t)
{var heading;
 if(t == 'dir')
 {if(act == 'add')heading = "Enter name of sub-folder";
  if(act == 'rename')heading = "Enter new name of folder";
  if(act == 'delete'){form_submit(act,t);return;}
  if(act == 'download'){window.open('.'+get_path(selected_dir_id)+'?download=dir');return;}
  if(act == 'cut'){ if(selected_dir_id == 1){alert('You cannot cut root directory');return;}clipboard['empty']=false;clipboard['type']='dir';clipboard['path']=get_path(selected_dir_id);clipboard['mode']='cut';return;}
  if(act == 'copy'){ clipboard['empty']=false;clipboard['type']='dir';clipboard['path']=get_path(selected_dir_id);clipboard['mode']='copy';return;}
  if(act == 'paste')
  {
    if(clipboard['empty'])
    {
      alert('Clipboard is empty. Please cut/copy the required file.');
      return;
    }
    if(get_path(selected_dir_id).indexOf(clipboard['path']) == 0)
    {
      alert('Cannot move/copy to a child folder');
      return;
    }
    if(window.confirm(clipboard['mode']+' '+clipboard['path'] + ' to '+get_path(selected_dir_id)))
    {
        form_submit(clipboard['mode'],'', '');
    }
    return;
  }
 }
 if(t == 'file')
 {if(act == 'rename')heading = "Enter new name of file";
  if(act == 'delete'){form_submit(act,t);return;}
  if(act == 'download'){window.open('.'+get_path(dir_id)+selected_file+'?download=file');return;}
  if(act == 'copy-public-link'){window.prompt("Public URL(Ctrl+C to copy to clipboard):",public_url_base+get_path(dir_id)+selected_file);return;}
  if(act == 'cut'){ clipboard['empty']=false;clipboard['type']='file';clipboard['path']=get_path(dir_id)+selected_file;clipboard['mode']='cut';return;}
  if(act == 'copy'){ clipboard['empty']=false;clipboard['type']='file';clipboard['path']=get_path(dir_id)+selected_file;clipboard['mode']='copy';return;}
 }
 action = act;
 type = t;
 var w = $(window);
 $('#popup').css('left',w.width()/2-100);
 $('#popup').css('top',w.height()/2-100);
 $('#heading').html(heading);
 $('#popup').show();
 $('#input').focus();
 $('#input').keypress(
   function(e){
     code= (e.keyCode ? e.keyCode : e.which);
     if(code == 13){
        var value=$('#input').val();
        $('#input').val('');
        $('#popup').hide();
        form_submit(action,type,value);
     }
   });
}

function form_submit(action,type,value){
  $('#path').val(get_path(dir_id));
  $('#current_path').val(get_path(dir_id));
  $('#file_or_dir').val(type);
  if(action == 'cut')
  {
    $('#action').val('move');
    $('#file_or_dir').val(clipboard['type']);
    $('#path').val(clipboard['path']);
    $('#current_path').val(get_path(selected_dir_id));
    $('#submit').trigger('click');
  }
  if(action == 'copy')
  {
    $('#action').val('copy');
    $('#file_or_dir').val(clipboard['type']);
    $('#path').val(clipboard['path']);
    $('#current_path').val(get_path(selected_dir_id));
    $('#submit').trigger('click');
  }
  if(action == 'upload')
  { $('#action').val('upload');
    $('#submit').trigger('click');
  }
  else if(action == 'add')
  { $('#path').val(get_path(selected_dir_id));
    $('#action').val('add');
    $('#name').val(value);
    $('#submit').trigger('click');
  }
  else if(action == 'rename')
  { if(type == 'dir')$('#path').val(get_path(selected_dir_id));
    if(type == 'file')$('#path').val(get_path(dir_id)+selected_file);
    $('#action').val('rename');
    $('#name').val(value);
    $('#submit').trigger('click');
  }
  else if(action == 'delete')
  { if(type == 'dir')$('#path').val(get_path(selected_dir_id));
    if(type == 'file')$('#path').val(get_path(dir_id)+selected_file);
    $('#action').val('delete');
    $('#submit').trigger('click');
  }
}
