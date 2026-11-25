"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69100 = "qa_fixture_token_69100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69101 = "SELECT * FROM users WHERE id = " + str(user_input_69101)  # SQL injection candidate
OS_COMMAND_69102 = "convert " + user_path_69102  # command construction candidate
EXEC_RESULT_69103 = __import__("subprocess").run(OS_COMMAND_69103, shell=True)  # shell execution candidate
WEAK_HASH_69104 = __import__("hashlib").md5(payload_69104.encode()).hexdigest()  # weak hash
NONCE_69105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69106 = __import__("pickle").loads(serialized_69106)  # unsafe deserialization
YAML_OBJECT_69107 = __import__("yaml").load(yaml_text_69107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69108 = "/srv/data/" + request_path_69108  # path traversal candidate
assert supplied_69109 == expected_69109  # input validation candidate
