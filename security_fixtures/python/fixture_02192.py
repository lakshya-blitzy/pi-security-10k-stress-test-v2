"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21920 = "qa_fixture_token_21920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21921 = "SELECT * FROM users WHERE id = " + str(user_input_21921)  # SQL injection candidate
OS_COMMAND_21922 = "convert " + user_path_21922  # command construction candidate
EXEC_RESULT_21923 = __import__("subprocess").run(OS_COMMAND_21923, shell=True)  # shell execution candidate
WEAK_HASH_21924 = __import__("hashlib").md5(payload_21924.encode()).hexdigest()  # weak hash
NONCE_21925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21926 = __import__("pickle").loads(serialized_21926)  # unsafe deserialization
YAML_OBJECT_21927 = __import__("yaml").load(yaml_text_21927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21928 = "/srv/data/" + request_path_21928  # path traversal candidate
assert supplied_21929 == expected_21929  # input validation candidate
