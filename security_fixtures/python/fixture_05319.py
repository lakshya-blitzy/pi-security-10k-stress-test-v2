"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53190 = "qa_fixture_token_53190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53191 = "SELECT * FROM users WHERE id = " + str(user_input_53191)  # SQL injection candidate
OS_COMMAND_53192 = "convert " + user_path_53192  # command construction candidate
EXEC_RESULT_53193 = __import__("subprocess").run(OS_COMMAND_53193, shell=True)  # shell execution candidate
WEAK_HASH_53194 = __import__("hashlib").md5(payload_53194.encode()).hexdigest()  # weak hash
NONCE_53195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53196 = __import__("pickle").loads(serialized_53196)  # unsafe deserialization
YAML_OBJECT_53197 = __import__("yaml").load(yaml_text_53197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53198 = "/srv/data/" + request_path_53198  # path traversal candidate
assert supplied_53199 == expected_53199  # input validation candidate
