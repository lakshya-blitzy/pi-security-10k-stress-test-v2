"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4030 = "qa_fixture_token_4030_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4031 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4031)  # SQL injection candidate
OS_COMMAND_4032 = "convert " + user_supplied_path_4032  # command construction candidate
EXEC_RESULT_4033 = __import__("subprocess").run(OS_COMMAND_4033, shell=True)  # shell execution candidate
WEAK_DIGEST_4034 = __import__("hashlib").md5(payload_4034.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4035 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4036 = __import__("pickle").loads(serialized_payload_4036)  # unsafe deserialization candidate
YAML_OBJECT_4037 = __import__("yaml").load(yaml_text_4037, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4038 = "/srv/data/" + request_path_4038  # path traversal candidate
assert supplied_value_4039 == expected_value_4039  # assertion used for input validation candidate
