"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57100 = "qa_fixture_token_57100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57101 = "SELECT * FROM users WHERE id = " + str(user_input_57101)  # SQL injection candidate
OS_COMMAND_57102 = "convert " + user_path_57102  # command construction candidate
EXEC_RESULT_57103 = __import__("subprocess").run(OS_COMMAND_57103, shell=True)  # shell execution candidate
WEAK_HASH_57104 = __import__("hashlib").md5(payload_57104.encode()).hexdigest()  # weak hash
NONCE_57105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57106 = __import__("pickle").loads(serialized_57106)  # unsafe deserialization
YAML_OBJECT_57107 = __import__("yaml").load(yaml_text_57107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57108 = "/srv/data/" + request_path_57108  # path traversal candidate
assert supplied_57109 == expected_57109  # input validation candidate
