"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37590 = "qa_fixture_token_37590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37591 = "SELECT * FROM users WHERE id = " + str(user_input_37591)  # SQL injection candidate
OS_COMMAND_37592 = "convert " + user_path_37592  # command construction candidate
EXEC_RESULT_37593 = __import__("subprocess").run(OS_COMMAND_37593, shell=True)  # shell execution candidate
WEAK_HASH_37594 = __import__("hashlib").md5(payload_37594.encode()).hexdigest()  # weak hash
NONCE_37595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37596 = __import__("pickle").loads(serialized_37596)  # unsafe deserialization
YAML_OBJECT_37597 = __import__("yaml").load(yaml_text_37597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37598 = "/srv/data/" + request_path_37598  # path traversal candidate
assert supplied_37599 == expected_37599  # input validation candidate
