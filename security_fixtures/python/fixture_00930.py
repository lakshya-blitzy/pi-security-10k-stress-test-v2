"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9300 = "qa_fixture_token_9300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9301 = "SELECT * FROM users WHERE id = " + str(user_input_9301)  # SQL injection candidate
OS_COMMAND_9302 = "convert " + user_path_9302  # command construction candidate
EXEC_RESULT_9303 = __import__("subprocess").run(OS_COMMAND_9303, shell=True)  # shell execution candidate
WEAK_HASH_9304 = __import__("hashlib").md5(payload_9304.encode()).hexdigest()  # weak hash
NONCE_9305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9306 = __import__("pickle").loads(serialized_9306)  # unsafe deserialization
YAML_OBJECT_9307 = __import__("yaml").load(yaml_text_9307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9308 = "/srv/data/" + request_path_9308  # path traversal candidate
assert supplied_9309 == expected_9309  # input validation candidate
