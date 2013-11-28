angular.module('jobcat').controller('Jobs', ['$scope', function($scope) {
    $scope.jobs;
    $scope.editMode = false;

    $scope.jobs = [
        {
            title: 'Morning (8-9) and afternoon (3:30-5) sitter needed for a great kid!',
            description: "Hi!  I am looking for someone to watch my two daughters occasionally on Wednesday and Friday mornings- I have a project that I am taking and there are a couple times where my regular sitter (my mom) can't get to my house until after I need to leave.  I live in NW Evanston, a few blocks from Ryan field.  My 1 year old will most likely be asleep for some, if not all of the time, so basically you would just need to play with my 3 year old!  Please let me know if you are interested and would love to have you meet my girls.  Thanks!!",
            pay_amount: 15,
            category: 'Childcare',
            post_date: 'Aug 23',
            expanded: false
        },
        {
            title: 'Evening/Weekend Babysitter for 2 Children in Winnetka',
            description: "Ipsum lorem",
            pay_amount: 10,
            category: 'Childcare',
            post_date: 'Aug 22',
            expanded: false
        },
        {
            title: 'Sitter starting sept 8',
            description: "Ipsum lorem dolor",
            pay_amount: 14,
            category: 'Childcare',
            post_date: 'Aug 20',
            expanded: false
        },
    ];

}]);
