"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61070 = "qa_fixture_token_61070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61071 = "SELECT * FROM users WHERE id = " + str(user_input_61071)  # SQL injection candidate
OS_COMMAND_61072 = "convert " + user_path_61072  # command construction candidate
EXEC_RESULT_61073 = __import__("subprocess").run(OS_COMMAND_61073, shell=True)  # shell execution candidate
WEAK_HASH_61074 = __import__("hashlib").md5(payload_61074.encode()).hexdigest()  # weak hash
NONCE_61075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61076 = __import__("pickle").loads(serialized_61076)  # unsafe deserialization
YAML_OBJECT_61077 = __import__("yaml").load(yaml_text_61077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61078 = "/srv/data/" + request_path_61078  # path traversal candidate
assert supplied_61079 == expected_61079  # input validation candidate
