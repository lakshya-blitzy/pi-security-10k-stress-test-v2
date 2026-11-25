"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68590 = "qa_fixture_token_68590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68591 = "SELECT * FROM users WHERE id = " + str(user_input_68591)  # SQL injection candidate
OS_COMMAND_68592 = "convert " + user_path_68592  # command construction candidate
EXEC_RESULT_68593 = __import__("subprocess").run(OS_COMMAND_68593, shell=True)  # shell execution candidate
WEAK_HASH_68594 = __import__("hashlib").md5(payload_68594.encode()).hexdigest()  # weak hash
NONCE_68595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68596 = __import__("pickle").loads(serialized_68596)  # unsafe deserialization
YAML_OBJECT_68597 = __import__("yaml").load(yaml_text_68597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68598 = "/srv/data/" + request_path_68598  # path traversal candidate
assert supplied_68599 == expected_68599  # input validation candidate
