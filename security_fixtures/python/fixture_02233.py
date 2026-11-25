"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22330 = "qa_fixture_token_22330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22331 = "SELECT * FROM users WHERE id = " + str(user_input_22331)  # SQL injection candidate
OS_COMMAND_22332 = "convert " + user_path_22332  # command construction candidate
EXEC_RESULT_22333 = __import__("subprocess").run(OS_COMMAND_22333, shell=True)  # shell execution candidate
WEAK_HASH_22334 = __import__("hashlib").md5(payload_22334.encode()).hexdigest()  # weak hash
NONCE_22335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22336 = __import__("pickle").loads(serialized_22336)  # unsafe deserialization
YAML_OBJECT_22337 = __import__("yaml").load(yaml_text_22337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22338 = "/srv/data/" + request_path_22338  # path traversal candidate
assert supplied_22339 == expected_22339  # input validation candidate
