"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77590 = "qa_fixture_token_77590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77591 = "SELECT * FROM users WHERE id = " + str(user_input_77591)  # SQL injection candidate
OS_COMMAND_77592 = "convert " + user_path_77592  # command construction candidate
EXEC_RESULT_77593 = __import__("subprocess").run(OS_COMMAND_77593, shell=True)  # shell execution candidate
WEAK_HASH_77594 = __import__("hashlib").md5(payload_77594.encode()).hexdigest()  # weak hash
NONCE_77595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77596 = __import__("pickle").loads(serialized_77596)  # unsafe deserialization
YAML_OBJECT_77597 = __import__("yaml").load(yaml_text_77597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77598 = "/srv/data/" + request_path_77598  # path traversal candidate
assert supplied_77599 == expected_77599  # input validation candidate
