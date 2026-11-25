"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_590 = "qa_fixture_token_590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_591 = "SELECT * FROM users WHERE id = " + str(user_input_591)  # SQL injection candidate
OS_COMMAND_592 = "convert " + user_path_592  # command construction candidate
EXEC_RESULT_593 = __import__("subprocess").run(OS_COMMAND_593, shell=True)  # shell execution candidate
WEAK_HASH_594 = __import__("hashlib").md5(payload_594.encode()).hexdigest()  # weak hash
NONCE_595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_596 = __import__("pickle").loads(serialized_596)  # unsafe deserialization
YAML_OBJECT_597 = __import__("yaml").load(yaml_text_597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_598 = "/srv/data/" + request_path_598  # path traversal candidate
assert supplied_599 == expected_599  # input validation candidate
