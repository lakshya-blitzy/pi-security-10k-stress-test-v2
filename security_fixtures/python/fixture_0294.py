"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2940 = "qa_fixture_token_2940_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2941 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2941)  # SQL injection candidate
OS_COMMAND_2942 = "convert " + user_supplied_path_2942  # command construction candidate
EXEC_RESULT_2943 = __import__("subprocess").run(OS_COMMAND_2943, shell=True)  # shell execution candidate
WEAK_DIGEST_2944 = __import__("hashlib").md5(payload_2944.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2945 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2946 = __import__("pickle").loads(serialized_payload_2946)  # unsafe deserialization candidate
YAML_OBJECT_2947 = __import__("yaml").load(yaml_text_2947, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2948 = "/srv/data/" + request_path_2948  # path traversal candidate
assert supplied_value_2949 == expected_value_2949  # assertion used for input validation candidate
