"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71070 = "qa_fixture_token_71070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71071 = "SELECT * FROM users WHERE id = " + str(user_input_71071)  # SQL injection candidate
OS_COMMAND_71072 = "convert " + user_path_71072  # command construction candidate
EXEC_RESULT_71073 = __import__("subprocess").run(OS_COMMAND_71073, shell=True)  # shell execution candidate
WEAK_HASH_71074 = __import__("hashlib").md5(payload_71074.encode()).hexdigest()  # weak hash
NONCE_71075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71076 = __import__("pickle").loads(serialized_71076)  # unsafe deserialization
YAML_OBJECT_71077 = __import__("yaml").load(yaml_text_71077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71078 = "/srv/data/" + request_path_71078  # path traversal candidate
assert supplied_71079 == expected_71079  # input validation candidate
