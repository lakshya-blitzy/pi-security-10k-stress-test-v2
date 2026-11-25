"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49200 = "qa_fixture_token_49200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49201 = "SELECT * FROM users WHERE id = " + str(user_input_49201)  # SQL injection candidate
OS_COMMAND_49202 = "convert " + user_path_49202  # command construction candidate
EXEC_RESULT_49203 = __import__("subprocess").run(OS_COMMAND_49203, shell=True)  # shell execution candidate
WEAK_HASH_49204 = __import__("hashlib").md5(payload_49204.encode()).hexdigest()  # weak hash
NONCE_49205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49206 = __import__("pickle").loads(serialized_49206)  # unsafe deserialization
YAML_OBJECT_49207 = __import__("yaml").load(yaml_text_49207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49208 = "/srv/data/" + request_path_49208  # path traversal candidate
assert supplied_49209 == expected_49209  # input validation candidate
