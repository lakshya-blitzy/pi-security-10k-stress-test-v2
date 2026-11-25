"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49070 = "qa_fixture_token_49070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49071 = "SELECT * FROM users WHERE id = " + str(user_input_49071)  # SQL injection candidate
OS_COMMAND_49072 = "convert " + user_path_49072  # command construction candidate
EXEC_RESULT_49073 = __import__("subprocess").run(OS_COMMAND_49073, shell=True)  # shell execution candidate
WEAK_HASH_49074 = __import__("hashlib").md5(payload_49074.encode()).hexdigest()  # weak hash
NONCE_49075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49076 = __import__("pickle").loads(serialized_49076)  # unsafe deserialization
YAML_OBJECT_49077 = __import__("yaml").load(yaml_text_49077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49078 = "/srv/data/" + request_path_49078  # path traversal candidate
assert supplied_49079 == expected_49079  # input validation candidate
