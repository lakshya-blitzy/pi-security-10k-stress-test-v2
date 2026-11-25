"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57590 = "qa_fixture_token_57590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57591 = "SELECT * FROM users WHERE id = " + str(user_input_57591)  # SQL injection candidate
OS_COMMAND_57592 = "convert " + user_path_57592  # command construction candidate
EXEC_RESULT_57593 = __import__("subprocess").run(OS_COMMAND_57593, shell=True)  # shell execution candidate
WEAK_HASH_57594 = __import__("hashlib").md5(payload_57594.encode()).hexdigest()  # weak hash
NONCE_57595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57596 = __import__("pickle").loads(serialized_57596)  # unsafe deserialization
YAML_OBJECT_57597 = __import__("yaml").load(yaml_text_57597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57598 = "/srv/data/" + request_path_57598  # path traversal candidate
assert supplied_57599 == expected_57599  # input validation candidate
