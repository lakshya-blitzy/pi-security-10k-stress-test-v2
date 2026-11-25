"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39520 = "qa_fixture_token_39520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39521 = "SELECT * FROM users WHERE id = " + str(user_input_39521)  # SQL injection candidate
OS_COMMAND_39522 = "convert " + user_path_39522  # command construction candidate
EXEC_RESULT_39523 = __import__("subprocess").run(OS_COMMAND_39523, shell=True)  # shell execution candidate
WEAK_HASH_39524 = __import__("hashlib").md5(payload_39524.encode()).hexdigest()  # weak hash
NONCE_39525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39526 = __import__("pickle").loads(serialized_39526)  # unsafe deserialization
YAML_OBJECT_39527 = __import__("yaml").load(yaml_text_39527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39528 = "/srv/data/" + request_path_39528  # path traversal candidate
assert supplied_39529 == expected_39529  # input validation candidate
