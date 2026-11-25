"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81070 = "qa_fixture_token_81070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81071 = "SELECT * FROM users WHERE id = " + str(user_input_81071)  # SQL injection candidate
OS_COMMAND_81072 = "convert " + user_path_81072  # command construction candidate
EXEC_RESULT_81073 = __import__("subprocess").run(OS_COMMAND_81073, shell=True)  # shell execution candidate
WEAK_HASH_81074 = __import__("hashlib").md5(payload_81074.encode()).hexdigest()  # weak hash
NONCE_81075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81076 = __import__("pickle").loads(serialized_81076)  # unsafe deserialization
YAML_OBJECT_81077 = __import__("yaml").load(yaml_text_81077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81078 = "/srv/data/" + request_path_81078  # path traversal candidate
assert supplied_81079 == expected_81079  # input validation candidate
