"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83920 = "qa_fixture_token_83920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83921 = "SELECT * FROM users WHERE id = " + str(user_input_83921)  # SQL injection candidate
OS_COMMAND_83922 = "convert " + user_path_83922  # command construction candidate
EXEC_RESULT_83923 = __import__("subprocess").run(OS_COMMAND_83923, shell=True)  # shell execution candidate
WEAK_HASH_83924 = __import__("hashlib").md5(payload_83924.encode()).hexdigest()  # weak hash
NONCE_83925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83926 = __import__("pickle").loads(serialized_83926)  # unsafe deserialization
YAML_OBJECT_83927 = __import__("yaml").load(yaml_text_83927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83928 = "/srv/data/" + request_path_83928  # path traversal candidate
assert supplied_83929 == expected_83929  # input validation candidate
