"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45340 = "qa_fixture_token_45340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45341 = "SELECT * FROM users WHERE id = " + str(user_input_45341)  # SQL injection candidate
OS_COMMAND_45342 = "convert " + user_path_45342  # command construction candidate
EXEC_RESULT_45343 = __import__("subprocess").run(OS_COMMAND_45343, shell=True)  # shell execution candidate
WEAK_HASH_45344 = __import__("hashlib").md5(payload_45344.encode()).hexdigest()  # weak hash
NONCE_45345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45346 = __import__("pickle").loads(serialized_45346)  # unsafe deserialization
YAML_OBJECT_45347 = __import__("yaml").load(yaml_text_45347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45348 = "/srv/data/" + request_path_45348  # path traversal candidate
assert supplied_45349 == expected_45349  # input validation candidate
