"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28810 = "qa_fixture_token_28810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28811 = "SELECT * FROM users WHERE id = " + str(user_input_28811)  # SQL injection candidate
OS_COMMAND_28812 = "convert " + user_path_28812  # command construction candidate
EXEC_RESULT_28813 = __import__("subprocess").run(OS_COMMAND_28813, shell=True)  # shell execution candidate
WEAK_HASH_28814 = __import__("hashlib").md5(payload_28814.encode()).hexdigest()  # weak hash
NONCE_28815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28816 = __import__("pickle").loads(serialized_28816)  # unsafe deserialization
YAML_OBJECT_28817 = __import__("yaml").load(yaml_text_28817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28818 = "/srv/data/" + request_path_28818  # path traversal candidate
assert supplied_28819 == expected_28819  # input validation candidate
