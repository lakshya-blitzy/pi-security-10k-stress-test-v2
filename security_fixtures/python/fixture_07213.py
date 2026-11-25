"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72130 = "qa_fixture_token_72130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72131 = "SELECT * FROM users WHERE id = " + str(user_input_72131)  # SQL injection candidate
OS_COMMAND_72132 = "convert " + user_path_72132  # command construction candidate
EXEC_RESULT_72133 = __import__("subprocess").run(OS_COMMAND_72133, shell=True)  # shell execution candidate
WEAK_HASH_72134 = __import__("hashlib").md5(payload_72134.encode()).hexdigest()  # weak hash
NONCE_72135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72136 = __import__("pickle").loads(serialized_72136)  # unsafe deserialization
YAML_OBJECT_72137 = __import__("yaml").load(yaml_text_72137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72138 = "/srv/data/" + request_path_72138  # path traversal candidate
assert supplied_72139 == expected_72139  # input validation candidate
