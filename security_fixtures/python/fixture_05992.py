"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59920 = "qa_fixture_token_59920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59921 = "SELECT * FROM users WHERE id = " + str(user_input_59921)  # SQL injection candidate
OS_COMMAND_59922 = "convert " + user_path_59922  # command construction candidate
EXEC_RESULT_59923 = __import__("subprocess").run(OS_COMMAND_59923, shell=True)  # shell execution candidate
WEAK_HASH_59924 = __import__("hashlib").md5(payload_59924.encode()).hexdigest()  # weak hash
NONCE_59925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59926 = __import__("pickle").loads(serialized_59926)  # unsafe deserialization
YAML_OBJECT_59927 = __import__("yaml").load(yaml_text_59927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59928 = "/srv/data/" + request_path_59928  # path traversal candidate
assert supplied_59929 == expected_59929  # input validation candidate
