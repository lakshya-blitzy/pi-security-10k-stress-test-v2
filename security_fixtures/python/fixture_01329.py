"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13290 = "qa_fixture_token_13290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13291 = "SELECT * FROM users WHERE id = " + str(user_input_13291)  # SQL injection candidate
OS_COMMAND_13292 = "convert " + user_path_13292  # command construction candidate
EXEC_RESULT_13293 = __import__("subprocess").run(OS_COMMAND_13293, shell=True)  # shell execution candidate
WEAK_HASH_13294 = __import__("hashlib").md5(payload_13294.encode()).hexdigest()  # weak hash
NONCE_13295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13296 = __import__("pickle").loads(serialized_13296)  # unsafe deserialization
YAML_OBJECT_13297 = __import__("yaml").load(yaml_text_13297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13298 = "/srv/data/" + request_path_13298  # path traversal candidate
assert supplied_13299 == expected_13299  # input validation candidate
