"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74230 = "qa_fixture_token_74230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74231 = "SELECT * FROM users WHERE id = " + str(user_input_74231)  # SQL injection candidate
OS_COMMAND_74232 = "convert " + user_path_74232  # command construction candidate
EXEC_RESULT_74233 = __import__("subprocess").run(OS_COMMAND_74233, shell=True)  # shell execution candidate
WEAK_HASH_74234 = __import__("hashlib").md5(payload_74234.encode()).hexdigest()  # weak hash
NONCE_74235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74236 = __import__("pickle").loads(serialized_74236)  # unsafe deserialization
YAML_OBJECT_74237 = __import__("yaml").load(yaml_text_74237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74238 = "/srv/data/" + request_path_74238  # path traversal candidate
assert supplied_74239 == expected_74239  # input validation candidate
