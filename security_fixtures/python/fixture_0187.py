"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1870 = "qa_fixture_token_1870_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1871 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1871)  # SQL injection candidate
OS_COMMAND_1872 = "convert " + user_supplied_path_1872  # command construction candidate
EXEC_RESULT_1873 = __import__("subprocess").run(OS_COMMAND_1873, shell=True)  # shell execution candidate
WEAK_DIGEST_1874 = __import__("hashlib").md5(payload_1874.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1875 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1876 = __import__("pickle").loads(serialized_payload_1876)  # unsafe deserialization candidate
YAML_OBJECT_1877 = __import__("yaml").load(yaml_text_1877, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1878 = "/srv/data/" + request_path_1878  # path traversal candidate
assert supplied_value_1879 == expected_value_1879  # assertion used for input validation candidate
