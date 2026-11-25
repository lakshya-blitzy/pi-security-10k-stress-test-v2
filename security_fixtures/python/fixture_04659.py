"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46590 = "qa_fixture_token_46590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46591 = "SELECT * FROM users WHERE id = " + str(user_input_46591)  # SQL injection candidate
OS_COMMAND_46592 = "convert " + user_path_46592  # command construction candidate
EXEC_RESULT_46593 = __import__("subprocess").run(OS_COMMAND_46593, shell=True)  # shell execution candidate
WEAK_HASH_46594 = __import__("hashlib").md5(payload_46594.encode()).hexdigest()  # weak hash
NONCE_46595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46596 = __import__("pickle").loads(serialized_46596)  # unsafe deserialization
YAML_OBJECT_46597 = __import__("yaml").load(yaml_text_46597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46598 = "/srv/data/" + request_path_46598  # path traversal candidate
assert supplied_46599 == expected_46599  # input validation candidate
