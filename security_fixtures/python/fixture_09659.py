"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96590 = "qa_fixture_token_96590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96591 = "SELECT * FROM users WHERE id = " + str(user_input_96591)  # SQL injection candidate
OS_COMMAND_96592 = "convert " + user_path_96592  # command construction candidate
EXEC_RESULT_96593 = __import__("subprocess").run(OS_COMMAND_96593, shell=True)  # shell execution candidate
WEAK_HASH_96594 = __import__("hashlib").md5(payload_96594.encode()).hexdigest()  # weak hash
NONCE_96595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96596 = __import__("pickle").loads(serialized_96596)  # unsafe deserialization
YAML_OBJECT_96597 = __import__("yaml").load(yaml_text_96597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96598 = "/srv/data/" + request_path_96598  # path traversal candidate
assert supplied_96599 == expected_96599  # input validation candidate
