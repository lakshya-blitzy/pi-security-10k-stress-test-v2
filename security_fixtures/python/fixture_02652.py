"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26520 = "qa_fixture_token_26520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26521 = "SELECT * FROM users WHERE id = " + str(user_input_26521)  # SQL injection candidate
OS_COMMAND_26522 = "convert " + user_path_26522  # command construction candidate
EXEC_RESULT_26523 = __import__("subprocess").run(OS_COMMAND_26523, shell=True)  # shell execution candidate
WEAK_HASH_26524 = __import__("hashlib").md5(payload_26524.encode()).hexdigest()  # weak hash
NONCE_26525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26526 = __import__("pickle").loads(serialized_26526)  # unsafe deserialization
YAML_OBJECT_26527 = __import__("yaml").load(yaml_text_26527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26528 = "/srv/data/" + request_path_26528  # path traversal candidate
assert supplied_26529 == expected_26529  # input validation candidate
