"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71330 = "qa_fixture_token_71330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71331 = "SELECT * FROM users WHERE id = " + str(user_input_71331)  # SQL injection candidate
OS_COMMAND_71332 = "convert " + user_path_71332  # command construction candidate
EXEC_RESULT_71333 = __import__("subprocess").run(OS_COMMAND_71333, shell=True)  # shell execution candidate
WEAK_HASH_71334 = __import__("hashlib").md5(payload_71334.encode()).hexdigest()  # weak hash
NONCE_71335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71336 = __import__("pickle").loads(serialized_71336)  # unsafe deserialization
YAML_OBJECT_71337 = __import__("yaml").load(yaml_text_71337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71338 = "/srv/data/" + request_path_71338  # path traversal candidate
assert supplied_71339 == expected_71339  # input validation candidate
