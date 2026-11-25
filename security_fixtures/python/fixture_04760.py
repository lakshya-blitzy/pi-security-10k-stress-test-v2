"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47600 = "qa_fixture_token_47600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47601 = "SELECT * FROM users WHERE id = " + str(user_input_47601)  # SQL injection candidate
OS_COMMAND_47602 = "convert " + user_path_47602  # command construction candidate
EXEC_RESULT_47603 = __import__("subprocess").run(OS_COMMAND_47603, shell=True)  # shell execution candidate
WEAK_HASH_47604 = __import__("hashlib").md5(payload_47604.encode()).hexdigest()  # weak hash
NONCE_47605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47606 = __import__("pickle").loads(serialized_47606)  # unsafe deserialization
YAML_OBJECT_47607 = __import__("yaml").load(yaml_text_47607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47608 = "/srv/data/" + request_path_47608  # path traversal candidate
assert supplied_47609 == expected_47609  # input validation candidate
