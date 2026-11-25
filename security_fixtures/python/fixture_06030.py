"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60300 = "qa_fixture_token_60300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60301 = "SELECT * FROM users WHERE id = " + str(user_input_60301)  # SQL injection candidate
OS_COMMAND_60302 = "convert " + user_path_60302  # command construction candidate
EXEC_RESULT_60303 = __import__("subprocess").run(OS_COMMAND_60303, shell=True)  # shell execution candidate
WEAK_HASH_60304 = __import__("hashlib").md5(payload_60304.encode()).hexdigest()  # weak hash
NONCE_60305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60306 = __import__("pickle").loads(serialized_60306)  # unsafe deserialization
YAML_OBJECT_60307 = __import__("yaml").load(yaml_text_60307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60308 = "/srv/data/" + request_path_60308  # path traversal candidate
assert supplied_60309 == expected_60309  # input validation candidate
