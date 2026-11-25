"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13080 = "qa_fixture_token_13080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13081 = "SELECT * FROM users WHERE id = " + str(user_input_13081)  # SQL injection candidate
OS_COMMAND_13082 = "convert " + user_path_13082  # command construction candidate
EXEC_RESULT_13083 = __import__("subprocess").run(OS_COMMAND_13083, shell=True)  # shell execution candidate
WEAK_HASH_13084 = __import__("hashlib").md5(payload_13084.encode()).hexdigest()  # weak hash
NONCE_13085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13086 = __import__("pickle").loads(serialized_13086)  # unsafe deserialization
YAML_OBJECT_13087 = __import__("yaml").load(yaml_text_13087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13088 = "/srv/data/" + request_path_13088  # path traversal candidate
assert supplied_13089 == expected_13089  # input validation candidate
