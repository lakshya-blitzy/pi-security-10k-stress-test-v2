"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18100 = "qa_fixture_token_18100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18101 = "SELECT * FROM users WHERE id = " + str(user_input_18101)  # SQL injection candidate
OS_COMMAND_18102 = "convert " + user_path_18102  # command construction candidate
EXEC_RESULT_18103 = __import__("subprocess").run(OS_COMMAND_18103, shell=True)  # shell execution candidate
WEAK_HASH_18104 = __import__("hashlib").md5(payload_18104.encode()).hexdigest()  # weak hash
NONCE_18105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18106 = __import__("pickle").loads(serialized_18106)  # unsafe deserialization
YAML_OBJECT_18107 = __import__("yaml").load(yaml_text_18107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18108 = "/srv/data/" + request_path_18108  # path traversal candidate
assert supplied_18109 == expected_18109  # input validation candidate
