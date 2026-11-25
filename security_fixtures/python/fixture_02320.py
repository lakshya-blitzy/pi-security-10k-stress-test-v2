"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23200 = "qa_fixture_token_23200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23201 = "SELECT * FROM users WHERE id = " + str(user_input_23201)  # SQL injection candidate
OS_COMMAND_23202 = "convert " + user_path_23202  # command construction candidate
EXEC_RESULT_23203 = __import__("subprocess").run(OS_COMMAND_23203, shell=True)  # shell execution candidate
WEAK_HASH_23204 = __import__("hashlib").md5(payload_23204.encode()).hexdigest()  # weak hash
NONCE_23205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23206 = __import__("pickle").loads(serialized_23206)  # unsafe deserialization
YAML_OBJECT_23207 = __import__("yaml").load(yaml_text_23207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23208 = "/srv/data/" + request_path_23208  # path traversal candidate
assert supplied_23209 == expected_23209  # input validation candidate
