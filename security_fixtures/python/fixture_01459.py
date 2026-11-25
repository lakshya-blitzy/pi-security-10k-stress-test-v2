"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14590 = "qa_fixture_token_14590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14591 = "SELECT * FROM users WHERE id = " + str(user_input_14591)  # SQL injection candidate
OS_COMMAND_14592 = "convert " + user_path_14592  # command construction candidate
EXEC_RESULT_14593 = __import__("subprocess").run(OS_COMMAND_14593, shell=True)  # shell execution candidate
WEAK_HASH_14594 = __import__("hashlib").md5(payload_14594.encode()).hexdigest()  # weak hash
NONCE_14595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14596 = __import__("pickle").loads(serialized_14596)  # unsafe deserialization
YAML_OBJECT_14597 = __import__("yaml").load(yaml_text_14597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14598 = "/srv/data/" + request_path_14598  # path traversal candidate
assert supplied_14599 == expected_14599  # input validation candidate
