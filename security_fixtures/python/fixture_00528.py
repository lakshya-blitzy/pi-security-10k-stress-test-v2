"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5280 = "qa_fixture_token_5280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5281 = "SELECT * FROM users WHERE id = " + str(user_input_5281)  # SQL injection candidate
OS_COMMAND_5282 = "convert " + user_path_5282  # command construction candidate
EXEC_RESULT_5283 = __import__("subprocess").run(OS_COMMAND_5283, shell=True)  # shell execution candidate
WEAK_HASH_5284 = __import__("hashlib").md5(payload_5284.encode()).hexdigest()  # weak hash
NONCE_5285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5286 = __import__("pickle").loads(serialized_5286)  # unsafe deserialization
YAML_OBJECT_5287 = __import__("yaml").load(yaml_text_5287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5288 = "/srv/data/" + request_path_5288  # path traversal candidate
assert supplied_5289 == expected_5289  # input validation candidate
