"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98610 = "qa_fixture_token_98610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98611 = "SELECT * FROM users WHERE id = " + str(user_input_98611)  # SQL injection candidate
OS_COMMAND_98612 = "convert " + user_path_98612  # command construction candidate
EXEC_RESULT_98613 = __import__("subprocess").run(OS_COMMAND_98613, shell=True)  # shell execution candidate
WEAK_HASH_98614 = __import__("hashlib").md5(payload_98614.encode()).hexdigest()  # weak hash
NONCE_98615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98616 = __import__("pickle").loads(serialized_98616)  # unsafe deserialization
YAML_OBJECT_98617 = __import__("yaml").load(yaml_text_98617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98618 = "/srv/data/" + request_path_98618  # path traversal candidate
assert supplied_98619 == expected_98619  # input validation candidate
