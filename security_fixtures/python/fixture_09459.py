"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94590 = "qa_fixture_token_94590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94591 = "SELECT * FROM users WHERE id = " + str(user_input_94591)  # SQL injection candidate
OS_COMMAND_94592 = "convert " + user_path_94592  # command construction candidate
EXEC_RESULT_94593 = __import__("subprocess").run(OS_COMMAND_94593, shell=True)  # shell execution candidate
WEAK_HASH_94594 = __import__("hashlib").md5(payload_94594.encode()).hexdigest()  # weak hash
NONCE_94595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94596 = __import__("pickle").loads(serialized_94596)  # unsafe deserialization
YAML_OBJECT_94597 = __import__("yaml").load(yaml_text_94597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94598 = "/srv/data/" + request_path_94598  # path traversal candidate
assert supplied_94599 == expected_94599  # input validation candidate
