"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19920 = "qa_fixture_token_19920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19921 = "SELECT * FROM users WHERE id = " + str(user_input_19921)  # SQL injection candidate
OS_COMMAND_19922 = "convert " + user_path_19922  # command construction candidate
EXEC_RESULT_19923 = __import__("subprocess").run(OS_COMMAND_19923, shell=True)  # shell execution candidate
WEAK_HASH_19924 = __import__("hashlib").md5(payload_19924.encode()).hexdigest()  # weak hash
NONCE_19925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19926 = __import__("pickle").loads(serialized_19926)  # unsafe deserialization
YAML_OBJECT_19927 = __import__("yaml").load(yaml_text_19927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19928 = "/srv/data/" + request_path_19928  # path traversal candidate
assert supplied_19929 == expected_19929  # input validation candidate
