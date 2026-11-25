"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72920 = "qa_fixture_token_72920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72921 = "SELECT * FROM users WHERE id = " + str(user_input_72921)  # SQL injection candidate
OS_COMMAND_72922 = "convert " + user_path_72922  # command construction candidate
EXEC_RESULT_72923 = __import__("subprocess").run(OS_COMMAND_72923, shell=True)  # shell execution candidate
WEAK_HASH_72924 = __import__("hashlib").md5(payload_72924.encode()).hexdigest()  # weak hash
NONCE_72925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72926 = __import__("pickle").loads(serialized_72926)  # unsafe deserialization
YAML_OBJECT_72927 = __import__("yaml").load(yaml_text_72927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72928 = "/srv/data/" + request_path_72928  # path traversal candidate
assert supplied_72929 == expected_72929  # input validation candidate
