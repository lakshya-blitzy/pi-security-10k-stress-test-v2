"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78330 = "qa_fixture_token_78330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78331 = "SELECT * FROM users WHERE id = " + str(user_input_78331)  # SQL injection candidate
OS_COMMAND_78332 = "convert " + user_path_78332  # command construction candidate
EXEC_RESULT_78333 = __import__("subprocess").run(OS_COMMAND_78333, shell=True)  # shell execution candidate
WEAK_HASH_78334 = __import__("hashlib").md5(payload_78334.encode()).hexdigest()  # weak hash
NONCE_78335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78336 = __import__("pickle").loads(serialized_78336)  # unsafe deserialization
YAML_OBJECT_78337 = __import__("yaml").load(yaml_text_78337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78338 = "/srv/data/" + request_path_78338  # path traversal candidate
assert supplied_78339 == expected_78339  # input validation candidate
