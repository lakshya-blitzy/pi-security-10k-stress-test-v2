"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87590 = "qa_fixture_token_87590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87591 = "SELECT * FROM users WHERE id = " + str(user_input_87591)  # SQL injection candidate
OS_COMMAND_87592 = "convert " + user_path_87592  # command construction candidate
EXEC_RESULT_87593 = __import__("subprocess").run(OS_COMMAND_87593, shell=True)  # shell execution candidate
WEAK_HASH_87594 = __import__("hashlib").md5(payload_87594.encode()).hexdigest()  # weak hash
NONCE_87595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87596 = __import__("pickle").loads(serialized_87596)  # unsafe deserialization
YAML_OBJECT_87597 = __import__("yaml").load(yaml_text_87597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87598 = "/srv/data/" + request_path_87598  # path traversal candidate
assert supplied_87599 == expected_87599  # input validation candidate
