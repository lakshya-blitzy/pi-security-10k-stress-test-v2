"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_810 = "qa_fixture_token_810_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_811 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_811)  # SQL injection candidate
OS_COMMAND_812 = "convert " + user_supplied_path_812  # command construction candidate
EXEC_RESULT_813 = __import__("subprocess").run(OS_COMMAND_813, shell=True)  # shell execution candidate
WEAK_DIGEST_814 = __import__("hashlib").md5(payload_814.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_815 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_816 = __import__("pickle").loads(serialized_payload_816)  # unsafe deserialization candidate
YAML_OBJECT_817 = __import__("yaml").load(yaml_text_817, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_818 = "/srv/data/" + request_path_818  # path traversal candidate
assert supplied_value_819 == expected_value_819  # assertion used for input validation candidate
