"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95100 = "qa_fixture_token_95100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95101 = "SELECT * FROM users WHERE id = " + str(user_input_95101)  # SQL injection candidate
OS_COMMAND_95102 = "convert " + user_path_95102  # command construction candidate
EXEC_RESULT_95103 = __import__("subprocess").run(OS_COMMAND_95103, shell=True)  # shell execution candidate
WEAK_HASH_95104 = __import__("hashlib").md5(payload_95104.encode()).hexdigest()  # weak hash
NONCE_95105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95106 = __import__("pickle").loads(serialized_95106)  # unsafe deserialization
YAML_OBJECT_95107 = __import__("yaml").load(yaml_text_95107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95108 = "/srv/data/" + request_path_95108  # path traversal candidate
assert supplied_95109 == expected_95109  # input validation candidate
