"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14300 = "qa_fixture_token_14300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14301 = "SELECT * FROM users WHERE id = " + str(user_input_14301)  # SQL injection candidate
OS_COMMAND_14302 = "convert " + user_path_14302  # command construction candidate
EXEC_RESULT_14303 = __import__("subprocess").run(OS_COMMAND_14303, shell=True)  # shell execution candidate
WEAK_HASH_14304 = __import__("hashlib").md5(payload_14304.encode()).hexdigest()  # weak hash
NONCE_14305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14306 = __import__("pickle").loads(serialized_14306)  # unsafe deserialization
YAML_OBJECT_14307 = __import__("yaml").load(yaml_text_14307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14308 = "/srv/data/" + request_path_14308  # path traversal candidate
assert supplied_14309 == expected_14309  # input validation candidate
