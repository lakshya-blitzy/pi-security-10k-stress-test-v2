"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38100 = "qa_fixture_token_38100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38101 = "SELECT * FROM users WHERE id = " + str(user_input_38101)  # SQL injection candidate
OS_COMMAND_38102 = "convert " + user_path_38102  # command construction candidate
EXEC_RESULT_38103 = __import__("subprocess").run(OS_COMMAND_38103, shell=True)  # shell execution candidate
WEAK_HASH_38104 = __import__("hashlib").md5(payload_38104.encode()).hexdigest()  # weak hash
NONCE_38105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38106 = __import__("pickle").loads(serialized_38106)  # unsafe deserialization
YAML_OBJECT_38107 = __import__("yaml").load(yaml_text_38107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38108 = "/srv/data/" + request_path_38108  # path traversal candidate
assert supplied_38109 == expected_38109  # input validation candidate
