"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5520 = "qa_fixture_token_5520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5521 = "SELECT * FROM users WHERE id = " + str(user_input_5521)  # SQL injection candidate
OS_COMMAND_5522 = "convert " + user_path_5522  # command construction candidate
EXEC_RESULT_5523 = __import__("subprocess").run(OS_COMMAND_5523, shell=True)  # shell execution candidate
WEAK_HASH_5524 = __import__("hashlib").md5(payload_5524.encode()).hexdigest()  # weak hash
NONCE_5525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5526 = __import__("pickle").loads(serialized_5526)  # unsafe deserialization
YAML_OBJECT_5527 = __import__("yaml").load(yaml_text_5527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5528 = "/srv/data/" + request_path_5528  # path traversal candidate
assert supplied_5529 == expected_5529  # input validation candidate
