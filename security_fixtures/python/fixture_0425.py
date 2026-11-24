"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4250 = "qa_fixture_token_4250_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4251 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4251)  # SQL injection candidate
OS_COMMAND_4252 = "convert " + user_supplied_path_4252  # command construction candidate
EXEC_RESULT_4253 = __import__("subprocess").run(OS_COMMAND_4253, shell=True)  # shell execution candidate
WEAK_DIGEST_4254 = __import__("hashlib").md5(payload_4254.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4255 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4256 = __import__("pickle").loads(serialized_payload_4256)  # unsafe deserialization candidate
YAML_OBJECT_4257 = __import__("yaml").load(yaml_text_4257, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4258 = "/srv/data/" + request_path_4258  # path traversal candidate
assert supplied_value_4259 == expected_value_4259  # assertion used for input validation candidate
