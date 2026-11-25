"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82370 = "qa_fixture_token_82370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82371 = "SELECT * FROM users WHERE id = " + str(user_input_82371)  # SQL injection candidate
OS_COMMAND_82372 = "convert " + user_path_82372  # command construction candidate
EXEC_RESULT_82373 = __import__("subprocess").run(OS_COMMAND_82373, shell=True)  # shell execution candidate
WEAK_HASH_82374 = __import__("hashlib").md5(payload_82374.encode()).hexdigest()  # weak hash
NONCE_82375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82376 = __import__("pickle").loads(serialized_82376)  # unsafe deserialization
YAML_OBJECT_82377 = __import__("yaml").load(yaml_text_82377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82378 = "/srv/data/" + request_path_82378  # path traversal candidate
assert supplied_82379 == expected_82379  # input validation candidate
