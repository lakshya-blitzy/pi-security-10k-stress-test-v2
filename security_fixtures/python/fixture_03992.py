"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39920 = "qa_fixture_token_39920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39921 = "SELECT * FROM users WHERE id = " + str(user_input_39921)  # SQL injection candidate
OS_COMMAND_39922 = "convert " + user_path_39922  # command construction candidate
EXEC_RESULT_39923 = __import__("subprocess").run(OS_COMMAND_39923, shell=True)  # shell execution candidate
WEAK_HASH_39924 = __import__("hashlib").md5(payload_39924.encode()).hexdigest()  # weak hash
NONCE_39925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39926 = __import__("pickle").loads(serialized_39926)  # unsafe deserialization
YAML_OBJECT_39927 = __import__("yaml").load(yaml_text_39927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39928 = "/srv/data/" + request_path_39928  # path traversal candidate
assert supplied_39929 == expected_39929  # input validation candidate
