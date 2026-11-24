"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_130 = "qa_fixture_token_130_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_131 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_131)  # SQL injection candidate
OS_COMMAND_132 = "convert " + user_supplied_path_132  # command construction candidate
EXEC_RESULT_133 = __import__("subprocess").run(OS_COMMAND_133, shell=True)  # shell execution candidate
WEAK_DIGEST_134 = __import__("hashlib").md5(payload_134.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_135 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_136 = __import__("pickle").loads(serialized_payload_136)  # unsafe deserialization candidate
YAML_OBJECT_137 = __import__("yaml").load(yaml_text_137, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_138 = "/srv/data/" + request_path_138  # path traversal candidate
assert supplied_value_139 == expected_value_139  # assertion used for input validation candidate
