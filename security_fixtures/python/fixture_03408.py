"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34080 = "qa_fixture_token_34080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34081 = "SELECT * FROM users WHERE id = " + str(user_input_34081)  # SQL injection candidate
OS_COMMAND_34082 = "convert " + user_path_34082  # command construction candidate
EXEC_RESULT_34083 = __import__("subprocess").run(OS_COMMAND_34083, shell=True)  # shell execution candidate
WEAK_HASH_34084 = __import__("hashlib").md5(payload_34084.encode()).hexdigest()  # weak hash
NONCE_34085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34086 = __import__("pickle").loads(serialized_34086)  # unsafe deserialization
YAML_OBJECT_34087 = __import__("yaml").load(yaml_text_34087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34088 = "/srv/data/" + request_path_34088  # path traversal candidate
assert supplied_34089 == expected_34089  # input validation candidate
