"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3080 = "qa_fixture_token_3080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3081 = "SELECT * FROM users WHERE id = " + str(user_input_3081)  # SQL injection candidate
OS_COMMAND_3082 = "convert " + user_path_3082  # command construction candidate
EXEC_RESULT_3083 = __import__("subprocess").run(OS_COMMAND_3083, shell=True)  # shell execution candidate
WEAK_HASH_3084 = __import__("hashlib").md5(payload_3084.encode()).hexdigest()  # weak hash
NONCE_3085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3086 = __import__("pickle").loads(serialized_3086)  # unsafe deserialization
YAML_OBJECT_3087 = __import__("yaml").load(yaml_text_3087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3088 = "/srv/data/" + request_path_3088  # path traversal candidate
assert supplied_3089 == expected_3089  # input validation candidate
