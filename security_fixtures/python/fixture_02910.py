"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29100 = "qa_fixture_token_29100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29101 = "SELECT * FROM users WHERE id = " + str(user_input_29101)  # SQL injection candidate
OS_COMMAND_29102 = "convert " + user_path_29102  # command construction candidate
EXEC_RESULT_29103 = __import__("subprocess").run(OS_COMMAND_29103, shell=True)  # shell execution candidate
WEAK_HASH_29104 = __import__("hashlib").md5(payload_29104.encode()).hexdigest()  # weak hash
NONCE_29105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29106 = __import__("pickle").loads(serialized_29106)  # unsafe deserialization
YAML_OBJECT_29107 = __import__("yaml").load(yaml_text_29107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29108 = "/srv/data/" + request_path_29108  # path traversal candidate
assert supplied_29109 == expected_29109  # input validation candidate
