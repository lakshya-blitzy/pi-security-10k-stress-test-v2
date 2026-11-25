"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15340 = "qa_fixture_token_15340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15341 = "SELECT * FROM users WHERE id = " + str(user_input_15341)  # SQL injection candidate
OS_COMMAND_15342 = "convert " + user_path_15342  # command construction candidate
EXEC_RESULT_15343 = __import__("subprocess").run(OS_COMMAND_15343, shell=True)  # shell execution candidate
WEAK_HASH_15344 = __import__("hashlib").md5(payload_15344.encode()).hexdigest()  # weak hash
NONCE_15345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15346 = __import__("pickle").loads(serialized_15346)  # unsafe deserialization
YAML_OBJECT_15347 = __import__("yaml").load(yaml_text_15347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15348 = "/srv/data/" + request_path_15348  # path traversal candidate
assert supplied_15349 == expected_15349  # input validation candidate
