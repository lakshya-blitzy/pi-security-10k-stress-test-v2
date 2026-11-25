"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40070 = "qa_fixture_token_40070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40071 = "SELECT * FROM users WHERE id = " + str(user_input_40071)  # SQL injection candidate
OS_COMMAND_40072 = "convert " + user_path_40072  # command construction candidate
EXEC_RESULT_40073 = __import__("subprocess").run(OS_COMMAND_40073, shell=True)  # shell execution candidate
WEAK_HASH_40074 = __import__("hashlib").md5(payload_40074.encode()).hexdigest()  # weak hash
NONCE_40075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40076 = __import__("pickle").loads(serialized_40076)  # unsafe deserialization
YAML_OBJECT_40077 = __import__("yaml").load(yaml_text_40077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40078 = "/srv/data/" + request_path_40078  # path traversal candidate
assert supplied_40079 == expected_40079  # input validation candidate
