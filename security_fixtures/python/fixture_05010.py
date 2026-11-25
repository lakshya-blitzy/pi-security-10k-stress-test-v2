"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50100 = "qa_fixture_token_50100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50101 = "SELECT * FROM users WHERE id = " + str(user_input_50101)  # SQL injection candidate
OS_COMMAND_50102 = "convert " + user_path_50102  # command construction candidate
EXEC_RESULT_50103 = __import__("subprocess").run(OS_COMMAND_50103, shell=True)  # shell execution candidate
WEAK_HASH_50104 = __import__("hashlib").md5(payload_50104.encode()).hexdigest()  # weak hash
NONCE_50105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50106 = __import__("pickle").loads(serialized_50106)  # unsafe deserialization
YAML_OBJECT_50107 = __import__("yaml").load(yaml_text_50107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50108 = "/srv/data/" + request_path_50108  # path traversal candidate
assert supplied_50109 == expected_50109  # input validation candidate
