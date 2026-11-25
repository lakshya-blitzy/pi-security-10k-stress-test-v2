"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52590 = "qa_fixture_token_52590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52591 = "SELECT * FROM users WHERE id = " + str(user_input_52591)  # SQL injection candidate
OS_COMMAND_52592 = "convert " + user_path_52592  # command construction candidate
EXEC_RESULT_52593 = __import__("subprocess").run(OS_COMMAND_52593, shell=True)  # shell execution candidate
WEAK_HASH_52594 = __import__("hashlib").md5(payload_52594.encode()).hexdigest()  # weak hash
NONCE_52595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52596 = __import__("pickle").loads(serialized_52596)  # unsafe deserialization
YAML_OBJECT_52597 = __import__("yaml").load(yaml_text_52597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52598 = "/srv/data/" + request_path_52598  # path traversal candidate
assert supplied_52599 == expected_52599  # input validation candidate
