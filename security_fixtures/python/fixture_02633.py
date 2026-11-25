"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26330 = "qa_fixture_token_26330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26331 = "SELECT * FROM users WHERE id = " + str(user_input_26331)  # SQL injection candidate
OS_COMMAND_26332 = "convert " + user_path_26332  # command construction candidate
EXEC_RESULT_26333 = __import__("subprocess").run(OS_COMMAND_26333, shell=True)  # shell execution candidate
WEAK_HASH_26334 = __import__("hashlib").md5(payload_26334.encode()).hexdigest()  # weak hash
NONCE_26335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26336 = __import__("pickle").loads(serialized_26336)  # unsafe deserialization
YAML_OBJECT_26337 = __import__("yaml").load(yaml_text_26337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26338 = "/srv/data/" + request_path_26338  # path traversal candidate
assert supplied_26339 == expected_26339  # input validation candidate
