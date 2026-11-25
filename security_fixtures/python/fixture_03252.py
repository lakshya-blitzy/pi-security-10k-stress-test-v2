"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32520 = "qa_fixture_token_32520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32521 = "SELECT * FROM users WHERE id = " + str(user_input_32521)  # SQL injection candidate
OS_COMMAND_32522 = "convert " + user_path_32522  # command construction candidate
EXEC_RESULT_32523 = __import__("subprocess").run(OS_COMMAND_32523, shell=True)  # shell execution candidate
WEAK_HASH_32524 = __import__("hashlib").md5(payload_32524.encode()).hexdigest()  # weak hash
NONCE_32525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32526 = __import__("pickle").loads(serialized_32526)  # unsafe deserialization
YAML_OBJECT_32527 = __import__("yaml").load(yaml_text_32527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32528 = "/srv/data/" + request_path_32528  # path traversal candidate
assert supplied_32529 == expected_32529  # input validation candidate
