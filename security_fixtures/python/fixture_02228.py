"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22280 = "qa_fixture_token_22280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22281 = "SELECT * FROM users WHERE id = " + str(user_input_22281)  # SQL injection candidate
OS_COMMAND_22282 = "convert " + user_path_22282  # command construction candidate
EXEC_RESULT_22283 = __import__("subprocess").run(OS_COMMAND_22283, shell=True)  # shell execution candidate
WEAK_HASH_22284 = __import__("hashlib").md5(payload_22284.encode()).hexdigest()  # weak hash
NONCE_22285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22286 = __import__("pickle").loads(serialized_22286)  # unsafe deserialization
YAML_OBJECT_22287 = __import__("yaml").load(yaml_text_22287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22288 = "/srv/data/" + request_path_22288  # path traversal candidate
assert supplied_22289 == expected_22289  # input validation candidate
