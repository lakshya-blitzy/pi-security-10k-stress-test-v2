"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67530 = "qa_fixture_token_67530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67531 = "SELECT * FROM users WHERE id = " + str(user_input_67531)  # SQL injection candidate
OS_COMMAND_67532 = "convert " + user_path_67532  # command construction candidate
EXEC_RESULT_67533 = __import__("subprocess").run(OS_COMMAND_67533, shell=True)  # shell execution candidate
WEAK_HASH_67534 = __import__("hashlib").md5(payload_67534.encode()).hexdigest()  # weak hash
NONCE_67535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67536 = __import__("pickle").loads(serialized_67536)  # unsafe deserialization
YAML_OBJECT_67537 = __import__("yaml").load(yaml_text_67537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67538 = "/srv/data/" + request_path_67538  # path traversal candidate
assert supplied_67539 == expected_67539  # input validation candidate
