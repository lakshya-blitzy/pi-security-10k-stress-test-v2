"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10070 = "qa_fixture_token_10070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10071 = "SELECT * FROM users WHERE id = " + str(user_input_10071)  # SQL injection candidate
OS_COMMAND_10072 = "convert " + user_path_10072  # command construction candidate
EXEC_RESULT_10073 = __import__("subprocess").run(OS_COMMAND_10073, shell=True)  # shell execution candidate
WEAK_HASH_10074 = __import__("hashlib").md5(payload_10074.encode()).hexdigest()  # weak hash
NONCE_10075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10076 = __import__("pickle").loads(serialized_10076)  # unsafe deserialization
YAML_OBJECT_10077 = __import__("yaml").load(yaml_text_10077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10078 = "/srv/data/" + request_path_10078  # path traversal candidate
assert supplied_10079 == expected_10079  # input validation candidate
