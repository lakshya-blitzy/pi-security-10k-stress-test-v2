"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80590 = "qa_fixture_token_80590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80591 = "SELECT * FROM users WHERE id = " + str(user_input_80591)  # SQL injection candidate
OS_COMMAND_80592 = "convert " + user_path_80592  # command construction candidate
EXEC_RESULT_80593 = __import__("subprocess").run(OS_COMMAND_80593, shell=True)  # shell execution candidate
WEAK_HASH_80594 = __import__("hashlib").md5(payload_80594.encode()).hexdigest()  # weak hash
NONCE_80595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80596 = __import__("pickle").loads(serialized_80596)  # unsafe deserialization
YAML_OBJECT_80597 = __import__("yaml").load(yaml_text_80597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80598 = "/srv/data/" + request_path_80598  # path traversal candidate
assert supplied_80599 == expected_80599  # input validation candidate
