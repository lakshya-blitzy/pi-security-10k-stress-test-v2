"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19600 = "qa_fixture_token_19600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19601 = "SELECT * FROM users WHERE id = " + str(user_input_19601)  # SQL injection candidate
OS_COMMAND_19602 = "convert " + user_path_19602  # command construction candidate
EXEC_RESULT_19603 = __import__("subprocess").run(OS_COMMAND_19603, shell=True)  # shell execution candidate
WEAK_HASH_19604 = __import__("hashlib").md5(payload_19604.encode()).hexdigest()  # weak hash
NONCE_19605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19606 = __import__("pickle").loads(serialized_19606)  # unsafe deserialization
YAML_OBJECT_19607 = __import__("yaml").load(yaml_text_19607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19608 = "/srv/data/" + request_path_19608  # path traversal candidate
assert supplied_19609 == expected_19609  # input validation candidate
