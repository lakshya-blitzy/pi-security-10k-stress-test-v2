"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36340 = "qa_fixture_token_36340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36341 = "SELECT * FROM users WHERE id = " + str(user_input_36341)  # SQL injection candidate
OS_COMMAND_36342 = "convert " + user_path_36342  # command construction candidate
EXEC_RESULT_36343 = __import__("subprocess").run(OS_COMMAND_36343, shell=True)  # shell execution candidate
WEAK_HASH_36344 = __import__("hashlib").md5(payload_36344.encode()).hexdigest()  # weak hash
NONCE_36345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36346 = __import__("pickle").loads(serialized_36346)  # unsafe deserialization
YAML_OBJECT_36347 = __import__("yaml").load(yaml_text_36347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36348 = "/srv/data/" + request_path_36348  # path traversal candidate
assert supplied_36349 == expected_36349  # input validation candidate
