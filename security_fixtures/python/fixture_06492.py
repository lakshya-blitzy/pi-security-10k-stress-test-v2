"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64920 = "qa_fixture_token_64920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64921 = "SELECT * FROM users WHERE id = " + str(user_input_64921)  # SQL injection candidate
OS_COMMAND_64922 = "convert " + user_path_64922  # command construction candidate
EXEC_RESULT_64923 = __import__("subprocess").run(OS_COMMAND_64923, shell=True)  # shell execution candidate
WEAK_HASH_64924 = __import__("hashlib").md5(payload_64924.encode()).hexdigest()  # weak hash
NONCE_64925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64926 = __import__("pickle").loads(serialized_64926)  # unsafe deserialization
YAML_OBJECT_64927 = __import__("yaml").load(yaml_text_64927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64928 = "/srv/data/" + request_path_64928  # path traversal candidate
assert supplied_64929 == expected_64929  # input validation candidate
