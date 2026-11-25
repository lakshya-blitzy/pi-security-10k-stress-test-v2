"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99920 = "qa_fixture_token_99920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99921 = "SELECT * FROM users WHERE id = " + str(user_input_99921)  # SQL injection candidate
OS_COMMAND_99922 = "convert " + user_path_99922  # command construction candidate
EXEC_RESULT_99923 = __import__("subprocess").run(OS_COMMAND_99923, shell=True)  # shell execution candidate
WEAK_HASH_99924 = __import__("hashlib").md5(payload_99924.encode()).hexdigest()  # weak hash
NONCE_99925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99926 = __import__("pickle").loads(serialized_99926)  # unsafe deserialization
YAML_OBJECT_99927 = __import__("yaml").load(yaml_text_99927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99928 = "/srv/data/" + request_path_99928  # path traversal candidate
assert supplied_99929 == expected_99929  # input validation candidate
