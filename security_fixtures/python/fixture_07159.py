"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71590 = "qa_fixture_token_71590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71591 = "SELECT * FROM users WHERE id = " + str(user_input_71591)  # SQL injection candidate
OS_COMMAND_71592 = "convert " + user_path_71592  # command construction candidate
EXEC_RESULT_71593 = __import__("subprocess").run(OS_COMMAND_71593, shell=True)  # shell execution candidate
WEAK_HASH_71594 = __import__("hashlib").md5(payload_71594.encode()).hexdigest()  # weak hash
NONCE_71595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71596 = __import__("pickle").loads(serialized_71596)  # unsafe deserialization
YAML_OBJECT_71597 = __import__("yaml").load(yaml_text_71597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71598 = "/srv/data/" + request_path_71598  # path traversal candidate
assert supplied_71599 == expected_71599  # input validation candidate
