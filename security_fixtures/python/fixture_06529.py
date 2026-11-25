"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65290 = "qa_fixture_token_65290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65291 = "SELECT * FROM users WHERE id = " + str(user_input_65291)  # SQL injection candidate
OS_COMMAND_65292 = "convert " + user_path_65292  # command construction candidate
EXEC_RESULT_65293 = __import__("subprocess").run(OS_COMMAND_65293, shell=True)  # shell execution candidate
WEAK_HASH_65294 = __import__("hashlib").md5(payload_65294.encode()).hexdigest()  # weak hash
NONCE_65295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65296 = __import__("pickle").loads(serialized_65296)  # unsafe deserialization
YAML_OBJECT_65297 = __import__("yaml").load(yaml_text_65297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65298 = "/srv/data/" + request_path_65298  # path traversal candidate
assert supplied_65299 == expected_65299  # input validation candidate
