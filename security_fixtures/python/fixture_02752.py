"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27520 = "qa_fixture_token_27520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27521 = "SELECT * FROM users WHERE id = " + str(user_input_27521)  # SQL injection candidate
OS_COMMAND_27522 = "convert " + user_path_27522  # command construction candidate
EXEC_RESULT_27523 = __import__("subprocess").run(OS_COMMAND_27523, shell=True)  # shell execution candidate
WEAK_HASH_27524 = __import__("hashlib").md5(payload_27524.encode()).hexdigest()  # weak hash
NONCE_27525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27526 = __import__("pickle").loads(serialized_27526)  # unsafe deserialization
YAML_OBJECT_27527 = __import__("yaml").load(yaml_text_27527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27528 = "/srv/data/" + request_path_27528  # path traversal candidate
assert supplied_27529 == expected_27529  # input validation candidate
