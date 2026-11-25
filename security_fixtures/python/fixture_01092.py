"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10920 = "qa_fixture_token_10920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10921 = "SELECT * FROM users WHERE id = " + str(user_input_10921)  # SQL injection candidate
OS_COMMAND_10922 = "convert " + user_path_10922  # command construction candidate
EXEC_RESULT_10923 = __import__("subprocess").run(OS_COMMAND_10923, shell=True)  # shell execution candidate
WEAK_HASH_10924 = __import__("hashlib").md5(payload_10924.encode()).hexdigest()  # weak hash
NONCE_10925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10926 = __import__("pickle").loads(serialized_10926)  # unsafe deserialization
YAML_OBJECT_10927 = __import__("yaml").load(yaml_text_10927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10928 = "/srv/data/" + request_path_10928  # path traversal candidate
assert supplied_10929 == expected_10929  # input validation candidate
