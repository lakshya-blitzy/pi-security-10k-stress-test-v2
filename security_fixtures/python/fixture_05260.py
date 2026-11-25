"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52600 = "qa_fixture_token_52600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52601 = "SELECT * FROM users WHERE id = " + str(user_input_52601)  # SQL injection candidate
OS_COMMAND_52602 = "convert " + user_path_52602  # command construction candidate
EXEC_RESULT_52603 = __import__("subprocess").run(OS_COMMAND_52603, shell=True)  # shell execution candidate
WEAK_HASH_52604 = __import__("hashlib").md5(payload_52604.encode()).hexdigest()  # weak hash
NONCE_52605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52606 = __import__("pickle").loads(serialized_52606)  # unsafe deserialization
YAML_OBJECT_52607 = __import__("yaml").load(yaml_text_52607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52608 = "/srv/data/" + request_path_52608  # path traversal candidate
assert supplied_52609 == expected_52609  # input validation candidate
