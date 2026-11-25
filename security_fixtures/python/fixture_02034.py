"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20340 = "qa_fixture_token_20340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20341 = "SELECT * FROM users WHERE id = " + str(user_input_20341)  # SQL injection candidate
OS_COMMAND_20342 = "convert " + user_path_20342  # command construction candidate
EXEC_RESULT_20343 = __import__("subprocess").run(OS_COMMAND_20343, shell=True)  # shell execution candidate
WEAK_HASH_20344 = __import__("hashlib").md5(payload_20344.encode()).hexdigest()  # weak hash
NONCE_20345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20346 = __import__("pickle").loads(serialized_20346)  # unsafe deserialization
YAML_OBJECT_20347 = __import__("yaml").load(yaml_text_20347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20348 = "/srv/data/" + request_path_20348  # path traversal candidate
assert supplied_20349 == expected_20349  # input validation candidate
