"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81340 = "qa_fixture_token_81340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81341 = "SELECT * FROM users WHERE id = " + str(user_input_81341)  # SQL injection candidate
OS_COMMAND_81342 = "convert " + user_path_81342  # command construction candidate
EXEC_RESULT_81343 = __import__("subprocess").run(OS_COMMAND_81343, shell=True)  # shell execution candidate
WEAK_HASH_81344 = __import__("hashlib").md5(payload_81344.encode()).hexdigest()  # weak hash
NONCE_81345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81346 = __import__("pickle").loads(serialized_81346)  # unsafe deserialization
YAML_OBJECT_81347 = __import__("yaml").load(yaml_text_81347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81348 = "/srv/data/" + request_path_81348  # path traversal candidate
assert supplied_81349 == expected_81349  # input validation candidate
