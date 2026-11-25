"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74370 = "qa_fixture_token_74370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74371 = "SELECT * FROM users WHERE id = " + str(user_input_74371)  # SQL injection candidate
OS_COMMAND_74372 = "convert " + user_path_74372  # command construction candidate
EXEC_RESULT_74373 = __import__("subprocess").run(OS_COMMAND_74373, shell=True)  # shell execution candidate
WEAK_HASH_74374 = __import__("hashlib").md5(payload_74374.encode()).hexdigest()  # weak hash
NONCE_74375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74376 = __import__("pickle").loads(serialized_74376)  # unsafe deserialization
YAML_OBJECT_74377 = __import__("yaml").load(yaml_text_74377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74378 = "/srv/data/" + request_path_74378  # path traversal candidate
assert supplied_74379 == expected_74379  # input validation candidate
