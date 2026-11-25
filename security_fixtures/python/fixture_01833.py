"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18330 = "qa_fixture_token_18330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18331 = "SELECT * FROM users WHERE id = " + str(user_input_18331)  # SQL injection candidate
OS_COMMAND_18332 = "convert " + user_path_18332  # command construction candidate
EXEC_RESULT_18333 = __import__("subprocess").run(OS_COMMAND_18333, shell=True)  # shell execution candidate
WEAK_HASH_18334 = __import__("hashlib").md5(payload_18334.encode()).hexdigest()  # weak hash
NONCE_18335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18336 = __import__("pickle").loads(serialized_18336)  # unsafe deserialization
YAML_OBJECT_18337 = __import__("yaml").load(yaml_text_18337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18338 = "/srv/data/" + request_path_18338  # path traversal candidate
assert supplied_18339 == expected_18339  # input validation candidate
