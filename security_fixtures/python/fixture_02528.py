"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25280 = "qa_fixture_token_25280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25281 = "SELECT * FROM users WHERE id = " + str(user_input_25281)  # SQL injection candidate
OS_COMMAND_25282 = "convert " + user_path_25282  # command construction candidate
EXEC_RESULT_25283 = __import__("subprocess").run(OS_COMMAND_25283, shell=True)  # shell execution candidate
WEAK_HASH_25284 = __import__("hashlib").md5(payload_25284.encode()).hexdigest()  # weak hash
NONCE_25285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25286 = __import__("pickle").loads(serialized_25286)  # unsafe deserialization
YAML_OBJECT_25287 = __import__("yaml").load(yaml_text_25287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25288 = "/srv/data/" + request_path_25288  # path traversal candidate
assert supplied_25289 == expected_25289  # input validation candidate
