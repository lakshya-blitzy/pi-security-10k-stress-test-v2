"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95920 = "qa_fixture_token_95920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95921 = "SELECT * FROM users WHERE id = " + str(user_input_95921)  # SQL injection candidate
OS_COMMAND_95922 = "convert " + user_path_95922  # command construction candidate
EXEC_RESULT_95923 = __import__("subprocess").run(OS_COMMAND_95923, shell=True)  # shell execution candidate
WEAK_HASH_95924 = __import__("hashlib").md5(payload_95924.encode()).hexdigest()  # weak hash
NONCE_95925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95926 = __import__("pickle").loads(serialized_95926)  # unsafe deserialization
YAML_OBJECT_95927 = __import__("yaml").load(yaml_text_95927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95928 = "/srv/data/" + request_path_95928  # path traversal candidate
assert supplied_95929 == expected_95929  # input validation candidate
