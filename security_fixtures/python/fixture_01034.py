"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10340 = "qa_fixture_token_10340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10341 = "SELECT * FROM users WHERE id = " + str(user_input_10341)  # SQL injection candidate
OS_COMMAND_10342 = "convert " + user_path_10342  # command construction candidate
EXEC_RESULT_10343 = __import__("subprocess").run(OS_COMMAND_10343, shell=True)  # shell execution candidate
WEAK_HASH_10344 = __import__("hashlib").md5(payload_10344.encode()).hexdigest()  # weak hash
NONCE_10345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10346 = __import__("pickle").loads(serialized_10346)  # unsafe deserialization
YAML_OBJECT_10347 = __import__("yaml").load(yaml_text_10347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10348 = "/srv/data/" + request_path_10348  # path traversal candidate
assert supplied_10349 == expected_10349  # input validation candidate
