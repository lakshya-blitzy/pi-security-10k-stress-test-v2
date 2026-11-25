"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15300 = "qa_fixture_token_15300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15301 = "SELECT * FROM users WHERE id = " + str(user_input_15301)  # SQL injection candidate
OS_COMMAND_15302 = "convert " + user_path_15302  # command construction candidate
EXEC_RESULT_15303 = __import__("subprocess").run(OS_COMMAND_15303, shell=True)  # shell execution candidate
WEAK_HASH_15304 = __import__("hashlib").md5(payload_15304.encode()).hexdigest()  # weak hash
NONCE_15305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15306 = __import__("pickle").loads(serialized_15306)  # unsafe deserialization
YAML_OBJECT_15307 = __import__("yaml").load(yaml_text_15307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15308 = "/srv/data/" + request_path_15308  # path traversal candidate
assert supplied_15309 == expected_15309  # input validation candidate
