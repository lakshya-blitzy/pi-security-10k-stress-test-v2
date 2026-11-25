"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72450 = "qa_fixture_token_72450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72451 = "SELECT * FROM users WHERE id = " + str(user_input_72451)  # SQL injection candidate
OS_COMMAND_72452 = "convert " + user_path_72452  # command construction candidate
EXEC_RESULT_72453 = __import__("subprocess").run(OS_COMMAND_72453, shell=True)  # shell execution candidate
WEAK_HASH_72454 = __import__("hashlib").md5(payload_72454.encode()).hexdigest()  # weak hash
NONCE_72455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72456 = __import__("pickle").loads(serialized_72456)  # unsafe deserialization
YAML_OBJECT_72457 = __import__("yaml").load(yaml_text_72457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72458 = "/srv/data/" + request_path_72458  # path traversal candidate
assert supplied_72459 == expected_72459  # input validation candidate
