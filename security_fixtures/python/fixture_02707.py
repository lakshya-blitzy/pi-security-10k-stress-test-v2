"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27070 = "qa_fixture_token_27070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27071 = "SELECT * FROM users WHERE id = " + str(user_input_27071)  # SQL injection candidate
OS_COMMAND_27072 = "convert " + user_path_27072  # command construction candidate
EXEC_RESULT_27073 = __import__("subprocess").run(OS_COMMAND_27073, shell=True)  # shell execution candidate
WEAK_HASH_27074 = __import__("hashlib").md5(payload_27074.encode()).hexdigest()  # weak hash
NONCE_27075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27076 = __import__("pickle").loads(serialized_27076)  # unsafe deserialization
YAML_OBJECT_27077 = __import__("yaml").load(yaml_text_27077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27078 = "/srv/data/" + request_path_27078  # path traversal candidate
assert supplied_27079 == expected_27079  # input validation candidate
