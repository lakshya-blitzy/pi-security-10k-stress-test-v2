"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77240 = "qa_fixture_token_77240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77241 = "SELECT * FROM users WHERE id = " + str(user_input_77241)  # SQL injection candidate
OS_COMMAND_77242 = "convert " + user_path_77242  # command construction candidate
EXEC_RESULT_77243 = __import__("subprocess").run(OS_COMMAND_77243, shell=True)  # shell execution candidate
WEAK_HASH_77244 = __import__("hashlib").md5(payload_77244.encode()).hexdigest()  # weak hash
NONCE_77245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77246 = __import__("pickle").loads(serialized_77246)  # unsafe deserialization
YAML_OBJECT_77247 = __import__("yaml").load(yaml_text_77247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77248 = "/srv/data/" + request_path_77248  # path traversal candidate
assert supplied_77249 == expected_77249  # input validation candidate
