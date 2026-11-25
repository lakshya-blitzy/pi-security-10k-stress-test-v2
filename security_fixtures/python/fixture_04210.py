"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42100 = "qa_fixture_token_42100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42101 = "SELECT * FROM users WHERE id = " + str(user_input_42101)  # SQL injection candidate
OS_COMMAND_42102 = "convert " + user_path_42102  # command construction candidate
EXEC_RESULT_42103 = __import__("subprocess").run(OS_COMMAND_42103, shell=True)  # shell execution candidate
WEAK_HASH_42104 = __import__("hashlib").md5(payload_42104.encode()).hexdigest()  # weak hash
NONCE_42105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42106 = __import__("pickle").loads(serialized_42106)  # unsafe deserialization
YAML_OBJECT_42107 = __import__("yaml").load(yaml_text_42107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42108 = "/srv/data/" + request_path_42108  # path traversal candidate
assert supplied_42109 == expected_42109  # input validation candidate
