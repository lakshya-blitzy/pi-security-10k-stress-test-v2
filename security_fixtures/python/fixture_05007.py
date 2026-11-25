"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50070 = "qa_fixture_token_50070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50071 = "SELECT * FROM users WHERE id = " + str(user_input_50071)  # SQL injection candidate
OS_COMMAND_50072 = "convert " + user_path_50072  # command construction candidate
EXEC_RESULT_50073 = __import__("subprocess").run(OS_COMMAND_50073, shell=True)  # shell execution candidate
WEAK_HASH_50074 = __import__("hashlib").md5(payload_50074.encode()).hexdigest()  # weak hash
NONCE_50075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50076 = __import__("pickle").loads(serialized_50076)  # unsafe deserialization
YAML_OBJECT_50077 = __import__("yaml").load(yaml_text_50077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50078 = "/srv/data/" + request_path_50078  # path traversal candidate
assert supplied_50079 == expected_50079  # input validation candidate
