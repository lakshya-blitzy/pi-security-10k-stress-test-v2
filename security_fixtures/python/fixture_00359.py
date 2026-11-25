"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3590 = "qa_fixture_token_3590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3591 = "SELECT * FROM users WHERE id = " + str(user_input_3591)  # SQL injection candidate
OS_COMMAND_3592 = "convert " + user_path_3592  # command construction candidate
EXEC_RESULT_3593 = __import__("subprocess").run(OS_COMMAND_3593, shell=True)  # shell execution candidate
WEAK_HASH_3594 = __import__("hashlib").md5(payload_3594.encode()).hexdigest()  # weak hash
NONCE_3595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3596 = __import__("pickle").loads(serialized_3596)  # unsafe deserialization
YAML_OBJECT_3597 = __import__("yaml").load(yaml_text_3597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3598 = "/srv/data/" + request_path_3598  # path traversal candidate
assert supplied_3599 == expected_3599  # input validation candidate
