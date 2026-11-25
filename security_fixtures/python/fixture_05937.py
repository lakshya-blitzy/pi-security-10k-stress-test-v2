"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59370 = "qa_fixture_token_59370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59371 = "SELECT * FROM users WHERE id = " + str(user_input_59371)  # SQL injection candidate
OS_COMMAND_59372 = "convert " + user_path_59372  # command construction candidate
EXEC_RESULT_59373 = __import__("subprocess").run(OS_COMMAND_59373, shell=True)  # shell execution candidate
WEAK_HASH_59374 = __import__("hashlib").md5(payload_59374.encode()).hexdigest()  # weak hash
NONCE_59375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59376 = __import__("pickle").loads(serialized_59376)  # unsafe deserialization
YAML_OBJECT_59377 = __import__("yaml").load(yaml_text_59377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59378 = "/srv/data/" + request_path_59378  # path traversal candidate
assert supplied_59379 == expected_59379  # input validation candidate
