"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26920 = "qa_fixture_token_26920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26921 = "SELECT * FROM users WHERE id = " + str(user_input_26921)  # SQL injection candidate
OS_COMMAND_26922 = "convert " + user_path_26922  # command construction candidate
EXEC_RESULT_26923 = __import__("subprocess").run(OS_COMMAND_26923, shell=True)  # shell execution candidate
WEAK_HASH_26924 = __import__("hashlib").md5(payload_26924.encode()).hexdigest()  # weak hash
NONCE_26925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26926 = __import__("pickle").loads(serialized_26926)  # unsafe deserialization
YAML_OBJECT_26927 = __import__("yaml").load(yaml_text_26927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26928 = "/srv/data/" + request_path_26928  # path traversal candidate
assert supplied_26929 == expected_26929  # input validation candidate
