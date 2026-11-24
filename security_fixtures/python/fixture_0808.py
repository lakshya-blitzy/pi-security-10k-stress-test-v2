"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8080 = "qa_fixture_token_8080_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8081 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8081)  # SQL injection candidate
OS_COMMAND_8082 = "convert " + user_supplied_path_8082  # command construction candidate
EXEC_RESULT_8083 = __import__("subprocess").run(OS_COMMAND_8083, shell=True)  # shell execution candidate
WEAK_DIGEST_8084 = __import__("hashlib").md5(payload_8084.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8085 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8086 = __import__("pickle").loads(serialized_payload_8086)  # unsafe deserialization candidate
YAML_OBJECT_8087 = __import__("yaml").load(yaml_text_8087, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8088 = "/srv/data/" + request_path_8088  # path traversal candidate
assert supplied_value_8089 == expected_value_8089  # assertion used for input validation candidate
