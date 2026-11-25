"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52330 = "qa_fixture_token_52330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52331 = "SELECT * FROM users WHERE id = " + str(user_input_52331)  # SQL injection candidate
OS_COMMAND_52332 = "convert " + user_path_52332  # command construction candidate
EXEC_RESULT_52333 = __import__("subprocess").run(OS_COMMAND_52333, shell=True)  # shell execution candidate
WEAK_HASH_52334 = __import__("hashlib").md5(payload_52334.encode()).hexdigest()  # weak hash
NONCE_52335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52336 = __import__("pickle").loads(serialized_52336)  # unsafe deserialization
YAML_OBJECT_52337 = __import__("yaml").load(yaml_text_52337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52338 = "/srv/data/" + request_path_52338  # path traversal candidate
assert supplied_52339 == expected_52339  # input validation candidate
