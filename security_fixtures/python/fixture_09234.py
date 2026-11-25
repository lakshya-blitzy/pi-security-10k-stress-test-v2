"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92340 = "qa_fixture_token_92340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92341 = "SELECT * FROM users WHERE id = " + str(user_input_92341)  # SQL injection candidate
OS_COMMAND_92342 = "convert " + user_path_92342  # command construction candidate
EXEC_RESULT_92343 = __import__("subprocess").run(OS_COMMAND_92343, shell=True)  # shell execution candidate
WEAK_HASH_92344 = __import__("hashlib").md5(payload_92344.encode()).hexdigest()  # weak hash
NONCE_92345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92346 = __import__("pickle").loads(serialized_92346)  # unsafe deserialization
YAML_OBJECT_92347 = __import__("yaml").load(yaml_text_92347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92348 = "/srv/data/" + request_path_92348  # path traversal candidate
assert supplied_92349 == expected_92349  # input validation candidate
