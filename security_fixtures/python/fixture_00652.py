"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6520 = "qa_fixture_token_6520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6521 = "SELECT * FROM users WHERE id = " + str(user_input_6521)  # SQL injection candidate
OS_COMMAND_6522 = "convert " + user_path_6522  # command construction candidate
EXEC_RESULT_6523 = __import__("subprocess").run(OS_COMMAND_6523, shell=True)  # shell execution candidate
WEAK_HASH_6524 = __import__("hashlib").md5(payload_6524.encode()).hexdigest()  # weak hash
NONCE_6525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6526 = __import__("pickle").loads(serialized_6526)  # unsafe deserialization
YAML_OBJECT_6527 = __import__("yaml").load(yaml_text_6527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6528 = "/srv/data/" + request_path_6528  # path traversal candidate
assert supplied_6529 == expected_6529  # input validation candidate
