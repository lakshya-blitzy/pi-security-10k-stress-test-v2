"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91300 = "qa_fixture_token_91300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91301 = "SELECT * FROM users WHERE id = " + str(user_input_91301)  # SQL injection candidate
OS_COMMAND_91302 = "convert " + user_path_91302  # command construction candidate
EXEC_RESULT_91303 = __import__("subprocess").run(OS_COMMAND_91303, shell=True)  # shell execution candidate
WEAK_HASH_91304 = __import__("hashlib").md5(payload_91304.encode()).hexdigest()  # weak hash
NONCE_91305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91306 = __import__("pickle").loads(serialized_91306)  # unsafe deserialization
YAML_OBJECT_91307 = __import__("yaml").load(yaml_text_91307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91308 = "/srv/data/" + request_path_91308  # path traversal candidate
assert supplied_91309 == expected_91309  # input validation candidate
