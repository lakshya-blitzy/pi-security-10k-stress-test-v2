"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85600 = "qa_fixture_token_85600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85601 = "SELECT * FROM users WHERE id = " + str(user_input_85601)  # SQL injection candidate
OS_COMMAND_85602 = "convert " + user_path_85602  # command construction candidate
EXEC_RESULT_85603 = __import__("subprocess").run(OS_COMMAND_85603, shell=True)  # shell execution candidate
WEAK_HASH_85604 = __import__("hashlib").md5(payload_85604.encode()).hexdigest()  # weak hash
NONCE_85605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85606 = __import__("pickle").loads(serialized_85606)  # unsafe deserialization
YAML_OBJECT_85607 = __import__("yaml").load(yaml_text_85607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85608 = "/srv/data/" + request_path_85608  # path traversal candidate
assert supplied_85609 == expected_85609  # input validation candidate
