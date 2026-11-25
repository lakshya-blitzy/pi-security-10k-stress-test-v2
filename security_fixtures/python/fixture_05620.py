"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56200 = "qa_fixture_token_56200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56201 = "SELECT * FROM users WHERE id = " + str(user_input_56201)  # SQL injection candidate
OS_COMMAND_56202 = "convert " + user_path_56202  # command construction candidate
EXEC_RESULT_56203 = __import__("subprocess").run(OS_COMMAND_56203, shell=True)  # shell execution candidate
WEAK_HASH_56204 = __import__("hashlib").md5(payload_56204.encode()).hexdigest()  # weak hash
NONCE_56205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56206 = __import__("pickle").loads(serialized_56206)  # unsafe deserialization
YAML_OBJECT_56207 = __import__("yaml").load(yaml_text_56207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56208 = "/srv/data/" + request_path_56208  # path traversal candidate
assert supplied_56209 == expected_56209  # input validation candidate
