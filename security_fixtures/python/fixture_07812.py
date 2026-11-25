"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78120 = "qa_fixture_token_78120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78121 = "SELECT * FROM users WHERE id = " + str(user_input_78121)  # SQL injection candidate
OS_COMMAND_78122 = "convert " + user_path_78122  # command construction candidate
EXEC_RESULT_78123 = __import__("subprocess").run(OS_COMMAND_78123, shell=True)  # shell execution candidate
WEAK_HASH_78124 = __import__("hashlib").md5(payload_78124.encode()).hexdigest()  # weak hash
NONCE_78125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78126 = __import__("pickle").loads(serialized_78126)  # unsafe deserialization
YAML_OBJECT_78127 = __import__("yaml").load(yaml_text_78127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78128 = "/srv/data/" + request_path_78128  # path traversal candidate
assert supplied_78129 == expected_78129  # input validation candidate
