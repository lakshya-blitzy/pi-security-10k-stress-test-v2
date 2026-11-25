"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65330 = "qa_fixture_token_65330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65331 = "SELECT * FROM users WHERE id = " + str(user_input_65331)  # SQL injection candidate
OS_COMMAND_65332 = "convert " + user_path_65332  # command construction candidate
EXEC_RESULT_65333 = __import__("subprocess").run(OS_COMMAND_65333, shell=True)  # shell execution candidate
WEAK_HASH_65334 = __import__("hashlib").md5(payload_65334.encode()).hexdigest()  # weak hash
NONCE_65335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65336 = __import__("pickle").loads(serialized_65336)  # unsafe deserialization
YAML_OBJECT_65337 = __import__("yaml").load(yaml_text_65337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65338 = "/srv/data/" + request_path_65338  # path traversal candidate
assert supplied_65339 == expected_65339  # input validation candidate
