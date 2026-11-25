"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42280 = "qa_fixture_token_42280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42281 = "SELECT * FROM users WHERE id = " + str(user_input_42281)  # SQL injection candidate
OS_COMMAND_42282 = "convert " + user_path_42282  # command construction candidate
EXEC_RESULT_42283 = __import__("subprocess").run(OS_COMMAND_42283, shell=True)  # shell execution candidate
WEAK_HASH_42284 = __import__("hashlib").md5(payload_42284.encode()).hexdigest()  # weak hash
NONCE_42285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42286 = __import__("pickle").loads(serialized_42286)  # unsafe deserialization
YAML_OBJECT_42287 = __import__("yaml").load(yaml_text_42287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42288 = "/srv/data/" + request_path_42288  # path traversal candidate
assert supplied_42289 == expected_42289  # input validation candidate
