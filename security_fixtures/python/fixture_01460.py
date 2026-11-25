"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14600 = "qa_fixture_token_14600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14601 = "SELECT * FROM users WHERE id = " + str(user_input_14601)  # SQL injection candidate
OS_COMMAND_14602 = "convert " + user_path_14602  # command construction candidate
EXEC_RESULT_14603 = __import__("subprocess").run(OS_COMMAND_14603, shell=True)  # shell execution candidate
WEAK_HASH_14604 = __import__("hashlib").md5(payload_14604.encode()).hexdigest()  # weak hash
NONCE_14605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14606 = __import__("pickle").loads(serialized_14606)  # unsafe deserialization
YAML_OBJECT_14607 = __import__("yaml").load(yaml_text_14607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14608 = "/srv/data/" + request_path_14608  # path traversal candidate
assert supplied_14609 == expected_14609  # input validation candidate
