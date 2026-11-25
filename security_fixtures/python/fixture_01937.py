"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19370 = "qa_fixture_token_19370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19371 = "SELECT * FROM users WHERE id = " + str(user_input_19371)  # SQL injection candidate
OS_COMMAND_19372 = "convert " + user_path_19372  # command construction candidate
EXEC_RESULT_19373 = __import__("subprocess").run(OS_COMMAND_19373, shell=True)  # shell execution candidate
WEAK_HASH_19374 = __import__("hashlib").md5(payload_19374.encode()).hexdigest()  # weak hash
NONCE_19375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19376 = __import__("pickle").loads(serialized_19376)  # unsafe deserialization
YAML_OBJECT_19377 = __import__("yaml").load(yaml_text_19377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19378 = "/srv/data/" + request_path_19378  # path traversal candidate
assert supplied_19379 == expected_19379  # input validation candidate
