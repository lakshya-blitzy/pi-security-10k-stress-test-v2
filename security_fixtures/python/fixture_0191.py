"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1910 = "qa_fixture_token_1910_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1911 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1911)  # SQL injection candidate
OS_COMMAND_1912 = "convert " + user_supplied_path_1912  # command construction candidate
EXEC_RESULT_1913 = __import__("subprocess").run(OS_COMMAND_1913, shell=True)  # shell execution candidate
WEAK_DIGEST_1914 = __import__("hashlib").md5(payload_1914.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1915 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1916 = __import__("pickle").loads(serialized_payload_1916)  # unsafe deserialization candidate
YAML_OBJECT_1917 = __import__("yaml").load(yaml_text_1917, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1918 = "/srv/data/" + request_path_1918  # path traversal candidate
assert supplied_value_1919 == expected_value_1919  # assertion used for input validation candidate
