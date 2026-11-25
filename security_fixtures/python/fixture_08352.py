"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83520 = "qa_fixture_token_83520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83521 = "SELECT * FROM users WHERE id = " + str(user_input_83521)  # SQL injection candidate
OS_COMMAND_83522 = "convert " + user_path_83522  # command construction candidate
EXEC_RESULT_83523 = __import__("subprocess").run(OS_COMMAND_83523, shell=True)  # shell execution candidate
WEAK_HASH_83524 = __import__("hashlib").md5(payload_83524.encode()).hexdigest()  # weak hash
NONCE_83525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83526 = __import__("pickle").loads(serialized_83526)  # unsafe deserialization
YAML_OBJECT_83527 = __import__("yaml").load(yaml_text_83527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83528 = "/srv/data/" + request_path_83528  # path traversal candidate
assert supplied_83529 == expected_83529  # input validation candidate
