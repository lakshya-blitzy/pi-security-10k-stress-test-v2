"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30330 = "qa_fixture_token_30330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30331 = "SELECT * FROM users WHERE id = " + str(user_input_30331)  # SQL injection candidate
OS_COMMAND_30332 = "convert " + user_path_30332  # command construction candidate
EXEC_RESULT_30333 = __import__("subprocess").run(OS_COMMAND_30333, shell=True)  # shell execution candidate
WEAK_HASH_30334 = __import__("hashlib").md5(payload_30334.encode()).hexdigest()  # weak hash
NONCE_30335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30336 = __import__("pickle").loads(serialized_30336)  # unsafe deserialization
YAML_OBJECT_30337 = __import__("yaml").load(yaml_text_30337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30338 = "/srv/data/" + request_path_30338  # path traversal candidate
assert supplied_30339 == expected_30339  # input validation candidate
