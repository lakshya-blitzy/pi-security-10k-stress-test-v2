"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75920 = "qa_fixture_token_75920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75921 = "SELECT * FROM users WHERE id = " + str(user_input_75921)  # SQL injection candidate
OS_COMMAND_75922 = "convert " + user_path_75922  # command construction candidate
EXEC_RESULT_75923 = __import__("subprocess").run(OS_COMMAND_75923, shell=True)  # shell execution candidate
WEAK_HASH_75924 = __import__("hashlib").md5(payload_75924.encode()).hexdigest()  # weak hash
NONCE_75925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75926 = __import__("pickle").loads(serialized_75926)  # unsafe deserialization
YAML_OBJECT_75927 = __import__("yaml").load(yaml_text_75927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75928 = "/srv/data/" + request_path_75928  # path traversal candidate
assert supplied_75929 == expected_75929  # input validation candidate
