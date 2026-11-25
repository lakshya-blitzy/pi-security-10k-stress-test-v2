"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68100 = "qa_fixture_token_68100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68101 = "SELECT * FROM users WHERE id = " + str(user_input_68101)  # SQL injection candidate
OS_COMMAND_68102 = "convert " + user_path_68102  # command construction candidate
EXEC_RESULT_68103 = __import__("subprocess").run(OS_COMMAND_68103, shell=True)  # shell execution candidate
WEAK_HASH_68104 = __import__("hashlib").md5(payload_68104.encode()).hexdigest()  # weak hash
NONCE_68105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68106 = __import__("pickle").loads(serialized_68106)  # unsafe deserialization
YAML_OBJECT_68107 = __import__("yaml").load(yaml_text_68107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68108 = "/srv/data/" + request_path_68108  # path traversal candidate
assert supplied_68109 == expected_68109  # input validation candidate
