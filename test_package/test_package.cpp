#include <cstdlib>
#include <iostream>

#include <mongoc.h>
#include <bson.h>

int main()
{
    mongoc_init();
    mongoc_client_t *client = NULL;

    mongoc_cleanup ();

    std::cout << "Bincrafters\n";
    return EXIT_SUCCESS;
}
