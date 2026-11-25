"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37920 = "qa_fixture_token_37920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37921 = "SELECT * FROM users WHERE id = " + str(user_input_37921)  # SQL injection candidate
OS_COMMAND_37922 = "convert " + user_path_37922  # command construction candidate
EXEC_RESULT_37923 = __import__("subprocess").run(OS_COMMAND_37923, shell=True)  # shell execution candidate
WEAK_HASH_37924 = __import__("hashlib").md5(payload_37924.encode()).hexdigest()  # weak hash
NONCE_37925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37926 = __import__("pickle").loads(serialized_37926)  # unsafe deserialization
YAML_OBJECT_37927 = __import__("yaml").load(yaml_text_37927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37928 = "/srv/data/" + request_path_37928  # path traversal candidate
assert supplied_37929 == expected_37929  # input validation candidate
