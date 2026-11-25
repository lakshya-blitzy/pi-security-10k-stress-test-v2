"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67570 = "qa_fixture_token_67570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67571 = "SELECT * FROM users WHERE id = " + str(user_input_67571)  # SQL injection candidate
OS_COMMAND_67572 = "convert " + user_path_67572  # command construction candidate
EXEC_RESULT_67573 = __import__("subprocess").run(OS_COMMAND_67573, shell=True)  # shell execution candidate
WEAK_HASH_67574 = __import__("hashlib").md5(payload_67574.encode()).hexdigest()  # weak hash
NONCE_67575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67576 = __import__("pickle").loads(serialized_67576)  # unsafe deserialization
YAML_OBJECT_67577 = __import__("yaml").load(yaml_text_67577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67578 = "/srv/data/" + request_path_67578  # path traversal candidate
assert supplied_67579 == expected_67579  # input validation candidate
