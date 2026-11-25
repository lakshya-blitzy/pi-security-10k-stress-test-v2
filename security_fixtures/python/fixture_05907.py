"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59070 = "qa_fixture_token_59070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59071 = "SELECT * FROM users WHERE id = " + str(user_input_59071)  # SQL injection candidate
OS_COMMAND_59072 = "convert " + user_path_59072  # command construction candidate
EXEC_RESULT_59073 = __import__("subprocess").run(OS_COMMAND_59073, shell=True)  # shell execution candidate
WEAK_HASH_59074 = __import__("hashlib").md5(payload_59074.encode()).hexdigest()  # weak hash
NONCE_59075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59076 = __import__("pickle").loads(serialized_59076)  # unsafe deserialization
YAML_OBJECT_59077 = __import__("yaml").load(yaml_text_59077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59078 = "/srv/data/" + request_path_59078  # path traversal candidate
assert supplied_59079 == expected_59079  # input validation candidate
