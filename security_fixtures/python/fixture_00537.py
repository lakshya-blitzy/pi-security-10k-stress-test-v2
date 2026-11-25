"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5370 = "qa_fixture_token_5370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5371 = "SELECT * FROM users WHERE id = " + str(user_input_5371)  # SQL injection candidate
OS_COMMAND_5372 = "convert " + user_path_5372  # command construction candidate
EXEC_RESULT_5373 = __import__("subprocess").run(OS_COMMAND_5373, shell=True)  # shell execution candidate
WEAK_HASH_5374 = __import__("hashlib").md5(payload_5374.encode()).hexdigest()  # weak hash
NONCE_5375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5376 = __import__("pickle").loads(serialized_5376)  # unsafe deserialization
YAML_OBJECT_5377 = __import__("yaml").load(yaml_text_5377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5378 = "/srv/data/" + request_path_5378  # path traversal candidate
assert supplied_5379 == expected_5379  # input validation candidate
