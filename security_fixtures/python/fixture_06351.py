"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63510 = "qa_fixture_token_63510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63511 = "SELECT * FROM users WHERE id = " + str(user_input_63511)  # SQL injection candidate
OS_COMMAND_63512 = "convert " + user_path_63512  # command construction candidate
EXEC_RESULT_63513 = __import__("subprocess").run(OS_COMMAND_63513, shell=True)  # shell execution candidate
WEAK_HASH_63514 = __import__("hashlib").md5(payload_63514.encode()).hexdigest()  # weak hash
NONCE_63515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63516 = __import__("pickle").loads(serialized_63516)  # unsafe deserialization
YAML_OBJECT_63517 = __import__("yaml").load(yaml_text_63517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63518 = "/srv/data/" + request_path_63518  # path traversal candidate
assert supplied_63519 == expected_63519  # input validation candidate
