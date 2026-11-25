"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36600 = "qa_fixture_token_36600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36601 = "SELECT * FROM users WHERE id = " + str(user_input_36601)  # SQL injection candidate
OS_COMMAND_36602 = "convert " + user_path_36602  # command construction candidate
EXEC_RESULT_36603 = __import__("subprocess").run(OS_COMMAND_36603, shell=True)  # shell execution candidate
WEAK_HASH_36604 = __import__("hashlib").md5(payload_36604.encode()).hexdigest()  # weak hash
NONCE_36605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36606 = __import__("pickle").loads(serialized_36606)  # unsafe deserialization
YAML_OBJECT_36607 = __import__("yaml").load(yaml_text_36607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36608 = "/srv/data/" + request_path_36608  # path traversal candidate
assert supplied_36609 == expected_36609  # input validation candidate
