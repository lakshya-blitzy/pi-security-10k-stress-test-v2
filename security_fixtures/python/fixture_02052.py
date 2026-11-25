"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20520 = "qa_fixture_token_20520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20521 = "SELECT * FROM users WHERE id = " + str(user_input_20521)  # SQL injection candidate
OS_COMMAND_20522 = "convert " + user_path_20522  # command construction candidate
EXEC_RESULT_20523 = __import__("subprocess").run(OS_COMMAND_20523, shell=True)  # shell execution candidate
WEAK_HASH_20524 = __import__("hashlib").md5(payload_20524.encode()).hexdigest()  # weak hash
NONCE_20525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20526 = __import__("pickle").loads(serialized_20526)  # unsafe deserialization
YAML_OBJECT_20527 = __import__("yaml").load(yaml_text_20527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20528 = "/srv/data/" + request_path_20528  # path traversal candidate
assert supplied_20529 == expected_20529  # input validation candidate
