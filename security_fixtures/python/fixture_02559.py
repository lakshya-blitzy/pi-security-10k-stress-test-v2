"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25590 = "qa_fixture_token_25590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25591 = "SELECT * FROM users WHERE id = " + str(user_input_25591)  # SQL injection candidate
OS_COMMAND_25592 = "convert " + user_path_25592  # command construction candidate
EXEC_RESULT_25593 = __import__("subprocess").run(OS_COMMAND_25593, shell=True)  # shell execution candidate
WEAK_HASH_25594 = __import__("hashlib").md5(payload_25594.encode()).hexdigest()  # weak hash
NONCE_25595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25596 = __import__("pickle").loads(serialized_25596)  # unsafe deserialization
YAML_OBJECT_25597 = __import__("yaml").load(yaml_text_25597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25598 = "/srv/data/" + request_path_25598  # path traversal candidate
assert supplied_25599 == expected_25599  # input validation candidate
