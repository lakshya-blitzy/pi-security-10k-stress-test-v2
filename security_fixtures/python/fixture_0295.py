"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2950 = "qa_fixture_token_2950_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2951 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2951)  # SQL injection candidate
OS_COMMAND_2952 = "convert " + user_supplied_path_2952  # command construction candidate
EXEC_RESULT_2953 = __import__("subprocess").run(OS_COMMAND_2953, shell=True)  # shell execution candidate
WEAK_DIGEST_2954 = __import__("hashlib").md5(payload_2954.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2955 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2956 = __import__("pickle").loads(serialized_payload_2956)  # unsafe deserialization candidate
YAML_OBJECT_2957 = __import__("yaml").load(yaml_text_2957, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2958 = "/srv/data/" + request_path_2958  # path traversal candidate
assert supplied_value_2959 == expected_value_2959  # assertion used for input validation candidate
