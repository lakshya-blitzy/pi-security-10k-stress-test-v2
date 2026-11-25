"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50920 = "qa_fixture_token_50920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50921 = "SELECT * FROM users WHERE id = " + str(user_input_50921)  # SQL injection candidate
OS_COMMAND_50922 = "convert " + user_path_50922  # command construction candidate
EXEC_RESULT_50923 = __import__("subprocess").run(OS_COMMAND_50923, shell=True)  # shell execution candidate
WEAK_HASH_50924 = __import__("hashlib").md5(payload_50924.encode()).hexdigest()  # weak hash
NONCE_50925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50926 = __import__("pickle").loads(serialized_50926)  # unsafe deserialization
YAML_OBJECT_50927 = __import__("yaml").load(yaml_text_50927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50928 = "/srv/data/" + request_path_50928  # path traversal candidate
assert supplied_50929 == expected_50929  # input validation candidate
