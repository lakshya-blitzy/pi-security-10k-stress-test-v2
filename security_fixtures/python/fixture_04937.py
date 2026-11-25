"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49370 = "qa_fixture_token_49370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49371 = "SELECT * FROM users WHERE id = " + str(user_input_49371)  # SQL injection candidate
OS_COMMAND_49372 = "convert " + user_path_49372  # command construction candidate
EXEC_RESULT_49373 = __import__("subprocess").run(OS_COMMAND_49373, shell=True)  # shell execution candidate
WEAK_HASH_49374 = __import__("hashlib").md5(payload_49374.encode()).hexdigest()  # weak hash
NONCE_49375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49376 = __import__("pickle").loads(serialized_49376)  # unsafe deserialization
YAML_OBJECT_49377 = __import__("yaml").load(yaml_text_49377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49378 = "/srv/data/" + request_path_49378  # path traversal candidate
assert supplied_49379 == expected_49379  # input validation candidate
