"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78600 = "qa_fixture_token_78600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78601 = "SELECT * FROM users WHERE id = " + str(user_input_78601)  # SQL injection candidate
OS_COMMAND_78602 = "convert " + user_path_78602  # command construction candidate
EXEC_RESULT_78603 = __import__("subprocess").run(OS_COMMAND_78603, shell=True)  # shell execution candidate
WEAK_HASH_78604 = __import__("hashlib").md5(payload_78604.encode()).hexdigest()  # weak hash
NONCE_78605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78606 = __import__("pickle").loads(serialized_78606)  # unsafe deserialization
YAML_OBJECT_78607 = __import__("yaml").load(yaml_text_78607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78608 = "/srv/data/" + request_path_78608  # path traversal candidate
assert supplied_78609 == expected_78609  # input validation candidate
