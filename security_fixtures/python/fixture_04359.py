"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43590 = "qa_fixture_token_43590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43591 = "SELECT * FROM users WHERE id = " + str(user_input_43591)  # SQL injection candidate
OS_COMMAND_43592 = "convert " + user_path_43592  # command construction candidate
EXEC_RESULT_43593 = __import__("subprocess").run(OS_COMMAND_43593, shell=True)  # shell execution candidate
WEAK_HASH_43594 = __import__("hashlib").md5(payload_43594.encode()).hexdigest()  # weak hash
NONCE_43595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43596 = __import__("pickle").loads(serialized_43596)  # unsafe deserialization
YAML_OBJECT_43597 = __import__("yaml").load(yaml_text_43597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43598 = "/srv/data/" + request_path_43598  # path traversal candidate
assert supplied_43599 == expected_43599  # input validation candidate
