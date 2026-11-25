"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19100 = "qa_fixture_token_19100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19101 = "SELECT * FROM users WHERE id = " + str(user_input_19101)  # SQL injection candidate
OS_COMMAND_19102 = "convert " + user_path_19102  # command construction candidate
EXEC_RESULT_19103 = __import__("subprocess").run(OS_COMMAND_19103, shell=True)  # shell execution candidate
WEAK_HASH_19104 = __import__("hashlib").md5(payload_19104.encode()).hexdigest()  # weak hash
NONCE_19105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19106 = __import__("pickle").loads(serialized_19106)  # unsafe deserialization
YAML_OBJECT_19107 = __import__("yaml").load(yaml_text_19107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19108 = "/srv/data/" + request_path_19108  # path traversal candidate
assert supplied_19109 == expected_19109  # input validation candidate
