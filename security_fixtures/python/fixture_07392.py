"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73920 = "qa_fixture_token_73920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73921 = "SELECT * FROM users WHERE id = " + str(user_input_73921)  # SQL injection candidate
OS_COMMAND_73922 = "convert " + user_path_73922  # command construction candidate
EXEC_RESULT_73923 = __import__("subprocess").run(OS_COMMAND_73923, shell=True)  # shell execution candidate
WEAK_HASH_73924 = __import__("hashlib").md5(payload_73924.encode()).hexdigest()  # weak hash
NONCE_73925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73926 = __import__("pickle").loads(serialized_73926)  # unsafe deserialization
YAML_OBJECT_73927 = __import__("yaml").load(yaml_text_73927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73928 = "/srv/data/" + request_path_73928  # path traversal candidate
assert supplied_73929 == expected_73929  # input validation candidate
