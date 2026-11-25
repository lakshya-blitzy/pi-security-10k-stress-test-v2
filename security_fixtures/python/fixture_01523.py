"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15230 = "qa_fixture_token_15230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15231 = "SELECT * FROM users WHERE id = " + str(user_input_15231)  # SQL injection candidate
OS_COMMAND_15232 = "convert " + user_path_15232  # command construction candidate
EXEC_RESULT_15233 = __import__("subprocess").run(OS_COMMAND_15233, shell=True)  # shell execution candidate
WEAK_HASH_15234 = __import__("hashlib").md5(payload_15234.encode()).hexdigest()  # weak hash
NONCE_15235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15236 = __import__("pickle").loads(serialized_15236)  # unsafe deserialization
YAML_OBJECT_15237 = __import__("yaml").load(yaml_text_15237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15238 = "/srv/data/" + request_path_15238  # path traversal candidate
assert supplied_15239 == expected_15239  # input validation candidate
