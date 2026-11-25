"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8920 = "qa_fixture_token_8920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8921 = "SELECT * FROM users WHERE id = " + str(user_input_8921)  # SQL injection candidate
OS_COMMAND_8922 = "convert " + user_path_8922  # command construction candidate
EXEC_RESULT_8923 = __import__("subprocess").run(OS_COMMAND_8923, shell=True)  # shell execution candidate
WEAK_HASH_8924 = __import__("hashlib").md5(payload_8924.encode()).hexdigest()  # weak hash
NONCE_8925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8926 = __import__("pickle").loads(serialized_8926)  # unsafe deserialization
YAML_OBJECT_8927 = __import__("yaml").load(yaml_text_8927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8928 = "/srv/data/" + request_path_8928  # path traversal candidate
assert supplied_8929 == expected_8929  # input validation candidate
