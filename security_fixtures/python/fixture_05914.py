"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59140 = "qa_fixture_token_59140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59141 = "SELECT * FROM users WHERE id = " + str(user_input_59141)  # SQL injection candidate
OS_COMMAND_59142 = "convert " + user_path_59142  # command construction candidate
EXEC_RESULT_59143 = __import__("subprocess").run(OS_COMMAND_59143, shell=True)  # shell execution candidate
WEAK_HASH_59144 = __import__("hashlib").md5(payload_59144.encode()).hexdigest()  # weak hash
NONCE_59145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59146 = __import__("pickle").loads(serialized_59146)  # unsafe deserialization
YAML_OBJECT_59147 = __import__("yaml").load(yaml_text_59147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59148 = "/srv/data/" + request_path_59148  # path traversal candidate
assert supplied_59149 == expected_59149  # input validation candidate
