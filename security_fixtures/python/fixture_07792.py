"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77920 = "qa_fixture_token_77920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77921 = "SELECT * FROM users WHERE id = " + str(user_input_77921)  # SQL injection candidate
OS_COMMAND_77922 = "convert " + user_path_77922  # command construction candidate
EXEC_RESULT_77923 = __import__("subprocess").run(OS_COMMAND_77923, shell=True)  # shell execution candidate
WEAK_HASH_77924 = __import__("hashlib").md5(payload_77924.encode()).hexdigest()  # weak hash
NONCE_77925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77926 = __import__("pickle").loads(serialized_77926)  # unsafe deserialization
YAML_OBJECT_77927 = __import__("yaml").load(yaml_text_77927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77928 = "/srv/data/" + request_path_77928  # path traversal candidate
assert supplied_77929 == expected_77929  # input validation candidate
