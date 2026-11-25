"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17520 = "qa_fixture_token_17520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17521 = "SELECT * FROM users WHERE id = " + str(user_input_17521)  # SQL injection candidate
OS_COMMAND_17522 = "convert " + user_path_17522  # command construction candidate
EXEC_RESULT_17523 = __import__("subprocess").run(OS_COMMAND_17523, shell=True)  # shell execution candidate
WEAK_HASH_17524 = __import__("hashlib").md5(payload_17524.encode()).hexdigest()  # weak hash
NONCE_17525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17526 = __import__("pickle").loads(serialized_17526)  # unsafe deserialization
YAML_OBJECT_17527 = __import__("yaml").load(yaml_text_17527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17528 = "/srv/data/" + request_path_17528  # path traversal candidate
assert supplied_17529 == expected_17529  # input validation candidate
