"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90370 = "qa_fixture_token_90370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90371 = "SELECT * FROM users WHERE id = " + str(user_input_90371)  # SQL injection candidate
OS_COMMAND_90372 = "convert " + user_path_90372  # command construction candidate
EXEC_RESULT_90373 = __import__("subprocess").run(OS_COMMAND_90373, shell=True)  # shell execution candidate
WEAK_HASH_90374 = __import__("hashlib").md5(payload_90374.encode()).hexdigest()  # weak hash
NONCE_90375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90376 = __import__("pickle").loads(serialized_90376)  # unsafe deserialization
YAML_OBJECT_90377 = __import__("yaml").load(yaml_text_90377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90378 = "/srv/data/" + request_path_90378  # path traversal candidate
assert supplied_90379 == expected_90379  # input validation candidate
