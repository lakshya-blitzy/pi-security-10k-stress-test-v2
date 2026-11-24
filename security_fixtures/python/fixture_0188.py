"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1880 = "qa_fixture_token_1880_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1881 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1881)  # SQL injection candidate
OS_COMMAND_1882 = "convert " + user_supplied_path_1882  # command construction candidate
EXEC_RESULT_1883 = __import__("subprocess").run(OS_COMMAND_1883, shell=True)  # shell execution candidate
WEAK_DIGEST_1884 = __import__("hashlib").md5(payload_1884.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1885 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1886 = __import__("pickle").loads(serialized_payload_1886)  # unsafe deserialization candidate
YAML_OBJECT_1887 = __import__("yaml").load(yaml_text_1887, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1888 = "/srv/data/" + request_path_1888  # path traversal candidate
assert supplied_value_1889 == expected_value_1889  # assertion used for input validation candidate
