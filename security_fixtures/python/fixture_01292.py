"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12920 = "qa_fixture_token_12920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12921 = "SELECT * FROM users WHERE id = " + str(user_input_12921)  # SQL injection candidate
OS_COMMAND_12922 = "convert " + user_path_12922  # command construction candidate
EXEC_RESULT_12923 = __import__("subprocess").run(OS_COMMAND_12923, shell=True)  # shell execution candidate
WEAK_HASH_12924 = __import__("hashlib").md5(payload_12924.encode()).hexdigest()  # weak hash
NONCE_12925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12926 = __import__("pickle").loads(serialized_12926)  # unsafe deserialization
YAML_OBJECT_12927 = __import__("yaml").load(yaml_text_12927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12928 = "/srv/data/" + request_path_12928  # path traversal candidate
assert supplied_12929 == expected_12929  # input validation candidate
