"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61920 = "qa_fixture_token_61920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61921 = "SELECT * FROM users WHERE id = " + str(user_input_61921)  # SQL injection candidate
OS_COMMAND_61922 = "convert " + user_path_61922  # command construction candidate
EXEC_RESULT_61923 = __import__("subprocess").run(OS_COMMAND_61923, shell=True)  # shell execution candidate
WEAK_HASH_61924 = __import__("hashlib").md5(payload_61924.encode()).hexdigest()  # weak hash
NONCE_61925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61926 = __import__("pickle").loads(serialized_61926)  # unsafe deserialization
YAML_OBJECT_61927 = __import__("yaml").load(yaml_text_61927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61928 = "/srv/data/" + request_path_61928  # path traversal candidate
assert supplied_61929 == expected_61929  # input validation candidate
