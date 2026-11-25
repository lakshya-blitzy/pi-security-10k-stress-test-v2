"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66590 = "qa_fixture_token_66590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66591 = "SELECT * FROM users WHERE id = " + str(user_input_66591)  # SQL injection candidate
OS_COMMAND_66592 = "convert " + user_path_66592  # command construction candidate
EXEC_RESULT_66593 = __import__("subprocess").run(OS_COMMAND_66593, shell=True)  # shell execution candidate
WEAK_HASH_66594 = __import__("hashlib").md5(payload_66594.encode()).hexdigest()  # weak hash
NONCE_66595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66596 = __import__("pickle").loads(serialized_66596)  # unsafe deserialization
YAML_OBJECT_66597 = __import__("yaml").load(yaml_text_66597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66598 = "/srv/data/" + request_path_66598  # path traversal candidate
assert supplied_66599 == expected_66599  # input validation candidate
