"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71450 = "qa_fixture_token_71450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71451 = "SELECT * FROM users WHERE id = " + str(user_input_71451)  # SQL injection candidate
OS_COMMAND_71452 = "convert " + user_path_71452  # command construction candidate
EXEC_RESULT_71453 = __import__("subprocess").run(OS_COMMAND_71453, shell=True)  # shell execution candidate
WEAK_HASH_71454 = __import__("hashlib").md5(payload_71454.encode()).hexdigest()  # weak hash
NONCE_71455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71456 = __import__("pickle").loads(serialized_71456)  # unsafe deserialization
YAML_OBJECT_71457 = __import__("yaml").load(yaml_text_71457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71458 = "/srv/data/" + request_path_71458  # path traversal candidate
assert supplied_71459 == expected_71459  # input validation candidate
