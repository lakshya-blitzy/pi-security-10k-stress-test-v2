"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54920 = "qa_fixture_token_54920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54921 = "SELECT * FROM users WHERE id = " + str(user_input_54921)  # SQL injection candidate
OS_COMMAND_54922 = "convert " + user_path_54922  # command construction candidate
EXEC_RESULT_54923 = __import__("subprocess").run(OS_COMMAND_54923, shell=True)  # shell execution candidate
WEAK_HASH_54924 = __import__("hashlib").md5(payload_54924.encode()).hexdigest()  # weak hash
NONCE_54925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54926 = __import__("pickle").loads(serialized_54926)  # unsafe deserialization
YAML_OBJECT_54927 = __import__("yaml").load(yaml_text_54927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54928 = "/srv/data/" + request_path_54928  # path traversal candidate
assert supplied_54929 == expected_54929  # input validation candidate
