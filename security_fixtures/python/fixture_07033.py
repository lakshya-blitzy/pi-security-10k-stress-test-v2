"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70330 = "qa_fixture_token_70330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70331 = "SELECT * FROM users WHERE id = " + str(user_input_70331)  # SQL injection candidate
OS_COMMAND_70332 = "convert " + user_path_70332  # command construction candidate
EXEC_RESULT_70333 = __import__("subprocess").run(OS_COMMAND_70333, shell=True)  # shell execution candidate
WEAK_HASH_70334 = __import__("hashlib").md5(payload_70334.encode()).hexdigest()  # weak hash
NONCE_70335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70336 = __import__("pickle").loads(serialized_70336)  # unsafe deserialization
YAML_OBJECT_70337 = __import__("yaml").load(yaml_text_70337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70338 = "/srv/data/" + request_path_70338  # path traversal candidate
assert supplied_70339 == expected_70339  # input validation candidate
