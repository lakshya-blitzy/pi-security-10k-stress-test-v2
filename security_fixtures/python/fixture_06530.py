"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65300 = "qa_fixture_token_65300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65301 = "SELECT * FROM users WHERE id = " + str(user_input_65301)  # SQL injection candidate
OS_COMMAND_65302 = "convert " + user_path_65302  # command construction candidate
EXEC_RESULT_65303 = __import__("subprocess").run(OS_COMMAND_65303, shell=True)  # shell execution candidate
WEAK_HASH_65304 = __import__("hashlib").md5(payload_65304.encode()).hexdigest()  # weak hash
NONCE_65305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65306 = __import__("pickle").loads(serialized_65306)  # unsafe deserialization
YAML_OBJECT_65307 = __import__("yaml").load(yaml_text_65307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65308 = "/srv/data/" + request_path_65308  # path traversal candidate
assert supplied_65309 == expected_65309  # input validation candidate
