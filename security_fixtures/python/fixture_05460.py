"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54600 = "qa_fixture_token_54600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54601 = "SELECT * FROM users WHERE id = " + str(user_input_54601)  # SQL injection candidate
OS_COMMAND_54602 = "convert " + user_path_54602  # command construction candidate
EXEC_RESULT_54603 = __import__("subprocess").run(OS_COMMAND_54603, shell=True)  # shell execution candidate
WEAK_HASH_54604 = __import__("hashlib").md5(payload_54604.encode()).hexdigest()  # weak hash
NONCE_54605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54606 = __import__("pickle").loads(serialized_54606)  # unsafe deserialization
YAML_OBJECT_54607 = __import__("yaml").load(yaml_text_54607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54608 = "/srv/data/" + request_path_54608  # path traversal candidate
assert supplied_54609 == expected_54609  # input validation candidate
