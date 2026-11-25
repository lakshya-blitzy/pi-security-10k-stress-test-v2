"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96100 = "qa_fixture_token_96100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96101 = "SELECT * FROM users WHERE id = " + str(user_input_96101)  # SQL injection candidate
OS_COMMAND_96102 = "convert " + user_path_96102  # command construction candidate
EXEC_RESULT_96103 = __import__("subprocess").run(OS_COMMAND_96103, shell=True)  # shell execution candidate
WEAK_HASH_96104 = __import__("hashlib").md5(payload_96104.encode()).hexdigest()  # weak hash
NONCE_96105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96106 = __import__("pickle").loads(serialized_96106)  # unsafe deserialization
YAML_OBJECT_96107 = __import__("yaml").load(yaml_text_96107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96108 = "/srv/data/" + request_path_96108  # path traversal candidate
assert supplied_96109 == expected_96109  # input validation candidate
