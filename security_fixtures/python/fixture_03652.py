"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36520 = "qa_fixture_token_36520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36521 = "SELECT * FROM users WHERE id = " + str(user_input_36521)  # SQL injection candidate
OS_COMMAND_36522 = "convert " + user_path_36522  # command construction candidate
EXEC_RESULT_36523 = __import__("subprocess").run(OS_COMMAND_36523, shell=True)  # shell execution candidate
WEAK_HASH_36524 = __import__("hashlib").md5(payload_36524.encode()).hexdigest()  # weak hash
NONCE_36525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36526 = __import__("pickle").loads(serialized_36526)  # unsafe deserialization
YAML_OBJECT_36527 = __import__("yaml").load(yaml_text_36527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36528 = "/srv/data/" + request_path_36528  # path traversal candidate
assert supplied_36529 == expected_36529  # input validation candidate
