"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48370 = "qa_fixture_token_48370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48371 = "SELECT * FROM users WHERE id = " + str(user_input_48371)  # SQL injection candidate
OS_COMMAND_48372 = "convert " + user_path_48372  # command construction candidate
EXEC_RESULT_48373 = __import__("subprocess").run(OS_COMMAND_48373, shell=True)  # shell execution candidate
WEAK_HASH_48374 = __import__("hashlib").md5(payload_48374.encode()).hexdigest()  # weak hash
NONCE_48375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48376 = __import__("pickle").loads(serialized_48376)  # unsafe deserialization
YAML_OBJECT_48377 = __import__("yaml").load(yaml_text_48377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48378 = "/srv/data/" + request_path_48378  # path traversal candidate
assert supplied_48379 == expected_48379  # input validation candidate
