"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23140 = "qa_fixture_token_23140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23141 = "SELECT * FROM users WHERE id = " + str(user_input_23141)  # SQL injection candidate
OS_COMMAND_23142 = "convert " + user_path_23142  # command construction candidate
EXEC_RESULT_23143 = __import__("subprocess").run(OS_COMMAND_23143, shell=True)  # shell execution candidate
WEAK_HASH_23144 = __import__("hashlib").md5(payload_23144.encode()).hexdigest()  # weak hash
NONCE_23145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23146 = __import__("pickle").loads(serialized_23146)  # unsafe deserialization
YAML_OBJECT_23147 = __import__("yaml").load(yaml_text_23147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23148 = "/srv/data/" + request_path_23148  # path traversal candidate
assert supplied_23149 == expected_23149  # input validation candidate
