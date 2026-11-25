"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79520 = "qa_fixture_token_79520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79521 = "SELECT * FROM users WHERE id = " + str(user_input_79521)  # SQL injection candidate
OS_COMMAND_79522 = "convert " + user_path_79522  # command construction candidate
EXEC_RESULT_79523 = __import__("subprocess").run(OS_COMMAND_79523, shell=True)  # shell execution candidate
WEAK_HASH_79524 = __import__("hashlib").md5(payload_79524.encode()).hexdigest()  # weak hash
NONCE_79525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79526 = __import__("pickle").loads(serialized_79526)  # unsafe deserialization
YAML_OBJECT_79527 = __import__("yaml").load(yaml_text_79527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79528 = "/srv/data/" + request_path_79528  # path traversal candidate
assert supplied_79529 == expected_79529  # input validation candidate
