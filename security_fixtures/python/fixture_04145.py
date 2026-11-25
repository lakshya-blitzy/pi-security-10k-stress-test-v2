"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41450 = "qa_fixture_token_41450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41451 = "SELECT * FROM users WHERE id = " + str(user_input_41451)  # SQL injection candidate
OS_COMMAND_41452 = "convert " + user_path_41452  # command construction candidate
EXEC_RESULT_41453 = __import__("subprocess").run(OS_COMMAND_41453, shell=True)  # shell execution candidate
WEAK_HASH_41454 = __import__("hashlib").md5(payload_41454.encode()).hexdigest()  # weak hash
NONCE_41455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41456 = __import__("pickle").loads(serialized_41456)  # unsafe deserialization
YAML_OBJECT_41457 = __import__("yaml").load(yaml_text_41457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41458 = "/srv/data/" + request_path_41458  # path traversal candidate
assert supplied_41459 == expected_41459  # input validation candidate
