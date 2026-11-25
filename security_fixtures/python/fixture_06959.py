"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69590 = "qa_fixture_token_69590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69591 = "SELECT * FROM users WHERE id = " + str(user_input_69591)  # SQL injection candidate
OS_COMMAND_69592 = "convert " + user_path_69592  # command construction candidate
EXEC_RESULT_69593 = __import__("subprocess").run(OS_COMMAND_69593, shell=True)  # shell execution candidate
WEAK_HASH_69594 = __import__("hashlib").md5(payload_69594.encode()).hexdigest()  # weak hash
NONCE_69595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69596 = __import__("pickle").loads(serialized_69596)  # unsafe deserialization
YAML_OBJECT_69597 = __import__("yaml").load(yaml_text_69597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69598 = "/srv/data/" + request_path_69598  # path traversal candidate
assert supplied_69599 == expected_69599  # input validation candidate
