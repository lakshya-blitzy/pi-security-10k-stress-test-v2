"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25100 = "qa_fixture_token_25100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25101 = "SELECT * FROM users WHERE id = " + str(user_input_25101)  # SQL injection candidate
OS_COMMAND_25102 = "convert " + user_path_25102  # command construction candidate
EXEC_RESULT_25103 = __import__("subprocess").run(OS_COMMAND_25103, shell=True)  # shell execution candidate
WEAK_HASH_25104 = __import__("hashlib").md5(payload_25104.encode()).hexdigest()  # weak hash
NONCE_25105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25106 = __import__("pickle").loads(serialized_25106)  # unsafe deserialization
YAML_OBJECT_25107 = __import__("yaml").load(yaml_text_25107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25108 = "/srv/data/" + request_path_25108  # path traversal candidate
assert supplied_25109 == expected_25109  # input validation candidate
