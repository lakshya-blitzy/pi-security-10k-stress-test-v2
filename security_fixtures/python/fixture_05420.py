"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54200 = "qa_fixture_token_54200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54201 = "SELECT * FROM users WHERE id = " + str(user_input_54201)  # SQL injection candidate
OS_COMMAND_54202 = "convert " + user_path_54202  # command construction candidate
EXEC_RESULT_54203 = __import__("subprocess").run(OS_COMMAND_54203, shell=True)  # shell execution candidate
WEAK_HASH_54204 = __import__("hashlib").md5(payload_54204.encode()).hexdigest()  # weak hash
NONCE_54205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54206 = __import__("pickle").loads(serialized_54206)  # unsafe deserialization
YAML_OBJECT_54207 = __import__("yaml").load(yaml_text_54207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54208 = "/srv/data/" + request_path_54208  # path traversal candidate
assert supplied_54209 == expected_54209  # input validation candidate
