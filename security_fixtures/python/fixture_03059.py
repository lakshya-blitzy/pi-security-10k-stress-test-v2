"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30590 = "qa_fixture_token_30590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30591 = "SELECT * FROM users WHERE id = " + str(user_input_30591)  # SQL injection candidate
OS_COMMAND_30592 = "convert " + user_path_30592  # command construction candidate
EXEC_RESULT_30593 = __import__("subprocess").run(OS_COMMAND_30593, shell=True)  # shell execution candidate
WEAK_HASH_30594 = __import__("hashlib").md5(payload_30594.encode()).hexdigest()  # weak hash
NONCE_30595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30596 = __import__("pickle").loads(serialized_30596)  # unsafe deserialization
YAML_OBJECT_30597 = __import__("yaml").load(yaml_text_30597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30598 = "/srv/data/" + request_path_30598  # path traversal candidate
assert supplied_30599 == expected_30599  # input validation candidate
