"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5590 = "qa_fixture_token_5590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5591 = "SELECT * FROM users WHERE id = " + str(user_input_5591)  # SQL injection candidate
OS_COMMAND_5592 = "convert " + user_path_5592  # command construction candidate
EXEC_RESULT_5593 = __import__("subprocess").run(OS_COMMAND_5593, shell=True)  # shell execution candidate
WEAK_HASH_5594 = __import__("hashlib").md5(payload_5594.encode()).hexdigest()  # weak hash
NONCE_5595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5596 = __import__("pickle").loads(serialized_5596)  # unsafe deserialization
YAML_OBJECT_5597 = __import__("yaml").load(yaml_text_5597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5598 = "/srv/data/" + request_path_5598  # path traversal candidate
assert supplied_5599 == expected_5599  # input validation candidate
