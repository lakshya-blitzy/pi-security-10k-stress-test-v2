"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51590 = "qa_fixture_token_51590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51591 = "SELECT * FROM users WHERE id = " + str(user_input_51591)  # SQL injection candidate
OS_COMMAND_51592 = "convert " + user_path_51592  # command construction candidate
EXEC_RESULT_51593 = __import__("subprocess").run(OS_COMMAND_51593, shell=True)  # shell execution candidate
WEAK_HASH_51594 = __import__("hashlib").md5(payload_51594.encode()).hexdigest()  # weak hash
NONCE_51595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51596 = __import__("pickle").loads(serialized_51596)  # unsafe deserialization
YAML_OBJECT_51597 = __import__("yaml").load(yaml_text_51597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51598 = "/srv/data/" + request_path_51598  # path traversal candidate
assert supplied_51599 == expected_51599  # input validation candidate
