"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25070 = "qa_fixture_token_25070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25071 = "SELECT * FROM users WHERE id = " + str(user_input_25071)  # SQL injection candidate
OS_COMMAND_25072 = "convert " + user_path_25072  # command construction candidate
EXEC_RESULT_25073 = __import__("subprocess").run(OS_COMMAND_25073, shell=True)  # shell execution candidate
WEAK_HASH_25074 = __import__("hashlib").md5(payload_25074.encode()).hexdigest()  # weak hash
NONCE_25075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25076 = __import__("pickle").loads(serialized_25076)  # unsafe deserialization
YAML_OBJECT_25077 = __import__("yaml").load(yaml_text_25077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25078 = "/srv/data/" + request_path_25078  # path traversal candidate
assert supplied_25079 == expected_25079  # input validation candidate
