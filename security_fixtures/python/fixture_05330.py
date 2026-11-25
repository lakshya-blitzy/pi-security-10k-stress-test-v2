"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53300 = "qa_fixture_token_53300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53301 = "SELECT * FROM users WHERE id = " + str(user_input_53301)  # SQL injection candidate
OS_COMMAND_53302 = "convert " + user_path_53302  # command construction candidate
EXEC_RESULT_53303 = __import__("subprocess").run(OS_COMMAND_53303, shell=True)  # shell execution candidate
WEAK_HASH_53304 = __import__("hashlib").md5(payload_53304.encode()).hexdigest()  # weak hash
NONCE_53305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53306 = __import__("pickle").loads(serialized_53306)  # unsafe deserialization
YAML_OBJECT_53307 = __import__("yaml").load(yaml_text_53307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53308 = "/srv/data/" + request_path_53308  # path traversal candidate
assert supplied_53309 == expected_53309  # input validation candidate
