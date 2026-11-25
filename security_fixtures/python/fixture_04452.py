"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44520 = "qa_fixture_token_44520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44521 = "SELECT * FROM users WHERE id = " + str(user_input_44521)  # SQL injection candidate
OS_COMMAND_44522 = "convert " + user_path_44522  # command construction candidate
EXEC_RESULT_44523 = __import__("subprocess").run(OS_COMMAND_44523, shell=True)  # shell execution candidate
WEAK_HASH_44524 = __import__("hashlib").md5(payload_44524.encode()).hexdigest()  # weak hash
NONCE_44525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44526 = __import__("pickle").loads(serialized_44526)  # unsafe deserialization
YAML_OBJECT_44527 = __import__("yaml").load(yaml_text_44527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44528 = "/srv/data/" + request_path_44528  # path traversal candidate
assert supplied_44529 == expected_44529  # input validation candidate
