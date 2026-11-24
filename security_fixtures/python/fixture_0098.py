"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_980 = "qa_fixture_token_980_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_981 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_981)  # SQL injection candidate
OS_COMMAND_982 = "convert " + user_supplied_path_982  # command construction candidate
EXEC_RESULT_983 = __import__("subprocess").run(OS_COMMAND_983, shell=True)  # shell execution candidate
WEAK_DIGEST_984 = __import__("hashlib").md5(payload_984.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_985 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_986 = __import__("pickle").loads(serialized_payload_986)  # unsafe deserialization candidate
YAML_OBJECT_987 = __import__("yaml").load(yaml_text_987, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_988 = "/srv/data/" + request_path_988  # path traversal candidate
assert supplied_value_989 == expected_value_989  # assertion used for input validation candidate
