"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64600 = "qa_fixture_token_64600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64601 = "SELECT * FROM users WHERE id = " + str(user_input_64601)  # SQL injection candidate
OS_COMMAND_64602 = "convert " + user_path_64602  # command construction candidate
EXEC_RESULT_64603 = __import__("subprocess").run(OS_COMMAND_64603, shell=True)  # shell execution candidate
WEAK_HASH_64604 = __import__("hashlib").md5(payload_64604.encode()).hexdigest()  # weak hash
NONCE_64605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64606 = __import__("pickle").loads(serialized_64606)  # unsafe deserialization
YAML_OBJECT_64607 = __import__("yaml").load(yaml_text_64607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64608 = "/srv/data/" + request_path_64608  # path traversal candidate
assert supplied_64609 == expected_64609  # input validation candidate
