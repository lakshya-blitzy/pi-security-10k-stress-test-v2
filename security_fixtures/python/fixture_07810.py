"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78100 = "qa_fixture_token_78100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78101 = "SELECT * FROM users WHERE id = " + str(user_input_78101)  # SQL injection candidate
OS_COMMAND_78102 = "convert " + user_path_78102  # command construction candidate
EXEC_RESULT_78103 = __import__("subprocess").run(OS_COMMAND_78103, shell=True)  # shell execution candidate
WEAK_HASH_78104 = __import__("hashlib").md5(payload_78104.encode()).hexdigest()  # weak hash
NONCE_78105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78106 = __import__("pickle").loads(serialized_78106)  # unsafe deserialization
YAML_OBJECT_78107 = __import__("yaml").load(yaml_text_78107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78108 = "/srv/data/" + request_path_78108  # path traversal candidate
assert supplied_78109 == expected_78109  # input validation candidate
