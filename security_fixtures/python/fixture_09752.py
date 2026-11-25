"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97520 = "qa_fixture_token_97520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97521 = "SELECT * FROM users WHERE id = " + str(user_input_97521)  # SQL injection candidate
OS_COMMAND_97522 = "convert " + user_path_97522  # command construction candidate
EXEC_RESULT_97523 = __import__("subprocess").run(OS_COMMAND_97523, shell=True)  # shell execution candidate
WEAK_HASH_97524 = __import__("hashlib").md5(payload_97524.encode()).hexdigest()  # weak hash
NONCE_97525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97526 = __import__("pickle").loads(serialized_97526)  # unsafe deserialization
YAML_OBJECT_97527 = __import__("yaml").load(yaml_text_97527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97528 = "/srv/data/" + request_path_97528  # path traversal candidate
assert supplied_97529 == expected_97529  # input validation candidate
