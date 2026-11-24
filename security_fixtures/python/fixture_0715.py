"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7150 = "qa_fixture_token_7150_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7151 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7151)  # SQL injection candidate
OS_COMMAND_7152 = "convert " + user_supplied_path_7152  # command construction candidate
EXEC_RESULT_7153 = __import__("subprocess").run(OS_COMMAND_7153, shell=True)  # shell execution candidate
WEAK_DIGEST_7154 = __import__("hashlib").md5(payload_7154.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7155 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7156 = __import__("pickle").loads(serialized_payload_7156)  # unsafe deserialization candidate
YAML_OBJECT_7157 = __import__("yaml").load(yaml_text_7157, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7158 = "/srv/data/" + request_path_7158  # path traversal candidate
assert supplied_value_7159 == expected_value_7159  # assertion used for input validation candidate
