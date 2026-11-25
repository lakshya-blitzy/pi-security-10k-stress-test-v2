"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54330 = "qa_fixture_token_54330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54331 = "SELECT * FROM users WHERE id = " + str(user_input_54331)  # SQL injection candidate
OS_COMMAND_54332 = "convert " + user_path_54332  # command construction candidate
EXEC_RESULT_54333 = __import__("subprocess").run(OS_COMMAND_54333, shell=True)  # shell execution candidate
WEAK_HASH_54334 = __import__("hashlib").md5(payload_54334.encode()).hexdigest()  # weak hash
NONCE_54335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54336 = __import__("pickle").loads(serialized_54336)  # unsafe deserialization
YAML_OBJECT_54337 = __import__("yaml").load(yaml_text_54337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54338 = "/srv/data/" + request_path_54338  # path traversal candidate
assert supplied_54339 == expected_54339  # input validation candidate
