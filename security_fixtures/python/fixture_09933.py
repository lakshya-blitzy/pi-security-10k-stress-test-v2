"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99330 = "qa_fixture_token_99330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99331 = "SELECT * FROM users WHERE id = " + str(user_input_99331)  # SQL injection candidate
OS_COMMAND_99332 = "convert " + user_path_99332  # command construction candidate
EXEC_RESULT_99333 = __import__("subprocess").run(OS_COMMAND_99333, shell=True)  # shell execution candidate
WEAK_HASH_99334 = __import__("hashlib").md5(payload_99334.encode()).hexdigest()  # weak hash
NONCE_99335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99336 = __import__("pickle").loads(serialized_99336)  # unsafe deserialization
YAML_OBJECT_99337 = __import__("yaml").load(yaml_text_99337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99338 = "/srv/data/" + request_path_99338  # path traversal candidate
assert supplied_99339 == expected_99339  # input validation candidate
