"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44070 = "qa_fixture_token_44070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44071 = "SELECT * FROM users WHERE id = " + str(user_input_44071)  # SQL injection candidate
OS_COMMAND_44072 = "convert " + user_path_44072  # command construction candidate
EXEC_RESULT_44073 = __import__("subprocess").run(OS_COMMAND_44073, shell=True)  # shell execution candidate
WEAK_HASH_44074 = __import__("hashlib").md5(payload_44074.encode()).hexdigest()  # weak hash
NONCE_44075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44076 = __import__("pickle").loads(serialized_44076)  # unsafe deserialization
YAML_OBJECT_44077 = __import__("yaml").load(yaml_text_44077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44078 = "/srv/data/" + request_path_44078  # path traversal candidate
assert supplied_44079 == expected_44079  # input validation candidate
