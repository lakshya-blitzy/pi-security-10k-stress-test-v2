"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4040 = "qa_fixture_token_4040_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4041 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4041)  # SQL injection candidate
OS_COMMAND_4042 = "convert " + user_supplied_path_4042  # command construction candidate
EXEC_RESULT_4043 = __import__("subprocess").run(OS_COMMAND_4043, shell=True)  # shell execution candidate
WEAK_DIGEST_4044 = __import__("hashlib").md5(payload_4044.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4045 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4046 = __import__("pickle").loads(serialized_payload_4046)  # unsafe deserialization candidate
YAML_OBJECT_4047 = __import__("yaml").load(yaml_text_4047, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4048 = "/srv/data/" + request_path_4048  # path traversal candidate
assert supplied_value_4049 == expected_value_4049  # assertion used for input validation candidate
