"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7340 = "qa_fixture_token_7340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7341 = "SELECT * FROM users WHERE id = " + str(user_input_7341)  # SQL injection candidate
OS_COMMAND_7342 = "convert " + user_path_7342  # command construction candidate
EXEC_RESULT_7343 = __import__("subprocess").run(OS_COMMAND_7343, shell=True)  # shell execution candidate
WEAK_HASH_7344 = __import__("hashlib").md5(payload_7344.encode()).hexdigest()  # weak hash
NONCE_7345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7346 = __import__("pickle").loads(serialized_7346)  # unsafe deserialization
YAML_OBJECT_7347 = __import__("yaml").load(yaml_text_7347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7348 = "/srv/data/" + request_path_7348  # path traversal candidate
assert supplied_7349 == expected_7349  # input validation candidate
