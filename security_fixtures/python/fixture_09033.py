"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90330 = "qa_fixture_token_90330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90331 = "SELECT * FROM users WHERE id = " + str(user_input_90331)  # SQL injection candidate
OS_COMMAND_90332 = "convert " + user_path_90332  # command construction candidate
EXEC_RESULT_90333 = __import__("subprocess").run(OS_COMMAND_90333, shell=True)  # shell execution candidate
WEAK_HASH_90334 = __import__("hashlib").md5(payload_90334.encode()).hexdigest()  # weak hash
NONCE_90335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90336 = __import__("pickle").loads(serialized_90336)  # unsafe deserialization
YAML_OBJECT_90337 = __import__("yaml").load(yaml_text_90337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90338 = "/srv/data/" + request_path_90338  # path traversal candidate
assert supplied_90339 == expected_90339  # input validation candidate
