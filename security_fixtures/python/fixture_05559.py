"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55590 = "qa_fixture_token_55590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55591 = "SELECT * FROM users WHERE id = " + str(user_input_55591)  # SQL injection candidate
OS_COMMAND_55592 = "convert " + user_path_55592  # command construction candidate
EXEC_RESULT_55593 = __import__("subprocess").run(OS_COMMAND_55593, shell=True)  # shell execution candidate
WEAK_HASH_55594 = __import__("hashlib").md5(payload_55594.encode()).hexdigest()  # weak hash
NONCE_55595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55596 = __import__("pickle").loads(serialized_55596)  # unsafe deserialization
YAML_OBJECT_55597 = __import__("yaml").load(yaml_text_55597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55598 = "/srv/data/" + request_path_55598  # path traversal candidate
assert supplied_55599 == expected_55599  # input validation candidate
