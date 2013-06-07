
var bla = null;

function TodoCtrl($scope) {
  $scope.todos = [
    {text:'learn angular', done:true},
    {text:'build an angular app', done:false}];
 
  $scope.addTodo = function() {
    $scope.todos.push({text:$scope.todoText, done:false});
    $scope.todoText = '';
  };
 
  $scope.remaining = function() {
    var count = 0;
    angular.forEach($scope.todos, function(todo) {
      count += todo.done ? 0 : 1;
    });
    return count;
  };
 
  $scope.archive = function() {
    var oldTodos = $scope.todos;
    $scope.todos = [];
    angular.forEach(oldTodos, function(todo) {
      if (!todo.done) $scope.todos.push(todo);
    });
  };
}

function ListCtrl($scope) {
  console.log('init');

  bla = $scope;

  if (!base_data_set) {
      console.log('base data not set');
      return;
  }

  function update_pagination(nitems, current) {
      var pagination = $('#call_pagination');
      pagination.html('');

      var pages = parseInt(nitems / 5);
      if (nitems % 5) {
          pages += 1;
      }

      if (current == 0)
        pagination.append($('<li class="arrow unavailable"><a href>«</a></li>'));
      else
        pagination.append($('<li class="arrow"><a href>«</a></li>'));

      for (var idx=0; idx<pages; idx++) {
          var li = null;
          var npage = idx+1;
          if (idx == current)
              li = $('<li class="current"><a href>'+npage+'</a></li>');
          else
              li = $('<li><a href>'+npage+'</a></li>');
          pagination.append(li);
      }

      if (current == pages-1)
        pagination.append($('<li class="arrow unavailable"><a href>»</a></li>'));
      else
        pagination.append($('<li class="arrow"><a href>»</a></li>'));
  }

  //update_pagination(base_data.phones[1], 0);
  $scope.phones = base_data.phones[0];

  $scope.addPhone = function() {
    $scope.phones.push({name:$scope.phoneName, snippet:'bla', number:$scope.phoneNumber, done:false});
    $scope.todoName = '';
    $scope.todoNumber = '';
  };
 
}

function UserCtrl($scope) {
  console.log('init');
  if (!base_data_set) {
      console.log('base data not set');
      return;
  }

  $scope.name = base_data.user.name;
  $scope.number = base_data.user.number;
  $scope.credit = base_data.user.credit;
}

function add_member() {
    setTimeout(function() {bla.$apply(bla.phones.push({name:'annie', snippet:'build an angular app', done:false, number:'678333345'})); console.log("add");}, 10000);
}

add_member()
