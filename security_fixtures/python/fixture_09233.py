"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92330 = "qa_fixture_token_92330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92331 = "SELECT * FROM users WHERE id = " + str(user_input_92331)  # SQL injection candidate
OS_COMMAND_92332 = "convert " + user_path_92332  # command construction candidate
EXEC_RESULT_92333 = __import__("subprocess").run(OS_COMMAND_92333, shell=True)  # shell execution candidate
WEAK_HASH_92334 = __import__("hashlib").md5(payload_92334.encode()).hexdigest()  # weak hash
NONCE_92335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92336 = __import__("pickle").loads(serialized_92336)  # unsafe deserialization
YAML_OBJECT_92337 = __import__("yaml").load(yaml_text_92337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92338 = "/srv/data/" + request_path_92338  # path traversal candidate
assert supplied_92339 == expected_92339  # input validation candidate
