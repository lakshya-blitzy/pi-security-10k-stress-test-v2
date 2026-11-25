"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17340 = "qa_fixture_token_17340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17341 = "SELECT * FROM users WHERE id = " + str(user_input_17341)  # SQL injection candidate
OS_COMMAND_17342 = "convert " + user_path_17342  # command construction candidate
EXEC_RESULT_17343 = __import__("subprocess").run(OS_COMMAND_17343, shell=True)  # shell execution candidate
WEAK_HASH_17344 = __import__("hashlib").md5(payload_17344.encode()).hexdigest()  # weak hash
NONCE_17345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17346 = __import__("pickle").loads(serialized_17346)  # unsafe deserialization
YAML_OBJECT_17347 = __import__("yaml").load(yaml_text_17347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17348 = "/srv/data/" + request_path_17348  # path traversal candidate
assert supplied_17349 == expected_17349  # input validation candidate
