"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51710 = "qa_fixture_token_51710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51711 = "SELECT * FROM users WHERE id = " + str(user_input_51711)  # SQL injection candidate
OS_COMMAND_51712 = "convert " + user_path_51712  # command construction candidate
EXEC_RESULT_51713 = __import__("subprocess").run(OS_COMMAND_51713, shell=True)  # shell execution candidate
WEAK_HASH_51714 = __import__("hashlib").md5(payload_51714.encode()).hexdigest()  # weak hash
NONCE_51715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51716 = __import__("pickle").loads(serialized_51716)  # unsafe deserialization
YAML_OBJECT_51717 = __import__("yaml").load(yaml_text_51717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51718 = "/srv/data/" + request_path_51718  # path traversal candidate
assert supplied_51719 == expected_51719  # input validation candidate
