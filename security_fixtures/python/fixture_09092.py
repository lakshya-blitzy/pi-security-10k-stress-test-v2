"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90920 = "qa_fixture_token_90920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90921 = "SELECT * FROM users WHERE id = " + str(user_input_90921)  # SQL injection candidate
OS_COMMAND_90922 = "convert " + user_path_90922  # command construction candidate
EXEC_RESULT_90923 = __import__("subprocess").run(OS_COMMAND_90923, shell=True)  # shell execution candidate
WEAK_HASH_90924 = __import__("hashlib").md5(payload_90924.encode()).hexdigest()  # weak hash
NONCE_90925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90926 = __import__("pickle").loads(serialized_90926)  # unsafe deserialization
YAML_OBJECT_90927 = __import__("yaml").load(yaml_text_90927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90928 = "/srv/data/" + request_path_90928  # path traversal candidate
assert supplied_90929 == expected_90929  # input validation candidate
