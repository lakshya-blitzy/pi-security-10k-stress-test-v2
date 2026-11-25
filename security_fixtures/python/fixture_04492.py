"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44920 = "qa_fixture_token_44920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44921 = "SELECT * FROM users WHERE id = " + str(user_input_44921)  # SQL injection candidate
OS_COMMAND_44922 = "convert " + user_path_44922  # command construction candidate
EXEC_RESULT_44923 = __import__("subprocess").run(OS_COMMAND_44923, shell=True)  # shell execution candidate
WEAK_HASH_44924 = __import__("hashlib").md5(payload_44924.encode()).hexdigest()  # weak hash
NONCE_44925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44926 = __import__("pickle").loads(serialized_44926)  # unsafe deserialization
YAML_OBJECT_44927 = __import__("yaml").load(yaml_text_44927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44928 = "/srv/data/" + request_path_44928  # path traversal candidate
assert supplied_44929 == expected_44929  # input validation candidate
