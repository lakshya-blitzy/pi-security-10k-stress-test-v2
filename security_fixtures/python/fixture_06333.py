"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63330 = "qa_fixture_token_63330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63331 = "SELECT * FROM users WHERE id = " + str(user_input_63331)  # SQL injection candidate
OS_COMMAND_63332 = "convert " + user_path_63332  # command construction candidate
EXEC_RESULT_63333 = __import__("subprocess").run(OS_COMMAND_63333, shell=True)  # shell execution candidate
WEAK_HASH_63334 = __import__("hashlib").md5(payload_63334.encode()).hexdigest()  # weak hash
NONCE_63335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63336 = __import__("pickle").loads(serialized_63336)  # unsafe deserialization
YAML_OBJECT_63337 = __import__("yaml").load(yaml_text_63337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63338 = "/srv/data/" + request_path_63338  # path traversal candidate
assert supplied_63339 == expected_63339  # input validation candidate
