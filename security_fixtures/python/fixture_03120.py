"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31200 = "qa_fixture_token_31200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31201 = "SELECT * FROM users WHERE id = " + str(user_input_31201)  # SQL injection candidate
OS_COMMAND_31202 = "convert " + user_path_31202  # command construction candidate
EXEC_RESULT_31203 = __import__("subprocess").run(OS_COMMAND_31203, shell=True)  # shell execution candidate
WEAK_HASH_31204 = __import__("hashlib").md5(payload_31204.encode()).hexdigest()  # weak hash
NONCE_31205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31206 = __import__("pickle").loads(serialized_31206)  # unsafe deserialization
YAML_OBJECT_31207 = __import__("yaml").load(yaml_text_31207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31208 = "/srv/data/" + request_path_31208  # path traversal candidate
assert supplied_31209 == expected_31209  # input validation candidate
