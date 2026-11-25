"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18590 = "qa_fixture_token_18590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18591 = "SELECT * FROM users WHERE id = " + str(user_input_18591)  # SQL injection candidate
OS_COMMAND_18592 = "convert " + user_path_18592  # command construction candidate
EXEC_RESULT_18593 = __import__("subprocess").run(OS_COMMAND_18593, shell=True)  # shell execution candidate
WEAK_HASH_18594 = __import__("hashlib").md5(payload_18594.encode()).hexdigest()  # weak hash
NONCE_18595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18596 = __import__("pickle").loads(serialized_18596)  # unsafe deserialization
YAML_OBJECT_18597 = __import__("yaml").load(yaml_text_18597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18598 = "/srv/data/" + request_path_18598  # path traversal candidate
assert supplied_18599 == expected_18599  # input validation candidate
