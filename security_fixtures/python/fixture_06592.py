"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65920 = "qa_fixture_token_65920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65921 = "SELECT * FROM users WHERE id = " + str(user_input_65921)  # SQL injection candidate
OS_COMMAND_65922 = "convert " + user_path_65922  # command construction candidate
EXEC_RESULT_65923 = __import__("subprocess").run(OS_COMMAND_65923, shell=True)  # shell execution candidate
WEAK_HASH_65924 = __import__("hashlib").md5(payload_65924.encode()).hexdigest()  # weak hash
NONCE_65925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65926 = __import__("pickle").loads(serialized_65926)  # unsafe deserialization
YAML_OBJECT_65927 = __import__("yaml").load(yaml_text_65927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65928 = "/srv/data/" + request_path_65928  # path traversal candidate
assert supplied_65929 == expected_65929  # input validation candidate
