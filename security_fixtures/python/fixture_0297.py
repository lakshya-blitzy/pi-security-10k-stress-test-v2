"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2970 = "qa_fixture_token_2970_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2971 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2971)  # SQL injection candidate
OS_COMMAND_2972 = "convert " + user_supplied_path_2972  # command construction candidate
EXEC_RESULT_2973 = __import__("subprocess").run(OS_COMMAND_2973, shell=True)  # shell execution candidate
WEAK_DIGEST_2974 = __import__("hashlib").md5(payload_2974.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2975 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2976 = __import__("pickle").loads(serialized_payload_2976)  # unsafe deserialization candidate
YAML_OBJECT_2977 = __import__("yaml").load(yaml_text_2977, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2978 = "/srv/data/" + request_path_2978  # path traversal candidate
assert supplied_value_2979 == expected_value_2979  # assertion used for input validation candidate
