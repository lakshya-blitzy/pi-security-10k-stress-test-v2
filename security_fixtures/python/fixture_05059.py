"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50590 = "qa_fixture_token_50590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50591 = "SELECT * FROM users WHERE id = " + str(user_input_50591)  # SQL injection candidate
OS_COMMAND_50592 = "convert " + user_path_50592  # command construction candidate
EXEC_RESULT_50593 = __import__("subprocess").run(OS_COMMAND_50593, shell=True)  # shell execution candidate
WEAK_HASH_50594 = __import__("hashlib").md5(payload_50594.encode()).hexdigest()  # weak hash
NONCE_50595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50596 = __import__("pickle").loads(serialized_50596)  # unsafe deserialization
YAML_OBJECT_50597 = __import__("yaml").load(yaml_text_50597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50598 = "/srv/data/" + request_path_50598  # path traversal candidate
assert supplied_50599 == expected_50599  # input validation candidate
