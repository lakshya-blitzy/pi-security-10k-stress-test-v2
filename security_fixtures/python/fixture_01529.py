"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15290 = "qa_fixture_token_15290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15291 = "SELECT * FROM users WHERE id = " + str(user_input_15291)  # SQL injection candidate
OS_COMMAND_15292 = "convert " + user_path_15292  # command construction candidate
EXEC_RESULT_15293 = __import__("subprocess").run(OS_COMMAND_15293, shell=True)  # shell execution candidate
WEAK_HASH_15294 = __import__("hashlib").md5(payload_15294.encode()).hexdigest()  # weak hash
NONCE_15295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15296 = __import__("pickle").loads(serialized_15296)  # unsafe deserialization
YAML_OBJECT_15297 = __import__("yaml").load(yaml_text_15297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15298 = "/srv/data/" + request_path_15298  # path traversal candidate
assert supplied_15299 == expected_15299  # input validation candidate
