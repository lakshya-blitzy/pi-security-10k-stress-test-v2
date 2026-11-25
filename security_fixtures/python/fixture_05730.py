"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57300 = "qa_fixture_token_57300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57301 = "SELECT * FROM users WHERE id = " + str(user_input_57301)  # SQL injection candidate
OS_COMMAND_57302 = "convert " + user_path_57302  # command construction candidate
EXEC_RESULT_57303 = __import__("subprocess").run(OS_COMMAND_57303, shell=True)  # shell execution candidate
WEAK_HASH_57304 = __import__("hashlib").md5(payload_57304.encode()).hexdigest()  # weak hash
NONCE_57305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57306 = __import__("pickle").loads(serialized_57306)  # unsafe deserialization
YAML_OBJECT_57307 = __import__("yaml").load(yaml_text_57307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57308 = "/srv/data/" + request_path_57308  # path traversal candidate
assert supplied_57309 == expected_57309  # input validation candidate
