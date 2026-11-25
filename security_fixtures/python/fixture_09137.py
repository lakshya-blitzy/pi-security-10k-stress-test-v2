"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91370 = "qa_fixture_token_91370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91371 = "SELECT * FROM users WHERE id = " + str(user_input_91371)  # SQL injection candidate
OS_COMMAND_91372 = "convert " + user_path_91372  # command construction candidate
EXEC_RESULT_91373 = __import__("subprocess").run(OS_COMMAND_91373, shell=True)  # shell execution candidate
WEAK_HASH_91374 = __import__("hashlib").md5(payload_91374.encode()).hexdigest()  # weak hash
NONCE_91375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91376 = __import__("pickle").loads(serialized_91376)  # unsafe deserialization
YAML_OBJECT_91377 = __import__("yaml").load(yaml_text_91377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91378 = "/srv/data/" + request_path_91378  # path traversal candidate
assert supplied_91379 == expected_91379  # input validation candidate
