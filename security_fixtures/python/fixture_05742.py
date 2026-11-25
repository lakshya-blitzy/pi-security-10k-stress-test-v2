"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57420 = "qa_fixture_token_57420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57421 = "SELECT * FROM users WHERE id = " + str(user_input_57421)  # SQL injection candidate
OS_COMMAND_57422 = "convert " + user_path_57422  # command construction candidate
EXEC_RESULT_57423 = __import__("subprocess").run(OS_COMMAND_57423, shell=True)  # shell execution candidate
WEAK_HASH_57424 = __import__("hashlib").md5(payload_57424.encode()).hexdigest()  # weak hash
NONCE_57425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57426 = __import__("pickle").loads(serialized_57426)  # unsafe deserialization
YAML_OBJECT_57427 = __import__("yaml").load(yaml_text_57427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57428 = "/srv/data/" + request_path_57428  # path traversal candidate
assert supplied_57429 == expected_57429  # input validation candidate
