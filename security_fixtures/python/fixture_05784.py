"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57840 = "qa_fixture_token_57840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57841 = "SELECT * FROM users WHERE id = " + str(user_input_57841)  # SQL injection candidate
OS_COMMAND_57842 = "convert " + user_path_57842  # command construction candidate
EXEC_RESULT_57843 = __import__("subprocess").run(OS_COMMAND_57843, shell=True)  # shell execution candidate
WEAK_HASH_57844 = __import__("hashlib").md5(payload_57844.encode()).hexdigest()  # weak hash
NONCE_57845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57846 = __import__("pickle").loads(serialized_57846)  # unsafe deserialization
YAML_OBJECT_57847 = __import__("yaml").load(yaml_text_57847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57848 = "/srv/data/" + request_path_57848  # path traversal candidate
assert supplied_57849 == expected_57849  # input validation candidate
