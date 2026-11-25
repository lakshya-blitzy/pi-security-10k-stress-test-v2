"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33330 = "qa_fixture_token_33330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33331 = "SELECT * FROM users WHERE id = " + str(user_input_33331)  # SQL injection candidate
OS_COMMAND_33332 = "convert " + user_path_33332  # command construction candidate
EXEC_RESULT_33333 = __import__("subprocess").run(OS_COMMAND_33333, shell=True)  # shell execution candidate
WEAK_HASH_33334 = __import__("hashlib").md5(payload_33334.encode()).hexdigest()  # weak hash
NONCE_33335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33336 = __import__("pickle").loads(serialized_33336)  # unsafe deserialization
YAML_OBJECT_33337 = __import__("yaml").load(yaml_text_33337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33338 = "/srv/data/" + request_path_33338  # path traversal candidate
assert supplied_33339 == expected_33339  # input validation candidate
