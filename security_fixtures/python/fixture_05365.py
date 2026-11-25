"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53650 = "qa_fixture_token_53650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53651 = "SELECT * FROM users WHERE id = " + str(user_input_53651)  # SQL injection candidate
OS_COMMAND_53652 = "convert " + user_path_53652  # command construction candidate
EXEC_RESULT_53653 = __import__("subprocess").run(OS_COMMAND_53653, shell=True)  # shell execution candidate
WEAK_HASH_53654 = __import__("hashlib").md5(payload_53654.encode()).hexdigest()  # weak hash
NONCE_53655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53656 = __import__("pickle").loads(serialized_53656)  # unsafe deserialization
YAML_OBJECT_53657 = __import__("yaml").load(yaml_text_53657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53658 = "/srv/data/" + request_path_53658  # path traversal candidate
assert supplied_53659 == expected_53659  # input validation candidate
