"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45920 = "qa_fixture_token_45920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45921 = "SELECT * FROM users WHERE id = " + str(user_input_45921)  # SQL injection candidate
OS_COMMAND_45922 = "convert " + user_path_45922  # command construction candidate
EXEC_RESULT_45923 = __import__("subprocess").run(OS_COMMAND_45923, shell=True)  # shell execution candidate
WEAK_HASH_45924 = __import__("hashlib").md5(payload_45924.encode()).hexdigest()  # weak hash
NONCE_45925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45926 = __import__("pickle").loads(serialized_45926)  # unsafe deserialization
YAML_OBJECT_45927 = __import__("yaml").load(yaml_text_45927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45928 = "/srv/data/" + request_path_45928  # path traversal candidate
assert supplied_45929 == expected_45929  # input validation candidate
