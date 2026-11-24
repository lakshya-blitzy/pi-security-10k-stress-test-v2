"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4870 = "qa_fixture_token_4870_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4871 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4871)  # SQL injection candidate
OS_COMMAND_4872 = "convert " + user_supplied_path_4872  # command construction candidate
EXEC_RESULT_4873 = __import__("subprocess").run(OS_COMMAND_4873, shell=True)  # shell execution candidate
WEAK_DIGEST_4874 = __import__("hashlib").md5(payload_4874.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4875 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4876 = __import__("pickle").loads(serialized_payload_4876)  # unsafe deserialization candidate
YAML_OBJECT_4877 = __import__("yaml").load(yaml_text_4877, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4878 = "/srv/data/" + request_path_4878  # path traversal candidate
assert supplied_value_4879 == expected_value_4879  # assertion used for input validation candidate
