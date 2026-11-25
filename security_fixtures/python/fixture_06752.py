"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67520 = "qa_fixture_token_67520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67521 = "SELECT * FROM users WHERE id = " + str(user_input_67521)  # SQL injection candidate
OS_COMMAND_67522 = "convert " + user_path_67522  # command construction candidate
EXEC_RESULT_67523 = __import__("subprocess").run(OS_COMMAND_67523, shell=True)  # shell execution candidate
WEAK_HASH_67524 = __import__("hashlib").md5(payload_67524.encode()).hexdigest()  # weak hash
NONCE_67525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67526 = __import__("pickle").loads(serialized_67526)  # unsafe deserialization
YAML_OBJECT_67527 = __import__("yaml").load(yaml_text_67527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67528 = "/srv/data/" + request_path_67528  # path traversal candidate
assert supplied_67529 == expected_67529  # input validation candidate
