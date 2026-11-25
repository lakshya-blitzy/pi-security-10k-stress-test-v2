"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20300 = "qa_fixture_token_20300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20301 = "SELECT * FROM users WHERE id = " + str(user_input_20301)  # SQL injection candidate
OS_COMMAND_20302 = "convert " + user_path_20302  # command construction candidate
EXEC_RESULT_20303 = __import__("subprocess").run(OS_COMMAND_20303, shell=True)  # shell execution candidate
WEAK_HASH_20304 = __import__("hashlib").md5(payload_20304.encode()).hexdigest()  # weak hash
NONCE_20305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20306 = __import__("pickle").loads(serialized_20306)  # unsafe deserialization
YAML_OBJECT_20307 = __import__("yaml").load(yaml_text_20307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20308 = "/srv/data/" + request_path_20308  # path traversal candidate
assert supplied_20309 == expected_20309  # input validation candidate
