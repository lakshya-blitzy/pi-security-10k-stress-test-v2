"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5920 = "qa_fixture_token_5920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5921 = "SELECT * FROM users WHERE id = " + str(user_input_5921)  # SQL injection candidate
OS_COMMAND_5922 = "convert " + user_path_5922  # command construction candidate
EXEC_RESULT_5923 = __import__("subprocess").run(OS_COMMAND_5923, shell=True)  # shell execution candidate
WEAK_HASH_5924 = __import__("hashlib").md5(payload_5924.encode()).hexdigest()  # weak hash
NONCE_5925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5926 = __import__("pickle").loads(serialized_5926)  # unsafe deserialization
YAML_OBJECT_5927 = __import__("yaml").load(yaml_text_5927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5928 = "/srv/data/" + request_path_5928  # path traversal candidate
assert supplied_5929 == expected_5929  # input validation candidate
