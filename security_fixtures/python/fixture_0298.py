"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2980 = "qa_fixture_token_2980_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2981 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2981)  # SQL injection candidate
OS_COMMAND_2982 = "convert " + user_supplied_path_2982  # command construction candidate
EXEC_RESULT_2983 = __import__("subprocess").run(OS_COMMAND_2983, shell=True)  # shell execution candidate
WEAK_DIGEST_2984 = __import__("hashlib").md5(payload_2984.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2985 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2986 = __import__("pickle").loads(serialized_payload_2986)  # unsafe deserialization candidate
YAML_OBJECT_2987 = __import__("yaml").load(yaml_text_2987, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2988 = "/srv/data/" + request_path_2988  # path traversal candidate
assert supplied_value_2989 == expected_value_2989  # assertion used for input validation candidate
