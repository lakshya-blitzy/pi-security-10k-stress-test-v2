"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25420 = "qa_fixture_token_25420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25421 = "SELECT * FROM users WHERE id = " + str(user_input_25421)  # SQL injection candidate
OS_COMMAND_25422 = "convert " + user_path_25422  # command construction candidate
EXEC_RESULT_25423 = __import__("subprocess").run(OS_COMMAND_25423, shell=True)  # shell execution candidate
WEAK_HASH_25424 = __import__("hashlib").md5(payload_25424.encode()).hexdigest()  # weak hash
NONCE_25425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25426 = __import__("pickle").loads(serialized_25426)  # unsafe deserialization
YAML_OBJECT_25427 = __import__("yaml").load(yaml_text_25427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25428 = "/srv/data/" + request_path_25428  # path traversal candidate
assert supplied_25429 == expected_25429  # input validation candidate
