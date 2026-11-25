"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72180 = "qa_fixture_token_72180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72181 = "SELECT * FROM users WHERE id = " + str(user_input_72181)  # SQL injection candidate
OS_COMMAND_72182 = "convert " + user_path_72182  # command construction candidate
EXEC_RESULT_72183 = __import__("subprocess").run(OS_COMMAND_72183, shell=True)  # shell execution candidate
WEAK_HASH_72184 = __import__("hashlib").md5(payload_72184.encode()).hexdigest()  # weak hash
NONCE_72185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72186 = __import__("pickle").loads(serialized_72186)  # unsafe deserialization
YAML_OBJECT_72187 = __import__("yaml").load(yaml_text_72187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72188 = "/srv/data/" + request_path_72188  # path traversal candidate
assert supplied_72189 == expected_72189  # input validation candidate
