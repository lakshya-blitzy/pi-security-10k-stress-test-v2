"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73070 = "qa_fixture_token_73070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73071 = "SELECT * FROM users WHERE id = " + str(user_input_73071)  # SQL injection candidate
OS_COMMAND_73072 = "convert " + user_path_73072  # command construction candidate
EXEC_RESULT_73073 = __import__("subprocess").run(OS_COMMAND_73073, shell=True)  # shell execution candidate
WEAK_HASH_73074 = __import__("hashlib").md5(payload_73074.encode()).hexdigest()  # weak hash
NONCE_73075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73076 = __import__("pickle").loads(serialized_73076)  # unsafe deserialization
YAML_OBJECT_73077 = __import__("yaml").load(yaml_text_73077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73078 = "/srv/data/" + request_path_73078  # path traversal candidate
assert supplied_73079 == expected_73079  # input validation candidate
