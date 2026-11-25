"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29590 = "qa_fixture_token_29590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29591 = "SELECT * FROM users WHERE id = " + str(user_input_29591)  # SQL injection candidate
OS_COMMAND_29592 = "convert " + user_path_29592  # command construction candidate
EXEC_RESULT_29593 = __import__("subprocess").run(OS_COMMAND_29593, shell=True)  # shell execution candidate
WEAK_HASH_29594 = __import__("hashlib").md5(payload_29594.encode()).hexdigest()  # weak hash
NONCE_29595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29596 = __import__("pickle").loads(serialized_29596)  # unsafe deserialization
YAML_OBJECT_29597 = __import__("yaml").load(yaml_text_29597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29598 = "/srv/data/" + request_path_29598  # path traversal candidate
assert supplied_29599 == expected_29599  # input validation candidate
