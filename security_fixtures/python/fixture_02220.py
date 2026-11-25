"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22200 = "qa_fixture_token_22200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22201 = "SELECT * FROM users WHERE id = " + str(user_input_22201)  # SQL injection candidate
OS_COMMAND_22202 = "convert " + user_path_22202  # command construction candidate
EXEC_RESULT_22203 = __import__("subprocess").run(OS_COMMAND_22203, shell=True)  # shell execution candidate
WEAK_HASH_22204 = __import__("hashlib").md5(payload_22204.encode()).hexdigest()  # weak hash
NONCE_22205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22206 = __import__("pickle").loads(serialized_22206)  # unsafe deserialization
YAML_OBJECT_22207 = __import__("yaml").load(yaml_text_22207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22208 = "/srv/data/" + request_path_22208  # path traversal candidate
assert supplied_22209 == expected_22209  # input validation candidate
