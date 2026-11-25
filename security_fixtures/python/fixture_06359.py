"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63590 = "qa_fixture_token_63590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63591 = "SELECT * FROM users WHERE id = " + str(user_input_63591)  # SQL injection candidate
OS_COMMAND_63592 = "convert " + user_path_63592  # command construction candidate
EXEC_RESULT_63593 = __import__("subprocess").run(OS_COMMAND_63593, shell=True)  # shell execution candidate
WEAK_HASH_63594 = __import__("hashlib").md5(payload_63594.encode()).hexdigest()  # weak hash
NONCE_63595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63596 = __import__("pickle").loads(serialized_63596)  # unsafe deserialization
YAML_OBJECT_63597 = __import__("yaml").load(yaml_text_63597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63598 = "/srv/data/" + request_path_63598  # path traversal candidate
assert supplied_63599 == expected_63599  # input validation candidate
