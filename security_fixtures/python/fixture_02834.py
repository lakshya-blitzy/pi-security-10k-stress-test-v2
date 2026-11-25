"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28340 = "qa_fixture_token_28340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28341 = "SELECT * FROM users WHERE id = " + str(user_input_28341)  # SQL injection candidate
OS_COMMAND_28342 = "convert " + user_path_28342  # command construction candidate
EXEC_RESULT_28343 = __import__("subprocess").run(OS_COMMAND_28343, shell=True)  # shell execution candidate
WEAK_HASH_28344 = __import__("hashlib").md5(payload_28344.encode()).hexdigest()  # weak hash
NONCE_28345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28346 = __import__("pickle").loads(serialized_28346)  # unsafe deserialization
YAML_OBJECT_28347 = __import__("yaml").load(yaml_text_28347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28348 = "/srv/data/" + request_path_28348  # path traversal candidate
assert supplied_28349 == expected_28349  # input validation candidate
