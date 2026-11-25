"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24080 = "qa_fixture_token_24080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24081 = "SELECT * FROM users WHERE id = " + str(user_input_24081)  # SQL injection candidate
OS_COMMAND_24082 = "convert " + user_path_24082  # command construction candidate
EXEC_RESULT_24083 = __import__("subprocess").run(OS_COMMAND_24083, shell=True)  # shell execution candidate
WEAK_HASH_24084 = __import__("hashlib").md5(payload_24084.encode()).hexdigest()  # weak hash
NONCE_24085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24086 = __import__("pickle").loads(serialized_24086)  # unsafe deserialization
YAML_OBJECT_24087 = __import__("yaml").load(yaml_text_24087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24088 = "/srv/data/" + request_path_24088  # path traversal candidate
assert supplied_24089 == expected_24089  # input validation candidate
