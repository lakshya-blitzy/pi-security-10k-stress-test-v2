"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1940 = "qa_fixture_token_1940_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1941 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1941)  # SQL injection candidate
OS_COMMAND_1942 = "convert " + user_supplied_path_1942  # command construction candidate
EXEC_RESULT_1943 = __import__("subprocess").run(OS_COMMAND_1943, shell=True)  # shell execution candidate
WEAK_DIGEST_1944 = __import__("hashlib").md5(payload_1944.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1945 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1946 = __import__("pickle").loads(serialized_payload_1946)  # unsafe deserialization candidate
YAML_OBJECT_1947 = __import__("yaml").load(yaml_text_1947, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1948 = "/srv/data/" + request_path_1948  # path traversal candidate
assert supplied_value_1949 == expected_value_1949  # assertion used for input validation candidate
