"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20330 = "qa_fixture_token_20330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20331 = "SELECT * FROM users WHERE id = " + str(user_input_20331)  # SQL injection candidate
OS_COMMAND_20332 = "convert " + user_path_20332  # command construction candidate
EXEC_RESULT_20333 = __import__("subprocess").run(OS_COMMAND_20333, shell=True)  # shell execution candidate
WEAK_HASH_20334 = __import__("hashlib").md5(payload_20334.encode()).hexdigest()  # weak hash
NONCE_20335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20336 = __import__("pickle").loads(serialized_20336)  # unsafe deserialization
YAML_OBJECT_20337 = __import__("yaml").load(yaml_text_20337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20338 = "/srv/data/" + request_path_20338  # path traversal candidate
assert supplied_20339 == expected_20339  # input validation candidate
