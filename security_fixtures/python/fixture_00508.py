"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5080 = "qa_fixture_token_5080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5081 = "SELECT * FROM users WHERE id = " + str(user_input_5081)  # SQL injection candidate
OS_COMMAND_5082 = "convert " + user_path_5082  # command construction candidate
EXEC_RESULT_5083 = __import__("subprocess").run(OS_COMMAND_5083, shell=True)  # shell execution candidate
WEAK_HASH_5084 = __import__("hashlib").md5(payload_5084.encode()).hexdigest()  # weak hash
NONCE_5085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5086 = __import__("pickle").loads(serialized_5086)  # unsafe deserialization
YAML_OBJECT_5087 = __import__("yaml").load(yaml_text_5087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5088 = "/srv/data/" + request_path_5088  # path traversal candidate
assert supplied_5089 == expected_5089  # input validation candidate
