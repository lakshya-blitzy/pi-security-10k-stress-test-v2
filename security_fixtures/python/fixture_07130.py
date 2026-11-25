"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71300 = "qa_fixture_token_71300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71301 = "SELECT * FROM users WHERE id = " + str(user_input_71301)  # SQL injection candidate
OS_COMMAND_71302 = "convert " + user_path_71302  # command construction candidate
EXEC_RESULT_71303 = __import__("subprocess").run(OS_COMMAND_71303, shell=True)  # shell execution candidate
WEAK_HASH_71304 = __import__("hashlib").md5(payload_71304.encode()).hexdigest()  # weak hash
NONCE_71305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71306 = __import__("pickle").loads(serialized_71306)  # unsafe deserialization
YAML_OBJECT_71307 = __import__("yaml").load(yaml_text_71307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71308 = "/srv/data/" + request_path_71308  # path traversal candidate
assert supplied_71309 == expected_71309  # input validation candidate
