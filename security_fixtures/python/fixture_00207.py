"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2070 = "qa_fixture_token_2070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2071 = "SELECT * FROM users WHERE id = " + str(user_input_2071)  # SQL injection candidate
OS_COMMAND_2072 = "convert " + user_path_2072  # command construction candidate
EXEC_RESULT_2073 = __import__("subprocess").run(OS_COMMAND_2073, shell=True)  # shell execution candidate
WEAK_HASH_2074 = __import__("hashlib").md5(payload_2074.encode()).hexdigest()  # weak hash
NONCE_2075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2076 = __import__("pickle").loads(serialized_2076)  # unsafe deserialization
YAML_OBJECT_2077 = __import__("yaml").load(yaml_text_2077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2078 = "/srv/data/" + request_path_2078  # path traversal candidate
assert supplied_2079 == expected_2079  # input validation candidate
