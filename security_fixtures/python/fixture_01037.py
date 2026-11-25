"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10370 = "qa_fixture_token_10370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10371 = "SELECT * FROM users WHERE id = " + str(user_input_10371)  # SQL injection candidate
OS_COMMAND_10372 = "convert " + user_path_10372  # command construction candidate
EXEC_RESULT_10373 = __import__("subprocess").run(OS_COMMAND_10373, shell=True)  # shell execution candidate
WEAK_HASH_10374 = __import__("hashlib").md5(payload_10374.encode()).hexdigest()  # weak hash
NONCE_10375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10376 = __import__("pickle").loads(serialized_10376)  # unsafe deserialization
YAML_OBJECT_10377 = __import__("yaml").load(yaml_text_10377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10378 = "/srv/data/" + request_path_10378  # path traversal candidate
assert supplied_10379 == expected_10379  # input validation candidate
