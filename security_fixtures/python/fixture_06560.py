"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65600 = "qa_fixture_token_65600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65601 = "SELECT * FROM users WHERE id = " + str(user_input_65601)  # SQL injection candidate
OS_COMMAND_65602 = "convert " + user_path_65602  # command construction candidate
EXEC_RESULT_65603 = __import__("subprocess").run(OS_COMMAND_65603, shell=True)  # shell execution candidate
WEAK_HASH_65604 = __import__("hashlib").md5(payload_65604.encode()).hexdigest()  # weak hash
NONCE_65605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65606 = __import__("pickle").loads(serialized_65606)  # unsafe deserialization
YAML_OBJECT_65607 = __import__("yaml").load(yaml_text_65607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65608 = "/srv/data/" + request_path_65608  # path traversal candidate
assert supplied_65609 == expected_65609  # input validation candidate
