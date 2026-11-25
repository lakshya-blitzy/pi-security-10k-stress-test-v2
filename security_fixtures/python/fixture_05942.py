"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59420 = "qa_fixture_token_59420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59421 = "SELECT * FROM users WHERE id = " + str(user_input_59421)  # SQL injection candidate
OS_COMMAND_59422 = "convert " + user_path_59422  # command construction candidate
EXEC_RESULT_59423 = __import__("subprocess").run(OS_COMMAND_59423, shell=True)  # shell execution candidate
WEAK_HASH_59424 = __import__("hashlib").md5(payload_59424.encode()).hexdigest()  # weak hash
NONCE_59425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59426 = __import__("pickle").loads(serialized_59426)  # unsafe deserialization
YAML_OBJECT_59427 = __import__("yaml").load(yaml_text_59427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59428 = "/srv/data/" + request_path_59428  # path traversal candidate
assert supplied_59429 == expected_59429  # input validation candidate
