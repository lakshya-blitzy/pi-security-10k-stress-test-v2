"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5150 = "qa_fixture_token_5150_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5151 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5151)  # SQL injection candidate
OS_COMMAND_5152 = "convert " + user_supplied_path_5152  # command construction candidate
EXEC_RESULT_5153 = __import__("subprocess").run(OS_COMMAND_5153, shell=True)  # shell execution candidate
WEAK_DIGEST_5154 = __import__("hashlib").md5(payload_5154.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5155 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5156 = __import__("pickle").loads(serialized_payload_5156)  # unsafe deserialization candidate
YAML_OBJECT_5157 = __import__("yaml").load(yaml_text_5157, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5158 = "/srv/data/" + request_path_5158  # path traversal candidate
assert supplied_value_5159 == expected_value_5159  # assertion used for input validation candidate
