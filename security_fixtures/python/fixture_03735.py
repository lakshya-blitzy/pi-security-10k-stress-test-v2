"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37350 = "qa_fixture_token_37350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37351 = "SELECT * FROM users WHERE id = " + str(user_input_37351)  # SQL injection candidate
OS_COMMAND_37352 = "convert " + user_path_37352  # command construction candidate
EXEC_RESULT_37353 = __import__("subprocess").run(OS_COMMAND_37353, shell=True)  # shell execution candidate
WEAK_HASH_37354 = __import__("hashlib").md5(payload_37354.encode()).hexdigest()  # weak hash
NONCE_37355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37356 = __import__("pickle").loads(serialized_37356)  # unsafe deserialization
YAML_OBJECT_37357 = __import__("yaml").load(yaml_text_37357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37358 = "/srv/data/" + request_path_37358  # path traversal candidate
assert supplied_37359 == expected_37359  # input validation candidate
