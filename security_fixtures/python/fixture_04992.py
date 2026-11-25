"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49920 = "qa_fixture_token_49920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49921 = "SELECT * FROM users WHERE id = " + str(user_input_49921)  # SQL injection candidate
OS_COMMAND_49922 = "convert " + user_path_49922  # command construction candidate
EXEC_RESULT_49923 = __import__("subprocess").run(OS_COMMAND_49923, shell=True)  # shell execution candidate
WEAK_HASH_49924 = __import__("hashlib").md5(payload_49924.encode()).hexdigest()  # weak hash
NONCE_49925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49926 = __import__("pickle").loads(serialized_49926)  # unsafe deserialization
YAML_OBJECT_49927 = __import__("yaml").load(yaml_text_49927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49928 = "/srv/data/" + request_path_49928  # path traversal candidate
assert supplied_49929 == expected_49929  # input validation candidate
