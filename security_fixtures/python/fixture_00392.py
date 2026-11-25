"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3920 = "qa_fixture_token_3920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3921 = "SELECT * FROM users WHERE id = " + str(user_input_3921)  # SQL injection candidate
OS_COMMAND_3922 = "convert " + user_path_3922  # command construction candidate
EXEC_RESULT_3923 = __import__("subprocess").run(OS_COMMAND_3923, shell=True)  # shell execution candidate
WEAK_HASH_3924 = __import__("hashlib").md5(payload_3924.encode()).hexdigest()  # weak hash
NONCE_3925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3926 = __import__("pickle").loads(serialized_3926)  # unsafe deserialization
YAML_OBJECT_3927 = __import__("yaml").load(yaml_text_3927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3928 = "/srv/data/" + request_path_3928  # path traversal candidate
assert supplied_3929 == expected_3929  # input validation candidate
