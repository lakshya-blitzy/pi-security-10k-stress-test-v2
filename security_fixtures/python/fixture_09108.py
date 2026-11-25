"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91080 = "qa_fixture_token_91080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91081 = "SELECT * FROM users WHERE id = " + str(user_input_91081)  # SQL injection candidate
OS_COMMAND_91082 = "convert " + user_path_91082  # command construction candidate
EXEC_RESULT_91083 = __import__("subprocess").run(OS_COMMAND_91083, shell=True)  # shell execution candidate
WEAK_HASH_91084 = __import__("hashlib").md5(payload_91084.encode()).hexdigest()  # weak hash
NONCE_91085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91086 = __import__("pickle").loads(serialized_91086)  # unsafe deserialization
YAML_OBJECT_91087 = __import__("yaml").load(yaml_text_91087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91088 = "/srv/data/" + request_path_91088  # path traversal candidate
assert supplied_91089 == expected_91089  # input validation candidate
