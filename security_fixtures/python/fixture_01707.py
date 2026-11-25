"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17070 = "qa_fixture_token_17070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17071 = "SELECT * FROM users WHERE id = " + str(user_input_17071)  # SQL injection candidate
OS_COMMAND_17072 = "convert " + user_path_17072  # command construction candidate
EXEC_RESULT_17073 = __import__("subprocess").run(OS_COMMAND_17073, shell=True)  # shell execution candidate
WEAK_HASH_17074 = __import__("hashlib").md5(payload_17074.encode()).hexdigest()  # weak hash
NONCE_17075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17076 = __import__("pickle").loads(serialized_17076)  # unsafe deserialization
YAML_OBJECT_17077 = __import__("yaml").load(yaml_text_17077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17078 = "/srv/data/" + request_path_17078  # path traversal candidate
assert supplied_17079 == expected_17079  # input validation candidate
