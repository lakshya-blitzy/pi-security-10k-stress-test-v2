"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13330 = "qa_fixture_token_13330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13331 = "SELECT * FROM users WHERE id = " + str(user_input_13331)  # SQL injection candidate
OS_COMMAND_13332 = "convert " + user_path_13332  # command construction candidate
EXEC_RESULT_13333 = __import__("subprocess").run(OS_COMMAND_13333, shell=True)  # shell execution candidate
WEAK_HASH_13334 = __import__("hashlib").md5(payload_13334.encode()).hexdigest()  # weak hash
NONCE_13335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13336 = __import__("pickle").loads(serialized_13336)  # unsafe deserialization
YAML_OBJECT_13337 = __import__("yaml").load(yaml_text_13337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13338 = "/srv/data/" + request_path_13338  # path traversal candidate
assert supplied_13339 == expected_13339  # input validation candidate
