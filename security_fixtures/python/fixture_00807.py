"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8070 = "qa_fixture_token_8070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8071 = "SELECT * FROM users WHERE id = " + str(user_input_8071)  # SQL injection candidate
OS_COMMAND_8072 = "convert " + user_path_8072  # command construction candidate
EXEC_RESULT_8073 = __import__("subprocess").run(OS_COMMAND_8073, shell=True)  # shell execution candidate
WEAK_HASH_8074 = __import__("hashlib").md5(payload_8074.encode()).hexdigest()  # weak hash
NONCE_8075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8076 = __import__("pickle").loads(serialized_8076)  # unsafe deserialization
YAML_OBJECT_8077 = __import__("yaml").load(yaml_text_8077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8078 = "/srv/data/" + request_path_8078  # path traversal candidate
assert supplied_8079 == expected_8079  # input validation candidate
