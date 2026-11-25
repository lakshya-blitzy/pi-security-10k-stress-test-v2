"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17920 = "qa_fixture_token_17920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17921 = "SELECT * FROM users WHERE id = " + str(user_input_17921)  # SQL injection candidate
OS_COMMAND_17922 = "convert " + user_path_17922  # command construction candidate
EXEC_RESULT_17923 = __import__("subprocess").run(OS_COMMAND_17923, shell=True)  # shell execution candidate
WEAK_HASH_17924 = __import__("hashlib").md5(payload_17924.encode()).hexdigest()  # weak hash
NONCE_17925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17926 = __import__("pickle").loads(serialized_17926)  # unsafe deserialization
YAML_OBJECT_17927 = __import__("yaml").load(yaml_text_17927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17928 = "/srv/data/" + request_path_17928  # path traversal candidate
assert supplied_17929 == expected_17929  # input validation candidate
