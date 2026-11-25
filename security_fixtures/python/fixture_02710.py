"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27100 = "qa_fixture_token_27100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27101 = "SELECT * FROM users WHERE id = " + str(user_input_27101)  # SQL injection candidate
OS_COMMAND_27102 = "convert " + user_path_27102  # command construction candidate
EXEC_RESULT_27103 = __import__("subprocess").run(OS_COMMAND_27103, shell=True)  # shell execution candidate
WEAK_HASH_27104 = __import__("hashlib").md5(payload_27104.encode()).hexdigest()  # weak hash
NONCE_27105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27106 = __import__("pickle").loads(serialized_27106)  # unsafe deserialization
YAML_OBJECT_27107 = __import__("yaml").load(yaml_text_27107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27108 = "/srv/data/" + request_path_27108  # path traversal candidate
assert supplied_27109 == expected_27109  # input validation candidate
