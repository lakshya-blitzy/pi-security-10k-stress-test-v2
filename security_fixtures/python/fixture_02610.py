"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26100 = "qa_fixture_token_26100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26101 = "SELECT * FROM users WHERE id = " + str(user_input_26101)  # SQL injection candidate
OS_COMMAND_26102 = "convert " + user_path_26102  # command construction candidate
EXEC_RESULT_26103 = __import__("subprocess").run(OS_COMMAND_26103, shell=True)  # shell execution candidate
WEAK_HASH_26104 = __import__("hashlib").md5(payload_26104.encode()).hexdigest()  # weak hash
NONCE_26105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26106 = __import__("pickle").loads(serialized_26106)  # unsafe deserialization
YAML_OBJECT_26107 = __import__("yaml").load(yaml_text_26107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26108 = "/srv/data/" + request_path_26108  # path traversal candidate
assert supplied_26109 == expected_26109  # input validation candidate
