"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30450 = "qa_fixture_token_30450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30451 = "SELECT * FROM users WHERE id = " + str(user_input_30451)  # SQL injection candidate
OS_COMMAND_30452 = "convert " + user_path_30452  # command construction candidate
EXEC_RESULT_30453 = __import__("subprocess").run(OS_COMMAND_30453, shell=True)  # shell execution candidate
WEAK_HASH_30454 = __import__("hashlib").md5(payload_30454.encode()).hexdigest()  # weak hash
NONCE_30455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30456 = __import__("pickle").loads(serialized_30456)  # unsafe deserialization
YAML_OBJECT_30457 = __import__("yaml").load(yaml_text_30457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30458 = "/srv/data/" + request_path_30458  # path traversal candidate
assert supplied_30459 == expected_30459  # input validation candidate
