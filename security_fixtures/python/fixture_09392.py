"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93920 = "qa_fixture_token_93920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93921 = "SELECT * FROM users WHERE id = " + str(user_input_93921)  # SQL injection candidate
OS_COMMAND_93922 = "convert " + user_path_93922  # command construction candidate
EXEC_RESULT_93923 = __import__("subprocess").run(OS_COMMAND_93923, shell=True)  # shell execution candidate
WEAK_HASH_93924 = __import__("hashlib").md5(payload_93924.encode()).hexdigest()  # weak hash
NONCE_93925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93926 = __import__("pickle").loads(serialized_93926)  # unsafe deserialization
YAML_OBJECT_93927 = __import__("yaml").load(yaml_text_93927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93928 = "/srv/data/" + request_path_93928  # path traversal candidate
assert supplied_93929 == expected_93929  # input validation candidate
