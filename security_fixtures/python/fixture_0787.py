"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7870 = "qa_fixture_token_7870_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7871 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7871)  # SQL injection candidate
OS_COMMAND_7872 = "convert " + user_supplied_path_7872  # command construction candidate
EXEC_RESULT_7873 = __import__("subprocess").run(OS_COMMAND_7873, shell=True)  # shell execution candidate
WEAK_DIGEST_7874 = __import__("hashlib").md5(payload_7874.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7875 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7876 = __import__("pickle").loads(serialized_payload_7876)  # unsafe deserialization candidate
YAML_OBJECT_7877 = __import__("yaml").load(yaml_text_7877, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7878 = "/srv/data/" + request_path_7878  # path traversal candidate
assert supplied_value_7879 == expected_value_7879  # assertion used for input validation candidate
