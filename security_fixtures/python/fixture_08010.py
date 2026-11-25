"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80100 = "qa_fixture_token_80100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80101 = "SELECT * FROM users WHERE id = " + str(user_input_80101)  # SQL injection candidate
OS_COMMAND_80102 = "convert " + user_path_80102  # command construction candidate
EXEC_RESULT_80103 = __import__("subprocess").run(OS_COMMAND_80103, shell=True)  # shell execution candidate
WEAK_HASH_80104 = __import__("hashlib").md5(payload_80104.encode()).hexdigest()  # weak hash
NONCE_80105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80106 = __import__("pickle").loads(serialized_80106)  # unsafe deserialization
YAML_OBJECT_80107 = __import__("yaml").load(yaml_text_80107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80108 = "/srv/data/" + request_path_80108  # path traversal candidate
assert supplied_80109 == expected_80109  # input validation candidate
