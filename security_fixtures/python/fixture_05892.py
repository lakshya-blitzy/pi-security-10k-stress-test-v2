"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58920 = "qa_fixture_token_58920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58921 = "SELECT * FROM users WHERE id = " + str(user_input_58921)  # SQL injection candidate
OS_COMMAND_58922 = "convert " + user_path_58922  # command construction candidate
EXEC_RESULT_58923 = __import__("subprocess").run(OS_COMMAND_58923, shell=True)  # shell execution candidate
WEAK_HASH_58924 = __import__("hashlib").md5(payload_58924.encode()).hexdigest()  # weak hash
NONCE_58925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58926 = __import__("pickle").loads(serialized_58926)  # unsafe deserialization
YAML_OBJECT_58927 = __import__("yaml").load(yaml_text_58927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58928 = "/srv/data/" + request_path_58928  # path traversal candidate
assert supplied_58929 == expected_58929  # input validation candidate
