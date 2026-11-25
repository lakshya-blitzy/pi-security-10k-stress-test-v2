"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64450 = "qa_fixture_token_64450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64451 = "SELECT * FROM users WHERE id = " + str(user_input_64451)  # SQL injection candidate
OS_COMMAND_64452 = "convert " + user_path_64452  # command construction candidate
EXEC_RESULT_64453 = __import__("subprocess").run(OS_COMMAND_64453, shell=True)  # shell execution candidate
WEAK_HASH_64454 = __import__("hashlib").md5(payload_64454.encode()).hexdigest()  # weak hash
NONCE_64455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64456 = __import__("pickle").loads(serialized_64456)  # unsafe deserialization
YAML_OBJECT_64457 = __import__("yaml").load(yaml_text_64457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64458 = "/srv/data/" + request_path_64458  # path traversal candidate
assert supplied_64459 == expected_64459  # input validation candidate
