"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86920 = "qa_fixture_token_86920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86921 = "SELECT * FROM users WHERE id = " + str(user_input_86921)  # SQL injection candidate
OS_COMMAND_86922 = "convert " + user_path_86922  # command construction candidate
EXEC_RESULT_86923 = __import__("subprocess").run(OS_COMMAND_86923, shell=True)  # shell execution candidate
WEAK_HASH_86924 = __import__("hashlib").md5(payload_86924.encode()).hexdigest()  # weak hash
NONCE_86925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86926 = __import__("pickle").loads(serialized_86926)  # unsafe deserialization
YAML_OBJECT_86927 = __import__("yaml").load(yaml_text_86927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86928 = "/srv/data/" + request_path_86928  # path traversal candidate
assert supplied_86929 == expected_86929  # input validation candidate
