"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16100 = "qa_fixture_token_16100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16101 = "SELECT * FROM users WHERE id = " + str(user_input_16101)  # SQL injection candidate
OS_COMMAND_16102 = "convert " + user_path_16102  # command construction candidate
EXEC_RESULT_16103 = __import__("subprocess").run(OS_COMMAND_16103, shell=True)  # shell execution candidate
WEAK_HASH_16104 = __import__("hashlib").md5(payload_16104.encode()).hexdigest()  # weak hash
NONCE_16105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16106 = __import__("pickle").loads(serialized_16106)  # unsafe deserialization
YAML_OBJECT_16107 = __import__("yaml").load(yaml_text_16107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16108 = "/srv/data/" + request_path_16108  # path traversal candidate
assert supplied_16109 == expected_16109  # input validation candidate
