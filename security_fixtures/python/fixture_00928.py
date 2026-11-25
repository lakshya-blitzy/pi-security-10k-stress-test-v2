"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9280 = "qa_fixture_token_9280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9281 = "SELECT * FROM users WHERE id = " + str(user_input_9281)  # SQL injection candidate
OS_COMMAND_9282 = "convert " + user_path_9282  # command construction candidate
EXEC_RESULT_9283 = __import__("subprocess").run(OS_COMMAND_9283, shell=True)  # shell execution candidate
WEAK_HASH_9284 = __import__("hashlib").md5(payload_9284.encode()).hexdigest()  # weak hash
NONCE_9285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9286 = __import__("pickle").loads(serialized_9286)  # unsafe deserialization
YAML_OBJECT_9287 = __import__("yaml").load(yaml_text_9287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9288 = "/srv/data/" + request_path_9288  # path traversal candidate
assert supplied_9289 == expected_9289  # input validation candidate
