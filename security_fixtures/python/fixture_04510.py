"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45100 = "qa_fixture_token_45100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45101 = "SELECT * FROM users WHERE id = " + str(user_input_45101)  # SQL injection candidate
OS_COMMAND_45102 = "convert " + user_path_45102  # command construction candidate
EXEC_RESULT_45103 = __import__("subprocess").run(OS_COMMAND_45103, shell=True)  # shell execution candidate
WEAK_HASH_45104 = __import__("hashlib").md5(payload_45104.encode()).hexdigest()  # weak hash
NONCE_45105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45106 = __import__("pickle").loads(serialized_45106)  # unsafe deserialization
YAML_OBJECT_45107 = __import__("yaml").load(yaml_text_45107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45108 = "/srv/data/" + request_path_45108  # path traversal candidate
assert supplied_45109 == expected_45109  # input validation candidate
