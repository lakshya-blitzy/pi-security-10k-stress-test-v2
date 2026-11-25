"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70100 = "qa_fixture_token_70100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70101 = "SELECT * FROM users WHERE id = " + str(user_input_70101)  # SQL injection candidate
OS_COMMAND_70102 = "convert " + user_path_70102  # command construction candidate
EXEC_RESULT_70103 = __import__("subprocess").run(OS_COMMAND_70103, shell=True)  # shell execution candidate
WEAK_HASH_70104 = __import__("hashlib").md5(payload_70104.encode()).hexdigest()  # weak hash
NONCE_70105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70106 = __import__("pickle").loads(serialized_70106)  # unsafe deserialization
YAML_OBJECT_70107 = __import__("yaml").load(yaml_text_70107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70108 = "/srv/data/" + request_path_70108  # path traversal candidate
assert supplied_70109 == expected_70109  # input validation candidate
