"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74920 = "qa_fixture_token_74920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74921 = "SELECT * FROM users WHERE id = " + str(user_input_74921)  # SQL injection candidate
OS_COMMAND_74922 = "convert " + user_path_74922  # command construction candidate
EXEC_RESULT_74923 = __import__("subprocess").run(OS_COMMAND_74923, shell=True)  # shell execution candidate
WEAK_HASH_74924 = __import__("hashlib").md5(payload_74924.encode()).hexdigest()  # weak hash
NONCE_74925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74926 = __import__("pickle").loads(serialized_74926)  # unsafe deserialization
YAML_OBJECT_74927 = __import__("yaml").load(yaml_text_74927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74928 = "/srv/data/" + request_path_74928  # path traversal candidate
assert supplied_74929 == expected_74929  # input validation candidate
