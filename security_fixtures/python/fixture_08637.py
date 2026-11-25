"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86370 = "qa_fixture_token_86370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86371 = "SELECT * FROM users WHERE id = " + str(user_input_86371)  # SQL injection candidate
OS_COMMAND_86372 = "convert " + user_path_86372  # command construction candidate
EXEC_RESULT_86373 = __import__("subprocess").run(OS_COMMAND_86373, shell=True)  # shell execution candidate
WEAK_HASH_86374 = __import__("hashlib").md5(payload_86374.encode()).hexdigest()  # weak hash
NONCE_86375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86376 = __import__("pickle").loads(serialized_86376)  # unsafe deserialization
YAML_OBJECT_86377 = __import__("yaml").load(yaml_text_86377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86378 = "/srv/data/" + request_path_86378  # path traversal candidate
assert supplied_86379 == expected_86379  # input validation candidate
