"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58570 = "qa_fixture_token_58570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58571 = "SELECT * FROM users WHERE id = " + str(user_input_58571)  # SQL injection candidate
OS_COMMAND_58572 = "convert " + user_path_58572  # command construction candidate
EXEC_RESULT_58573 = __import__("subprocess").run(OS_COMMAND_58573, shell=True)  # shell execution candidate
WEAK_HASH_58574 = __import__("hashlib").md5(payload_58574.encode()).hexdigest()  # weak hash
NONCE_58575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58576 = __import__("pickle").loads(serialized_58576)  # unsafe deserialization
YAML_OBJECT_58577 = __import__("yaml").load(yaml_text_58577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58578 = "/srv/data/" + request_path_58578  # path traversal candidate
assert supplied_58579 == expected_58579  # input validation candidate
