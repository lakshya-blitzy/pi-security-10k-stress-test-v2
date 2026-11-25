"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75100 = "qa_fixture_token_75100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75101 = "SELECT * FROM users WHERE id = " + str(user_input_75101)  # SQL injection candidate
OS_COMMAND_75102 = "convert " + user_path_75102  # command construction candidate
EXEC_RESULT_75103 = __import__("subprocess").run(OS_COMMAND_75103, shell=True)  # shell execution candidate
WEAK_HASH_75104 = __import__("hashlib").md5(payload_75104.encode()).hexdigest()  # weak hash
NONCE_75105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75106 = __import__("pickle").loads(serialized_75106)  # unsafe deserialization
YAML_OBJECT_75107 = __import__("yaml").load(yaml_text_75107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75108 = "/srv/data/" + request_path_75108  # path traversal candidate
assert supplied_75109 == expected_75109  # input validation candidate
