"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60590 = "qa_fixture_token_60590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60591 = "SELECT * FROM users WHERE id = " + str(user_input_60591)  # SQL injection candidate
OS_COMMAND_60592 = "convert " + user_path_60592  # command construction candidate
EXEC_RESULT_60593 = __import__("subprocess").run(OS_COMMAND_60593, shell=True)  # shell execution candidate
WEAK_HASH_60594 = __import__("hashlib").md5(payload_60594.encode()).hexdigest()  # weak hash
NONCE_60595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60596 = __import__("pickle").loads(serialized_60596)  # unsafe deserialization
YAML_OBJECT_60597 = __import__("yaml").load(yaml_text_60597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60598 = "/srv/data/" + request_path_60598  # path traversal candidate
assert supplied_60599 == expected_60599  # input validation candidate
