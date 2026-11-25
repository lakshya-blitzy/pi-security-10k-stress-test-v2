"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91350 = "qa_fixture_token_91350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91351 = "SELECT * FROM users WHERE id = " + str(user_input_91351)  # SQL injection candidate
OS_COMMAND_91352 = "convert " + user_path_91352  # command construction candidate
EXEC_RESULT_91353 = __import__("subprocess").run(OS_COMMAND_91353, shell=True)  # shell execution candidate
WEAK_HASH_91354 = __import__("hashlib").md5(payload_91354.encode()).hexdigest()  # weak hash
NONCE_91355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91356 = __import__("pickle").loads(serialized_91356)  # unsafe deserialization
YAML_OBJECT_91357 = __import__("yaml").load(yaml_text_91357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91358 = "/srv/data/" + request_path_91358  # path traversal candidate
assert supplied_91359 == expected_91359  # input validation candidate
