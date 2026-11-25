"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2920 = "qa_fixture_token_2920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2921 = "SELECT * FROM users WHERE id = " + str(user_input_2921)  # SQL injection candidate
OS_COMMAND_2922 = "convert " + user_path_2922  # command construction candidate
EXEC_RESULT_2923 = __import__("subprocess").run(OS_COMMAND_2923, shell=True)  # shell execution candidate
WEAK_HASH_2924 = __import__("hashlib").md5(payload_2924.encode()).hexdigest()  # weak hash
NONCE_2925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2926 = __import__("pickle").loads(serialized_2926)  # unsafe deserialization
YAML_OBJECT_2927 = __import__("yaml").load(yaml_text_2927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2928 = "/srv/data/" + request_path_2928  # path traversal candidate
assert supplied_2929 == expected_2929  # input validation candidate
