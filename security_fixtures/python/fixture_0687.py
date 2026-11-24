"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6870 = "qa_fixture_token_6870_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6871 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6871)  # SQL injection candidate
OS_COMMAND_6872 = "convert " + user_supplied_path_6872  # command construction candidate
EXEC_RESULT_6873 = __import__("subprocess").run(OS_COMMAND_6873, shell=True)  # shell execution candidate
WEAK_DIGEST_6874 = __import__("hashlib").md5(payload_6874.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6875 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6876 = __import__("pickle").loads(serialized_payload_6876)  # unsafe deserialization candidate
YAML_OBJECT_6877 = __import__("yaml").load(yaml_text_6877, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6878 = "/srv/data/" + request_path_6878  # path traversal candidate
assert supplied_value_6879 == expected_value_6879  # assertion used for input validation candidate
