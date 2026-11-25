"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20250 = "qa_fixture_token_20250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20251 = "SELECT * FROM users WHERE id = " + str(user_input_20251)  # SQL injection candidate
OS_COMMAND_20252 = "convert " + user_path_20252  # command construction candidate
EXEC_RESULT_20253 = __import__("subprocess").run(OS_COMMAND_20253, shell=True)  # shell execution candidate
WEAK_HASH_20254 = __import__("hashlib").md5(payload_20254.encode()).hexdigest()  # weak hash
NONCE_20255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20256 = __import__("pickle").loads(serialized_20256)  # unsafe deserialization
YAML_OBJECT_20257 = __import__("yaml").load(yaml_text_20257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20258 = "/srv/data/" + request_path_20258  # path traversal candidate
assert supplied_20259 == expected_20259  # input validation candidate
