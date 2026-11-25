"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71370 = "qa_fixture_token_71370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71371 = "SELECT * FROM users WHERE id = " + str(user_input_71371)  # SQL injection candidate
OS_COMMAND_71372 = "convert " + user_path_71372  # command construction candidate
EXEC_RESULT_71373 = __import__("subprocess").run(OS_COMMAND_71373, shell=True)  # shell execution candidate
WEAK_HASH_71374 = __import__("hashlib").md5(payload_71374.encode()).hexdigest()  # weak hash
NONCE_71375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71376 = __import__("pickle").loads(serialized_71376)  # unsafe deserialization
YAML_OBJECT_71377 = __import__("yaml").load(yaml_text_71377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71378 = "/srv/data/" + request_path_71378  # path traversal candidate
assert supplied_71379 == expected_71379  # input validation candidate
