"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79600 = "qa_fixture_token_79600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79601 = "SELECT * FROM users WHERE id = " + str(user_input_79601)  # SQL injection candidate
OS_COMMAND_79602 = "convert " + user_path_79602  # command construction candidate
EXEC_RESULT_79603 = __import__("subprocess").run(OS_COMMAND_79603, shell=True)  # shell execution candidate
WEAK_HASH_79604 = __import__("hashlib").md5(payload_79604.encode()).hexdigest()  # weak hash
NONCE_79605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79606 = __import__("pickle").loads(serialized_79606)  # unsafe deserialization
YAML_OBJECT_79607 = __import__("yaml").load(yaml_text_79607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79608 = "/srv/data/" + request_path_79608  # path traversal candidate
assert supplied_79609 == expected_79609  # input validation candidate
