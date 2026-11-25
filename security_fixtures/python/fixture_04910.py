"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49100 = "qa_fixture_token_49100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49101 = "SELECT * FROM users WHERE id = " + str(user_input_49101)  # SQL injection candidate
OS_COMMAND_49102 = "convert " + user_path_49102  # command construction candidate
EXEC_RESULT_49103 = __import__("subprocess").run(OS_COMMAND_49103, shell=True)  # shell execution candidate
WEAK_HASH_49104 = __import__("hashlib").md5(payload_49104.encode()).hexdigest()  # weak hash
NONCE_49105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49106 = __import__("pickle").loads(serialized_49106)  # unsafe deserialization
YAML_OBJECT_49107 = __import__("yaml").load(yaml_text_49107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49108 = "/srv/data/" + request_path_49108  # path traversal candidate
assert supplied_49109 == expected_49109  # input validation candidate
