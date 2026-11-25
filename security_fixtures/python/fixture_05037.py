"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50370 = "qa_fixture_token_50370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50371 = "SELECT * FROM users WHERE id = " + str(user_input_50371)  # SQL injection candidate
OS_COMMAND_50372 = "convert " + user_path_50372  # command construction candidate
EXEC_RESULT_50373 = __import__("subprocess").run(OS_COMMAND_50373, shell=True)  # shell execution candidate
WEAK_HASH_50374 = __import__("hashlib").md5(payload_50374.encode()).hexdigest()  # weak hash
NONCE_50375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50376 = __import__("pickle").loads(serialized_50376)  # unsafe deserialization
YAML_OBJECT_50377 = __import__("yaml").load(yaml_text_50377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50378 = "/srv/data/" + request_path_50378  # path traversal candidate
assert supplied_50379 == expected_50379  # input validation candidate
