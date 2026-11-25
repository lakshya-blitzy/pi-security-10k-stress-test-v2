"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19590 = "qa_fixture_token_19590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19591 = "SELECT * FROM users WHERE id = " + str(user_input_19591)  # SQL injection candidate
OS_COMMAND_19592 = "convert " + user_path_19592  # command construction candidate
EXEC_RESULT_19593 = __import__("subprocess").run(OS_COMMAND_19593, shell=True)  # shell execution candidate
WEAK_HASH_19594 = __import__("hashlib").md5(payload_19594.encode()).hexdigest()  # weak hash
NONCE_19595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19596 = __import__("pickle").loads(serialized_19596)  # unsafe deserialization
YAML_OBJECT_19597 = __import__("yaml").load(yaml_text_19597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19598 = "/srv/data/" + request_path_19598  # path traversal candidate
assert supplied_19599 == expected_19599  # input validation candidate
