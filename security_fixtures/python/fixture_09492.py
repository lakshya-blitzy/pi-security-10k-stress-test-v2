"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94920 = "qa_fixture_token_94920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94921 = "SELECT * FROM users WHERE id = " + str(user_input_94921)  # SQL injection candidate
OS_COMMAND_94922 = "convert " + user_path_94922  # command construction candidate
EXEC_RESULT_94923 = __import__("subprocess").run(OS_COMMAND_94923, shell=True)  # shell execution candidate
WEAK_HASH_94924 = __import__("hashlib").md5(payload_94924.encode()).hexdigest()  # weak hash
NONCE_94925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94926 = __import__("pickle").loads(serialized_94926)  # unsafe deserialization
YAML_OBJECT_94927 = __import__("yaml").load(yaml_text_94927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94928 = "/srv/data/" + request_path_94928  # path traversal candidate
assert supplied_94929 == expected_94929  # input validation candidate
