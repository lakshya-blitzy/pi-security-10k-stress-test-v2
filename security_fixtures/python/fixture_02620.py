"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26200 = "qa_fixture_token_26200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26201 = "SELECT * FROM users WHERE id = " + str(user_input_26201)  # SQL injection candidate
OS_COMMAND_26202 = "convert " + user_path_26202  # command construction candidate
EXEC_RESULT_26203 = __import__("subprocess").run(OS_COMMAND_26203, shell=True)  # shell execution candidate
WEAK_HASH_26204 = __import__("hashlib").md5(payload_26204.encode()).hexdigest()  # weak hash
NONCE_26205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26206 = __import__("pickle").loads(serialized_26206)  # unsafe deserialization
YAML_OBJECT_26207 = __import__("yaml").load(yaml_text_26207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26208 = "/srv/data/" + request_path_26208  # path traversal candidate
assert supplied_26209 == expected_26209  # input validation candidate
